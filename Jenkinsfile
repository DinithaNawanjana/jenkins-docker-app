pipeline {
    agent any
    
    environment {
        
        DOCKER_CREDS = credentials('docker-hub-login')
        
        REGISTRY_USER = 'dinitha282'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code...'
            }
        }
        
        stage('Build Image') {
            steps {
                
                sh "docker build ${REGISTRY_USER}/my-python-app:v1 ."
            }
        }
        
        stage('Login to Docker Hub') {
            steps {
                
                sh 'echo ${DOCKER_CREDS_PSW} | docker login -u ${DOCKER_CREDS_USR} --password-stdin'
            }
        }
        
        stage('Push Image') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh "docker push ${REGISTRY_USER}/my-python-app:v1"
            }
        }
        
        stage('Cleanup') {
            steps {
                
                sh "docker rmi ${REGISTRY_USER}/my-python-app:v1"
            }
        }
    }
}