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
