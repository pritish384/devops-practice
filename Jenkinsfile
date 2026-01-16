pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Check Python') {
            steps {
                sh 'python --version'
            }
        }

        stage('Run App') {
            steps {
                sh 'python app/index.py'
            }
        }
    }
}
