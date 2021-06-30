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
      }






}
