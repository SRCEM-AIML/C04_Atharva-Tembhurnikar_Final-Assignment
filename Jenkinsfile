pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building Flask and Django applications...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying with Docker Compose...'
            }
        }
    }
}
