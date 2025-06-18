
pipeline {
  agent any

  environment {
    IMAGE_NAME = 'mostafa/devops-blueocean'
    IMAGE_TAG = 'latest'
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
      }
    }

    stage('Build App') {
      steps {
        echo 'Building app...'
        sh 'npm install'
      }
    }

    stage('Test') {
      steps {
        echo 'Running tests...'
        sh 'npm test'
      }
    }

    stage('Build Docker Image') {
      steps {
        echo 'Building Docker image...'
        sh '''
          docker build -t $IMAGE_NAME:$IMAGE_TAG .
        '''
      }
    }

    stage('Push to Docker Hub') {
      steps {
        echo 'Pushing image...'
        sh '''
          echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
          docker push $IMAGE_NAME:$IMAGE_TAG
        '''
      }
    }
  }

  post {
    always {
      echo 'Pipeline finished.'
      sh 'docker logout'
    }
  }
}
