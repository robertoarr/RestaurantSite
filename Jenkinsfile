pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'cp /home/roberto/Projects/jenkins/.env_tests .env'
                sh "docker build -t api_image:${env.BUILD_NUMBER} ."
            }
        }
        stage('Test'){
            steps {
                sh "docker exec -it mysql_cont mysql -u root --password=root -e 'CREATE DATABASE test_restaurant_site;'"
                sh "docker run --rm api_image:${env.BUILD_NUMBER} python manage.py test --noinput -k"
                sh "docker exec -it mysql_cont mysql -u root --password=root -e 'DROP DATABASE test_restaurant_site;'"
            }
        }
        stage('Deploy') {
            steps {
                sh 'if [ "$(docker ps -aq -f name=api_develop_cont)" ]; then docker rm -f api_develop_cont; fi'
                sh "docker run -d -t -e PYTHONUNBUFFERED=0 -p 8000:8000 --rm --name api_develop_cont api_image:${env.BUILD_NUMBER} python manage.py runserver 0:8000"
            }
        }
    }
}