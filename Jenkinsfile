pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'cp /home/roberto/Projects/jenkins/.env_tests .env'
                sh 'docker-compose up -f build.yml -d --build'
            }
        }
        stage('Test'){
            steps {
                sh 'docker-compose -f build.yml run --rm back python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -f deploy.yml -d'
            }
        }
    }
}
