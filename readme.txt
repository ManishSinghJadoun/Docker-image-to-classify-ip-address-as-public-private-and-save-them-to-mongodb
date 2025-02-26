1.Create three files one python fide that will contain the main code with the name ip_processor. 
2.Then create a docker file that contains the folder information, package information that are required to for our docker file.
3.A docker-compose.yml file defines services, networks, and volumes for multi-container Docker applications. It is a kind of dictionary file



4.Navigate to folder and these file should be in same folder then run.
docker-compose up --build

5.Tag your file and push it to docker hub.

docker tag ipprocessor-ip_processor:latest manishsinghjadoun/ipprocessor-ip_processor:latest
docker push manishsinghjadoun/ipprocessor-ip_processor:latest

6.Pull and run the file.

for linux
docker pull manishsinghjadoun/ipprocessor-ip_processor:latest
docker run -v $(pwd)/logs:/app/logs manishsinghjadoun/ipprocessor-ip_processor:latest


for cmd
docker run -v C:\Users\jadon\logs:/app/logs manishsinghjadoun/ipprocessor-ip_processor:latest

for powershell
docker run -v ${PWD}/logs:/app/logs manishsinghjadoun/ipprocessor-ip_processor:latest
