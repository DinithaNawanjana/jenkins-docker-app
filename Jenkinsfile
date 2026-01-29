pipeline {
    agent any
    
    environment {
        // අර අපි හදපු ID එක මෙතන දෙනවා
        DOCKER_CREDS = credentials('docker-hub-login')
        // ඔබේ Docker Hub නම මෙතන දාන්න
        REGISTRY_USER = 'YOUR_DOCKERHUB_USERNAME' 
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code...'
            }
        }
        
        stage('Build Image') {
            steps {
                // Image එකට නම දෙනකොට "username/image-name" විදියට දෙන්න ඕන
                sh "docker build -t ${REGISTRY_USER}/my-python-app:v1 ."
            }
        }
        
        stage('Login to Docker Hub') {
            steps {
                // මෙතන Jenkins රහසිගතව Log වෙනවා
                sh "echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin"
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
                // සර්වර් එකේ ඉඩ ඉතුරු කරගන්න පරණ Image මකනවා
                sh "docker rmi ${REGISTRY_USER}/my-python-app:v1"
            }
        }
    }
}