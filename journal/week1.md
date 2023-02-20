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
 