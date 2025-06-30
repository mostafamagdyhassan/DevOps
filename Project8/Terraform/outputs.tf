output "cluster_name" {
  value = module.eks.cluster_name
}

output "ecr_sensor_emulator_url" {
  value = aws_ecr_repository.sensor_emulator.repository_url
}

output "ecr_data_collector_url" {
  value = aws_ecr_repository.data_collector.repository_url
}

output "ecr_api_server_url" {
  value = aws_ecr_repository.api_server.repository_url
}
