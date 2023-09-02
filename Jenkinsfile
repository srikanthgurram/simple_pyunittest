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
            steps {
                echo "Running Unit tests with global variables ${env.TEST_USER_NAME} and ${env.TEST_USER_PASSWORD}"
                bat 'python -m pytest --junit-xml=pytest_unit.xml unit_tests.py'
                junit 'pytest_unit.xml'
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
}
