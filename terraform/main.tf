# main.tf
provider "aws" {
  region = var.region
}

# VPC for MiniTwitter
resource "aws_vpc" "MiniTwitter_vpc" {
  cidr_block = var.vpc_cidr
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "MiniTwitter-VPC"
  }
}

# Subnet for MiniTwitter
resource "aws_subnet" "MiniTwitter_subnet" {
  vpc_id                  = aws_vpc.MiniTwitter_vpc.id
  cidr_block              = var.subnet_cidr
  map_public_ip_on_launch = true
  tags = {
    Name = "MiniTwitter-Subnet"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "MiniTwitter_igw" {
  vpc_id = aws_vpc.MiniTwitter_vpc.id
  tags = {
    Name = "MiniTwitter-IGW"
  }
}

# Route Table
resource "aws_route_table" "MiniTwitter_route_table" {
  vpc_id = aws_vpc.MiniTwitter_vpc.id
  tags = {
    Name = "MiniTwitter-RouteTable"
  }

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.MiniTwitter_igw.id
  }
}

# Route Table Association
resource "aws_route_table_association" "MiniTwitter_rta" {
  subnet_id      = aws_subnet.MiniTwitter_subnet.id
  route_table_id = aws_route_table.MiniTwitter_route_table.id
}

# Security Group for MiniTwitter allowing SSH and gRPC (50051)
resource "aws_security_group" "MiniTwitter_sg" {
  vpc_id = aws_vpc.MiniTwitter_vpc.id
  tags = {
    Name = "MiniTwitter-SG"
  }

  # Allow SSH from anywhere
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow gRPC communication on port 50051
  ingress {
    from_port   = 50051
    to_port     = 50051
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound traffic (default all)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance to run MiniTwitter server
resource "aws_instance" "MiniTwitter_server" {
  ami                     = var.ami_id
  instance_type           = var.instance_type
  subnet_id               = aws_subnet.MiniTwitter_subnet.id
  vpc_security_group_ids  = [aws_security_group.MiniTwitter_sg.id]

  key_name = "ansible"

  tags = {
    Name = "MiniTwitter-Server"
  }
}

# Generate Ansible Inventory with Public IP
resource "null_resource" "create_inventory" {
  depends_on = [aws_instance.MiniTwitter_server]

  provisioner "local-exec" {
    command = <<EOT
      echo "[server]\n${aws_instance.MiniTwitter_server.public_ip} ansible_user=ec2-user" > ../ansible/inventory.ini
    EOT
  }
}
