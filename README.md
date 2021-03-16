**Demo of Creating Dockerize python flask app and pushing docker image to AWS ECS
**
First setup your environment

**Prequites**

Here I have used aws ec2-instance

**Install dependies as below
**
yum -y install git

yum -y install docker

 curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip

sudo ./aws/install

**Create an IAM user and download the access and secret keys
**

mkdir Flaskapp

cd flaskapp

git clone https://github.com/manjulive89/Flaskapp.git

docker build -t flask-blog .

docker images

**Creating Container registry in AWS
**

aws configure

Press Enter

Paste the accesskey of iam user "enter"

Paste the secret key of iam user "enter"

enter default region: us-west-2 "enter"

Enter"

**** create an container registry
****

aws ecr create-repository --repository-name ecs-flask-blog


docker tag flask-blog 136200979863.dkr.ecr.us-west-2.amazonaws.com/ecs-flask-blog


docker push 136200979863.dkr.ecr.us-west-2.amazonaws.com/ecs-flask-blog



Finall you can verify that Container repository is created in AWS and docker image is pushed to Container registry

