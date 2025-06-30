pipeline {
  agent any

  environment {
    SENSOR_IMAGE = "your-aws-account-id.dkr.ecr.us-east-1.amazonaws.com/iot-telemetry-sensor-emulator"
    COLLECTOR_IMAGE = "your-aws-account-id.dkr.ecr.us-east-1.amazonaws.com/iot-telemetry-data-collector"
    API_IMAGE = "your-aws-account-id.dkr.ecr.us-east-1.amazonaws.com/iot-telemetry-api-server"
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/yourusername/iot-telemetry-monitoring.git'
      }
    }

    stage('Build Docker Images') {
      steps {
        script {
          sh 'docker build -t $SENSOR_IMAGE ./sensor-emulator'
          sh 'docker build -t $COLLECTOR_IMAGE ./data-collector'
          sh 'docker build -t $API_IMAGE ./api-server'
        }
      }
    }

    stage('Push to ECR') {
      steps {
        script {
          sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $SENSOR_IMAGE'
          sh 'docker push $SENSOR_IMAGE'
          sh 'docker push $COLLECTOR_IMAGE'
          sh 'docker push $API_IMAGE'
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f k8s/namespace.yaml'
        sh 'kubectl apply -f k8s/data-collector.yaml'
        sh 'kubectl apply -f k8s/sensor-emulator.yaml'
        sh 'kubectl apply -f k8s/api-server.yaml'
        sh 'kubectl apply -f k8s/hpa-api-server.yaml'
        sh 'kubectl apply -f k8s/network-policy.yaml'
        sh 'kubectl apply -f k8s/ingress-api-server.yaml'
      }
    }
  }
}
