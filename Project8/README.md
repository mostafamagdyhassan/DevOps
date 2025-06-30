 IoT Telemetry Monitoring DevOps project

 # IoT Telemetry Monitoring DevOps Project

This project simulates an IoT telemetry system using:

- Python Microservices
- Docker & Kubernetes (EKS)
- Jenkins CI/CD Pipeline
- AWS (ECR, EKS, Terraform)
- Prometheus + Grafana Monitoring

## Components

- `sensor-emulator`: generates synthetic telemetry data
- `data-collector`: ingests and stores data, exposes metrics
- `api-server`: REST API to view aggregated metrics

## DevOps Stack

- Infrastructure: Terraform + AWS (EKS, ECR, VPC)
- CI/CD: Jenkinsfile builds/pushes/deploys images
- Monitoring: Prometheus + Grafana dashboards

## Setup

1. `terraform init && terraform apply`
2. Push Docker images to ECR
3. Apply Kubernetes YAMLs
4. Set up Ingress and DNS
5. Access API via `http://api.iot.local/summary`


iot-telemetry-monitoring/
├── sensor-emulator/
│   ├── sensor_emulator.py
│   └── Dockerfile
├── data-collector/
│   ├── data_collector.py
│   └── Dockerfile
├── api-server/
│   ├── api_server.py
│   └── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── k8s/
│   ├── namespace.yaml
│   ├── sensor-emulator.yaml
│   ├── data-collector.yaml
│   ├── api-server.yaml
│   ├── hpa-api-server.yaml
│   ├── network-policy.yaml
│   └── ingress-api-server.yaml
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── eks.tf
│   ├── ecr.tf
│   ├── outputs.tf
│   └── main.tf
├── README.md
└── commands.txt
