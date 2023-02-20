# Week 1 — App Containerization

Created Docker file as per livestream
Attached shell to running docker environment and noted no ENV variables for the Front and Back URL just like livestream 
Updated Python version on gitpod to 3.10.9 and updated pip to latest version
Proper command to set Front and Back URL is :  docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
Installed npm on FrontEnd (npm i commmand)

Modified the Docker Compose file to add Posgres and Dynamodb (local copy)
Created a sample dynamo db based off  https://github.com/100DaysOfCloud/challenge-dynamodb-local
Created a Music table, inserted a record
Scanned dynamo db using command " aws dynamodb scan --table-name Music --query "Items" --endpoint-url http://localhost:8000"
Able to see the record I added to local db

Added Notification backend api and front end react pages and modified routes
Made a typo on app router, had to restart docker container for front end - possibly cachced routes (Once rebooted UI worked)

Homework: Added Docker-Compose health check for backend and frontend
          Created bacth script for Docker command
          Pushed backend container to DockerHub account https://hub.docker.com/r/gundam073/backend-flask