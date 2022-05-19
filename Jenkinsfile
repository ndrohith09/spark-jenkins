pipeline{
    agent { label '(built-in)' } 

    environment {
        DOCKERHUB_CREDINTIALS = credentials('dockerhub')
    }

    stages {
        // stage ('git clone') {
        //     steps {
        //         git 'https://github.com/ndrohith09/spark-jenkins.git'
        //     }
        // }
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
                sh 'echo $DOCEKRHUB_CREDINTIALS_PSW | docker login -U $DOCKERHUB_CREDINTIALS_USR --password-stdin' 
                // sh 'echo $DOCEKRHUB_CREDINTIALS | docker login --username=${DOCKERHUB_CREDINTIALS.username} --password=${DOCKERHUB_CREDINTIALS.password}' 
            }
        }

        stage ('Push'){
            steps {
                sh 'docker push ndrohith09/spark-jenkins:latest .' 
            }
        }

        stage ('logout'){
            steps {
                sh 'docker logout' 
            }
        }
    }
    // post {
    //     always {
    //         sh 'docker logout'
    //     }
    // }
}

// pipeline {
//   environment {
//     imagename = "ndrohith09/spark"
//     registryCredential = 'ndrohith09'
//     dockerImage = ''
//   }
//   agent any
//   stages {
//     stage('Cloning Git') {
//       steps {
//         git([url: 'https://github.com/ndrohith09/spark-jenkins.git', branch: 'master', credentialsId: 'ndrohith09'])
 
//       }
//     }
//     stage('Building image') {
//       steps{
//         script {
//           dockerImage = docker.build imagename
//         }
//       }
//     }
//     stage('Deploy Image') {
//       steps{
//         script {
//           docker.withRegistry( '', registryCredential ) {
//             dockerImage.push("$BUILD_NUMBER")
//              dockerImage.push('latest')
//           }
//         }
//       }
//     }
//     stage('Remove Unused docker image') {
//       steps{
//         sh "docker rmi $imagename:$BUILD_NUMBER"
//          sh "docker rmi $imagename:latest"
 
//       }
//     }
//   }
// }