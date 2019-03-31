pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'if [ "$(docker ps -aq -f name=redis_test_cont)" ]; then docker rm -f redis_test_cont; fi'
                sh 'docker run -d -p 6378:6379 --name redis_test_cont redis:2.8'
                sh 'if [ "$(docker ps -aq -f name=mysql_test_cont)" ]; then docker rm -f mysql_test_cont; fi'
                sh 'docker run -d -e MYSQL_ROOT_PASSWORD=root -p 3309:3306 -v /home/roberto/Projects/jenkins/start_db.sql:/start_db.sql --name mysql_test_cont mysql/mysql-server:8.0.11'
                sh 'while [ "$(docker inspect -f {{.State.Health.Status}} mysql_test_cont)" != "healthy" ]; do sleep 10; done'
                sh "docker exec mysql_test_cont /bin/sh -c 'mysql -u root --password=root < /start_db.sql'"
                sh "docker build -t api_image:${env.BUILD_NUMBER} ."
            }
        }
        stage('Test'){
            steps {
                sh "docker run --rm -v /home/roberto/Projects/jenkins/.env_tests:.env api_image:${env.BUILD_NUMBER} python manage.py test --noinput -k"
            }
            post {
               always {
                    sh 'if [ "$(docker ps -aq -f name=redis_test_cont)" ]; then docker rm -f redis_test_cont; fi'
                    sh 'if [ "$(docker ps -aq -f name=mysql_test_cont)" ]; then docker rm -f mysql_test_cont; fi'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'if [ "$(docker ps -aq -f name=redis_develop_cont)" ]; then docker rm -f redis_develop_cont; fi'
                sh 'docker run -d -p 6379:6379 --name redis_develop_cont redis:2.8'
                sh 'if [ "$(docker ps -aq -f name=mysql_develop_cont)" ]; then docker rm -f mysql_develop_cont; fi'
                sh 'docker run -d -e MYSQL_ROOT_PASSWORD=root -p 3308:3306 -v /home/roberto/Projects/jenkins/start_db.sql:/start_db.sql --name mysql_develop_cont mysql/mysql-server:8.0.11'
                sh 'while [ "$(docker inspect -f {{.State.Health.Status}} mysql_develop_cont)" != "healthy" ]; do sleep 10; done'
                sh "docker exec mysql_develop_cont /bin/sh -c 'mysql -u root --password=root < /start_db.sql'"
                sh 'if [ "$(docker ps -aq -f name=api_develop_cont)" ]; then docker rm -f api_develop_cont; fi'
                sh "docker run -d -t -e PYTHONUNBUFFERED=0 -p 8000:8000 -v /home/roberto/Projects/jenkins/.env_develop:.env --name api_develop_cont api_image:${env.BUILD_NUMBER} python manage.py runserver 0:8000"
                sh "docker exec api_develop_cont python manage.py migrate"
            }
        }
    }
}