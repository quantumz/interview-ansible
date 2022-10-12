Interview
==================
We have a simple hello world flask application we want to deploy. There is an existing Ansible playbook that has some mistakes. Our goal is to fix them until the playbook runs without issues.
 
### Notes:
* To get started clone all files into /var/save from https://github.com/perzizzle/interview.git
* The ansible folder contains the main.yml and extra_vars.yml needed for executing the playbook. Running command.sh will execute the playbook.
* Only main.yml needs to be edited, there are no issues with the application.
* The artifact folder contains the application we are going to deploy as a zip file (helloworld.zip).
* We want the application to run out of /opt/helloworld on port 8080
* After deploying the application, we need to restart the helloworld service.
* Once it’s running, we should be able to curl the root of the application and receive “Hello World!”
* You have sudo permissions.
