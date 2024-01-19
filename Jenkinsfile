pipeline {
    agent any

    environment {
        // Define environment variables
        DOCKERHUB_USERNAME = 'Jhika'
        DOCKERHUB_PASSWORD = 'Hika 32146'
        IMAGE_TAG = 'Jhika/front-app' // Change as needed
        REPOSITORY_NAME = 'jhika/login'
         DOCKERFILE_NAME = 'frontdockerfile'
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out source code from GitHub
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t jhika/login:jhika/front-app .')
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub
                    sh "docker login -u ${DOCKERHUB_USERNAME} -p ${DOCKERHUB_PASSWORD}"
                    // Push the image
                    docker.push("${DOCKERHUB_USERNAME}/${REPOSITORY_NAME}:${IMAGE_TAG}")
                }
            }
        }
    }

    post {
        always {
            // Logout from Docker Hub to secure the credentials
            sh "docker logout"
        }
    }
}