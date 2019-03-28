pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'ls'
                sh 'pwd'
                sh 'docker ps'
                sh 'cp /home/roberto/Projects/jenkins/.env_tests .'
                step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: false])
                sh 'docker ps'
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
