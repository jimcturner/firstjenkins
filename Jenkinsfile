/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'echo hello from Jenkins project pipeline build stage!!!!!'
            }
        }
        stage('test') {
            steps {
                sh 'echo hello from Jenkins project pipeline test stage!!!!!'
            }
        }
    }
}
