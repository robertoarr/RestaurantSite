pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
        stage('Test'){
            steps {
                sh 'ls'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python manage.py runserver 0:8000'
            }
        }
    }
}
