pipeline{
      agent any
      
      stages{
            stage('git checkout'){
                  steps{
                        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], 
                        userRemoteConfigs: [[url: 'https://github.com/yaw4testing/python-lambda.git']]])
                  }
            }
            stage('check python and pip version'){
                  steps{
                        sh 'python3 --version'
                        sh 'pip --version'
                  
                  }
            }
            stage('build artifacts'){
                  steps{
                        sh 'python3 -m pip install folium'
                        sh 'python3 -m pip install pandas'
                  }
            }
            stage('testing the app'){
                  steps{
                        sh 'python3 ma.py'
                  }
            }
      }






}
