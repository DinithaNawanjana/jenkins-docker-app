pipeline {
    agent any

    environment {
        DOCKER_CREDS=credentials('docker-hub-login')
        REGISTRY_USER='dinitha282'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting code from GitHub...'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t jenkins-docker-app .'
            }
        }
        stage('Push Docker Image') {
            steps {
                echo 'Pushing Docker Image...'
                sh 'docker push ${REGISTRY_USER}/jenkins-docker-app'
            }
        }
        stage ('Run Container') {
            steps {
                echo 'Running Container....'
                sh 'docker run -d --name jenkins-docker-app ${REGISTRY_USER}/jenkins-docker-app'
            }
        }
        stage ('Finish'){
            steps{
                echo 'Pipeline completed Successfully....'
            }
        }

    }
}