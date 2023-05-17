pipeline {
    agent any
parameters {
    
 
        choice(name: 'BRANCH', choices: ['main', 'dev'], description: 'Choose branch')
 
    
    }
    stages {

        stage ("Code pull"){
            steps{
                checkout scm
                echo "${WORKSPACE}"
               
                echo "${BUILD_URL}"
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
