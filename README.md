# IP details FastAPI

This API provides an information on any IP (IPv4 or IPv6). 

## Documentation

### Tech Stack
- FastAPI
- Docker
  
In order to start the application you can do it in two ways

### Docker
- Create a docker container by running the command go the project root directory
    >docker build --no-cache -t <image_name> .
- Run the docker container by running the command
    >docker run -d --name <container_name> -p 80:80 <image_name>
- Now you should be able to access the API at localhost 
    >http://127.0.0.1:80/ip/<ipv4_or_ipv6>

### Start local server
- Create a Virtual environment for Python and install the dependencies from requirements.txt
    >pip3 install -r requirements.txt
- You can start the local server by running the command
    >uvicorn main:app --reload
- Now you should be able to access the API at localhost 
    >http://127.0.0.1:80/ip/<ipv4_or_ipv6>

