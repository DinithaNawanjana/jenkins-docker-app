pipeline {
    agent any

    stages {
        stage ('Checkout'){
            steps{
                echo 'Getting code from GitHub...'
            }
        }
        stage ('Test Application'){
            steps{
                echo 'Testing python code'
                sh 'python3 main.py'
            }
        }
        stage ('Finish'){
            steps{
                echo 'Pipelne completed Successfully....'
            }
        }

    }
}