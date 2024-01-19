pipeline {
    agent any

    environment {
        // Use Jenkins credentials and bind them to environment variables
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-login') // Assuming 'docker-hub-credentials' is the ID of your credentials in Jenkins
        IMAGE_TAG = 'latest' // Change as needed
        REPOSITORY_NAME = 'jhika/login' // Adjust the repository name as needed
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    sh "docker build -t ${REPOSITORY_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withEnv(["DOCKERHUB_USERNAME=${DOCKERHUB_CREDENTIALS_USR}", "DOCKERHUB_PASSWORD=${DOCKERHUB_CREDENTIALS_PSW}"]) {
                        sh "echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin"
                        sh "docker push ${REPOSITORY_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }
    }

    post {
        always {
            sh "docker logout"
        }
    }
}
