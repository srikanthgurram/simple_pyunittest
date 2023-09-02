pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        TEST_USER_NAME = credentials('TEST_USER_NAME')
        TEST_USER_PASSWORD = credentials('TEST_USER_PASSWORD')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Installing dependancies'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            environment {
                MAX_TIMEOUT = 120
                RERUN_COUNT = 2
            }
            steps {
                bat 'echo Running Unit tests with global variables %TEST_USER_NAME% and %TEST_USER_PASSWORD%'
                echo "Tests set for maximum timeout of ${MAX_TIMEOUT} seconds and re-run on failure for ${RERUN_COUNT} times"
                bat 'python -m pytest --junit-xml=pytest_unit.xml unit_tests.py'
            }
        }
        stage('Deploy') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Deploying..'
                echo "Completed Build ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
    post {
        always {
            junit '*.xml'
        }
        failure {
            emailext body: 'Test Message',
            subject: 'Jenkins Build failure', 
            to: '2gurram@gmail.com'
        }
    }
}
