pipeline{
  agent any
  stages{
    stage("GitHub checkout....") {
      steps {
        script {
          git branch: 'main', url: 'https://github.com/osagiefe/my-python-flask-docker-app.git'
       }
      }
    }
    stage("Build docker connecting....."){

      steps{
        sh 'printenv'
        sh 'git version'
        sh 'docker build . -t osagiefe/f-app1.1'
      }
    
    }

    stage("push image to DockerHub"){
      steps{
        script {
          withCredentials([string(credentialsId: 'DOCKERID', variable: 'DOCKERID')]) {
            sh 'docker login -u osagiefe -p ${DOCKERID}'
          }
            sh 'docker push osagiefe/f-app1.1:latest'
        }
      }
    }
    stage('Deploying python app to Kubernetes') {
      steps {
        script {
          dir('kubernetes') {
            sh ('aws eks update-kubeconfig --name eks-cluster-204 --region us-east-1')
            sh 'kubectl config current-context'
            // sh "kubectl get ns"
            sh "kubectl apply -f deployment.yaml"
            sh "kubectl apply -f service.yaml"
          }
        }
      }
    }
  }  
}

	
    