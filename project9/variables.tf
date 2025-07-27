variable "aws_region" {
  default = "ap-south-1"
}

variable "ami_id" {
  description = "AMI ID for EC2 instance"
  type        = string
}

variable "key_name" {
  description = "EC2 Key pair name"
  type        = string
}

variable "public_key" {
  description = "Public key content for key pair"
  type        = string
}

variable "db_password" {
  description = "PostgreSQL password"
  type        = string
  sensitive   = true
}

variable "allow_ssh_cidr" {
  description = "CIDR for SSH access"
  default     = "0.0.0.0/0"
}
variable "domain_name" {
  description = "Your domain name (e.g., example.com)"
  type        = string
}

variable "subdomain" {
  description = "Subdomain for web app (e.g., app.example.com -> use app)"
  type        = string
}
