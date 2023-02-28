/* Requires the Docker Pipeline plugin */
pipeline {
//     agent { docker { image 'python:3.10.7-alpine' } }
    agent { docker { image 'python:latest' } }

//     tools {
//         git 'agent-git'
//     }

    stages {
        stage('test') {
            steps {
                sh 'echo test stage: Running unit tests'
                sh 'python -m unittest discover tests "*_tests.py"'
            }
        }
        stage('build pyz') {
            steps {
                dir('build') {
                    sh 'echo build stage: Creating pyz archive in /build'
                    sh 'python -m zipapp ../src/main.py -o firstJenkinsPythonDeployment.pyz -p "/usr/bin/env python" -c'
                }

            }
        }
        stage('Checkout from github') {
            steps {
                sh 'echo Outer: `pwd`'
                dir('temp-subfolder') {
                   // The below will clone your repo and will be checked out to master branch by default.
                   git url: 'https://github.com/jimcturner/firstjenkinsdeployrepo.git'
                   // Do a ls -lart to view all the files are cloned. It will be clonned. This is just for you to be sure about it.
                   sh "ls -lart ./*"
                   sh 'echo Inner: `pwd`'
                   sh 'cp ../build/* .'
                   sh "ls -lart ./*"
                   sh 'echo `whereis git`'
                   sh 'git add *'
                   sh 'rm .git/config.lock'
                   sh 'git config --global user.name "jimcturner"'
                   sh '/usr/bin/git push -u origin master'
                }
            }
        }
    }
}
