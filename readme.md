
# API

## Install

### Venv creation

>  python3 -m venv ./.venv/

### Venv activation

#### Windows

> TODO

#### Linux

> chmod +x .venv/bin/activate

> .venv/bin/activate

### Libraries instalation

> pip install -r requirement.txt

## APP Launch

> uvicorn app.main:app --reload

The API should be accecible at this address+

>  http://127.0.0.1:8000

## .env format

``` shell
APP_NAME="IASearchAPI"
APP_DESC="API built for IA enhanced research on Neo4j with FastAPI"
APP_VERSION="0.1"
DOCS_URL="/docs"
REDOC_URL="/redoc"
NEO4J_URI="DB URL"
NEO4J_USERNAME="DB Username"
NEO4J_PASSWORD="DB password"
APP_PASSWORD="secure_this"
SECRET_KEY="secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=10800
```
# Docker

## Docker Creation

```shell
docker build -t fast_ai_search . 
```

Note that if you use docker for the API you must run a docker for neo4j as well.

You will have to change the NEO4J_URI replacing localhost by the result of this command:
```shell
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <neo4j-container name>
```

## Run
```shell
docker run -d --name ai_search_container -p 9000:80 fast_ai_search
```

## Dockered API URL

> http://locahost:9000



## Connect inside the Docker :

```shell
docker exec -it ai_search_container /bin/bash 
```

## Neo4J

```shell
docker run -d --name neo4j-container -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password -v neo4j_data:/home/villerot/Documents/GitHub/AI_Search_Neao4J_Docker_file/ neo4j:latest 
```
