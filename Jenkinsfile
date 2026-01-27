pipeline {
    agent any

    stages {
        statge ('Checkout'){
            steps{
                echo 'Getting code from GitHub...'
            }
        }
        statge ('Test Application'){
            steps{
                echo 'Testing python code'
                sh 'python3 main.py'
            }
        }
        statge ('Finish'){
            steps{
                echo 'Pipelne completed Successfully....'
            }
        }

    }
}