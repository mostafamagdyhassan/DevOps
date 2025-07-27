output "vpc_id" {
  value = module.vpc.vpc_id
}

output "ec2_instance_id" {
  value = aws_instance.web.id
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}
