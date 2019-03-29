pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'cp /home/roberto/Projects/jenkins/.env_tests .env'
                sh 'docker-compose -f build.yml up -d --remove-orphans'
            }
        }
        stage('Test'){
            steps {
                sh 'docker-compose -f build.yml run --rm api-build python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose -f deploy.yml up -d'
            }
        }
    }
}
