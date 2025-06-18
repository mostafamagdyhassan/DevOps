
pipeline {
  agent any

  environment {
    AWS_REGION = 'us-east-1'
    AWS_ACCOUNT_ID = '<your-aws-account-id>'
    BACKEND_IMAGE = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/flaskapp"
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/user112001/test.git', branch: 'main'
      }
    }

    stage('Login to ECR') {
      steps {
        sh '''
          aws ecr get-login-password --region $AWS_REGION |           docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $BACKEND_IMAGE:latest ./app'
      }
    }

    stage('Push to ECR') {
      steps {
        sh 'docker push $BACKEND_IMAGE:latest'
      }
    }

    stage('Deploy to EKS') {
      steps {
        sh '''
          aws eks --region $AWS_REGION update-kubeconfig --name task-cluster
          kubectl apply -f k8s/deployment.yaml
          kubectl apply -f k8s/service.yaml
        '''
      }
    }
  }
}
