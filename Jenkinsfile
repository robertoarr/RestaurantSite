pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'if [ "$(docker ps -aq -f name=redis_develop_cont)" ]; then docker rm -f redis_develop_cont; fi'
                sh 'docker run -d -p 6379:6379 --name redis_develop_cont redis:2.8'
                sh 'if [ "$(docker ps -aq -f name=mysql_develop_cont)" ]; then docker rm -f mysql_develop_cont; fi'
                sh 'docker run -d -e MYSQL_ROOT_PASSWORD=root -p 3308:3306 --name mysql_develop_cont mysql/mysql-server:8.0.11'
                sh 'while [ "$(docker inspect -f {{.State.Health.Status}} mysql_develop_cont)" != "healthy" ]; do sleep 10; done'
                sh "docker exec mysql_develop_cont mysql -u root --password=root -e 'CREATE DATABASE restaurant_site; CREATE USER 'test_user'@'%' IDENTIFIED WITH mysql_native_password BY 'Temporal123.'; GRANT ALL PRIVILEGES ON restaurant_site.* TO 'test_user'@'%';'"
                sh 'cp /home/roberto/Projects/jenkins/.env_tests .env'
                sh "docker build -t api_image:${env.BUILD_NUMBER} ."
            }
        }
        stage('Test'){
            steps {
                sh "docker run --rm api_image:${env.BUILD_NUMBER} python manage.py test --noinput -k"
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