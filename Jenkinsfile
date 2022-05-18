pipeline{
    agent { label '(built-in)' } 

    environment {
        DOCKERHUB_CREDINTIALS = credentials('dockerhub')
    }

    stages {
        stage ('git clone') {
            steps {
                git 'https://github.com/ndrohith09/spark-jenkins.git'
            }
        }
        stage ('Test file'){
            steps {
                sh 'python spark.py' 
            }
        }
        stage ('Build'){
            steps {
                sh 'docker build -t ndrohith09/spark-jenkins:latest .' 
            }
        }

        stage ('Login'){
            steps {
                sh 'echo $DOCEKRHUB_CREDINTIALS | docker login -U $DOCKERHUB_CREDINTIALS_USR --password-stdin' 
                // sh 'echo $DOCEKRHUB_CREDINTIALS | docker login --username=${DOCKERHUB_CREDINTIALS.username} --password=${DOCKERHUB_CREDINTIALS.password}' 
            }
        }

        stage ('Push'){
            steps {
                sh 'docker push ndrohith09/spark-jenkins:latest .' 
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}