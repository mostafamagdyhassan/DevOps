 IoT Telemetry Monitoring DevOps project

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
