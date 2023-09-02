pipeline {
    agent any
    // options {
        // skipStagesAfterUnstable()
    // }
    stages {
        stage('Build') {
            steps {
                echo 'Installing dependancies'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Unit tests..'
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
                echo "Completed ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}
