Hello Everyone,
We are ready to go now..!!

# Deploying_Python_Application using Docker container Platform...!!
This is sample python application where we build it through docker file and deploy it on container.

## PRE-REQUISITE

1) Amazon EC2 Instance:

   AMI - Ubuntu or ( you can take any as per your wish )
   InstanceType - t2.micro ( Free-Tier )
   Key - Recommonded
   SecurityGroup - we can use default security group where all the traffic are allowed or as per your requirement if any specific port 
                   are required.
   EBS - 8 GB

   #...We have created EC2 instance with above specification and connect it through SSH...#

2) ### Now we update the machine with below command:
   Sudo apt update
   
4) ### Once we are done with the update we make one directory:
   /python_app and inside that we clone our git repository --> @Deploying_Python_Application

   mkdir python_app
   
   cd python_app
   
   git clone <repository_URL>

5) ### Now we make one app.py file and requirements.txt file for sample Python program that uses Flask to create a web application. We'll also create a Dockerfile to containerize this application:

   sudo nano app.py 
   
   sudo nano requirements.txt
   
   sudo nano Dockerfile
   
6) ### Now, let's build the image and run the Docker container using below commands:

   ### Build the Docker image:

      docker build -t python-app .

   ### Run the Docker container and expose port 5000:
   
      docker run -itd -p 5000:5000 python-app
      
7) ### Now we can check our python-app image and container with below commands:

   docker images

   docker ps -a

   access it on browser through --> public ip of instance:5000

9) ### Now, the Flask web application is running inside a Docker container, and we can access it by visiting the specified host and port. In this case, it's http://localhost:5000. Adjust the URL accordingly if you are running Docker on a remote server or in a different environment.
      

![image](https://github.com/Kunal-Pere/Deploying_Python_Application-/assets/157100045/082cc90a-8e1b-4db8-880f-0b5acee27d4f)

