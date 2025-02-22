pipeline {
    agent {
        label 'test-agent'
    }

    environment {
        IMAGE_NAME = 'ghcr.io/sdpx-2024/jenkins-exam'
        REGISTRY_CREDENTIALS = credentials('ghcr-pat')
        APP_NAME = 'prime-api'
        ROBOT_REPO = 'https://github.com/SDPX-2024/jenkins-exam-robot.git'
        ROBOT_BRANCH = 'main'
    }

    stages {
        stage("Install & Run Unit Tests") {
            steps {
                sh "pip install -r requirements.txt"
                sh "python3 unit_test.py -v &> /home/test/exam/unit_results/unit_test.log"
            }
        }

        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_ID} ."
            }
        }

        stage('Run Container & Run Robot Testing') {
            steps {
                sh "docker run -dp 5000:5000 --name ${APP_NAME} ${IMAGE_NAME}:${BUILD_ID}"
                git branch: "${ROBOT_BRANCH}", url: "${ROBOT_REPO}"
                sh "python3 -m robot --outputdir /home/test/exam/robot_results/ plus.robot "
            }

            post {
                always {
                    sh returnStatus: true, script: "docker stop ${APP_NAME}"
                    sh returnStatus: true, script: "docker rm ${APP_NAME}"
                }
            }
        }

        stage('Push Image to Registry') {
            steps {
                sh 'echo $REGISTRY_CREDENTIALS_PSW  | docker login ghcr.io -u $REGISTRY_CREDENTIALS_USR --password-stdin'
                sh "docker tag ${IMAGE_NAME}:${BUILD_ID} ${IMAGE_NAME}:latest"
                sh "docker push ${IMAGE_NAME}:${BUILD_ID}"
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy') {
            agent {
                label 'uat-agent'
            }
            steps {
                sh returnStatus: true, script: "docker stop ${APP_NAME}"
                sh returnStatus: true, script: "docker rm ${APP_NAME}"
                sh 'echo $REGISTRY_CREDENTIALS_PSW  | docker login ghcr.io -u $REGISTRY_CREDENTIALS_USR --password-stdin'
                sh "docker pull ${IMAGE_NAME}:latest"
                sh "docker run -dp 5000:5000 --name ${APP_NAME} ${IMAGE_NAME}:latest"
                sh returnStatus: true, script: "docker images -q -f \"dangling=true\" | xargs -r docker rmi"
            }
        }
    }

    post {
        always {
            sh "docker system prune -af"
        }
    }
}