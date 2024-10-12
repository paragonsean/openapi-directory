from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def validate_documentby_clusters(request: web.Request, accept, acronym, id, body) -> web.Response:
    """Validate Document by Clusters

    

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param body: 
    :type body: List[]

    """
    return web.Response(status=200)
