from graphdatascience import GraphDataScience
from neontology import init_neontology
from fastapi import APIRouter, Depends
from dependencies import get_token_header
from config import settings
import time

router = APIRouter(
    tags=["Admin"],
    responses={404: {"description": "Not found"}},
)


# Neo4j database connection
@router.on_event("startup")
async def startup_event():
    init_neontology(
        init_neontology(
            neo4j_uri=settings.NEO4J_URI,
            neo4j_username=settings.NEO4J_USERNAME,
            neo4j_password=settings.NEO4J_PASSWORD,
        )
    )


@router.get("/info")
def info():
    return {
        "app_name": settings.app_name,
    }


@router.get("/neo4j")
async def check_DB():
    result_queue = await test_DB()
    return {"message": (
        "La connexion a réussi !" if result_queue else "La connexion a échoué, vérifiez que votre base de donnée neo4j est bien lancé au préalable.")}


async def test_DB():
    connection_try = 5
    host = settings.NEO4J_URI
    user = settings.NEO4J_USERNAME
    password = settings.NEO4J_PASSWORD

    start_time = time.time()

    while time.time() - start_time < connection_try:
        try:
            gds = GraphDataScience(host, auth=(user, password))
            print(f"Connexion établie, version de la librairie graphdatascience : {gds.version()}")
            return  True
        except Exception as e:
            print(f"Erreur de connexion : {e}")
            time.sleep(1)  # Pause de 1 seconde entre chaque tentative
    return False


@router.get("/up")
def is_up():
    return {"message": "the server is up"}
