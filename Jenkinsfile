pipeline {
    agent any

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }

        stage('Build environment') {
            steps {
                echo "Building virtualenv"
                sh  '''
                      pip3 install -r requirements.txt
                    '''
            }
        }

      
        }
    }
