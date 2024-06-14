Hello Everyone,
We are ready to go now..!!

# Deploying_Python_Application using Docker container Platform...!!
This is sample python application where we build it through docker file and deploy it on container.

!!!...PRE-REQUISITE...!!!

1) Amazon EC2 Instance:

   AMI - Ubuntu or ( you can take any as per your wish )
   InstanceType - T2.Micro ( Free-Tier )
   Key - Recommonded
   SecurityGroup - we can use default security group where all the traffic are allowed or as per your requirement if any specific port 
                   are present.
   EBS - 8 GB

### We have created EC2 instance with above specification and connect it through SSH

2) ### Now we update the machine with below command.
   Sudo apt update
3) ### Once we are done with update we make one directory
   /python_app and inside that we clone our git repository --> @Deploying_Python_Application

   #### mkdir python_app
   #### cd python_app
   #### git clone<repository url>

4) ### now we make one app.py file and requirements.txt file for simple Python program that uses Flask to create a web application. We'll also create a Dockerfile to containerize this application.

   sudo nano app.py
   sudo nano requirements.txt
   sudo nano Dockerfile
   


   


