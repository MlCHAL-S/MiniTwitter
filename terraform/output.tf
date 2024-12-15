output "MiniTwitter_server_public_ip" {
  value       = aws_instance.MiniTwitter_server.public_ip
  description = "Public IP of the MiniTwitter server EC2 instance"
}