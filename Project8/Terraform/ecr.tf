resource "aws_ecr_repository" "sensor_emulator" {
  name = "${var.project_name}-sensor-emulator"
}

resource "aws_ecr_repository" "data_collector" {
  name = "${var.project_name}-data-collector"
}

resource "aws_ecr_repository" "api_server" {
  name = "${var.project_name}-api-server"
}
