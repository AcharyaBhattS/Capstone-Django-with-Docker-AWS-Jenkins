# Capstone Project on Django with Docker, AWS EC2 and Jenkins
### Capstone Project on Django+Docker+AWS+Jenkins

### Project Steps overview:
 - [x] Create EC2
 - [x] Install Docker in EC2
 - [x] Install Jenkins in EC2
 - [x] Link GitHub with Jenkind (put the Repo link in Jenkins)
 - [x] Clone the project
 - [x] Run the docker container in docker desktop installed in EC2 through Jenkins
<br><br>

### Steps in Details:
1.
To install Docker
sudo snap install docker

To install docker-compose:
sudo apt install docker-compose

2. Clone the Project to EC2 from GitHub

3. sudo docker-compose up --build    # This command will build & up Dockerfile, docker-compose.yml & docker-compose.override.yml

4.. docker images

5. docker compose ps  # list of all docker containers

Ctrl+q to stop execution

6. Check docker image is running in EC2 or not

     sudo docker run -p 8000:80 fmm-website-backend-develop_djangoapp
     sudo docker run fmm-website-backend-develop_djangoapp
