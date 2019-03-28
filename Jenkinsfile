pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build') {
            steps {
                sh 'python manage runserver 0:8000'
            }
        }
    }
}
