/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('test') {
            steps {
                sh 'echo test stage: Running unit tests'
                sh 'python -m unittest discover tests "*_tests.py"'
            }
        }
        stage('build pyz') {
            steps {
                sh 'echo build stage: Creating pyz archive in /build'
                sh 'python -m zipapp src/main.py -o build/firstJenkinsPythonDeployment.pyz -p "/usr/bin/env python" -c'
            }
        }
        stage('Checkout from github') {
            steps {
                sh 'pwd'
                dir('my-new-folder') {
                    sh "pwd"
                }
            }
        }
    }
}
