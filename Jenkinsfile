pipeline {
    agent any

    stages {
        stage ('Checkout'){
            steps{
                echo 'Getting code from GitHub...'
            }
        }
        stage ('Build Docker Image'){
            steps{
                echo 'Testing python code'
                sh 'docker build -t jenkins-docker-app .'
            }
        }
        stage ('Test Docker Container'){
            steps{
                echo 'Testing Docker Container'
                sh 'docker run -d --name jenkins-docker-app jenkins-docker-app'
            }
        }
        stage ('Finish'){
            steps{
                echo 'Pipeline completed Successfully....'
            }
        }

    }
}