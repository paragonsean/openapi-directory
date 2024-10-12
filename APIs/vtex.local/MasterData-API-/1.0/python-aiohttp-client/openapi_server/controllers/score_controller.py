from typing import List, Dict
from aiohttp import web

from openapi_server.models.deletescorebyfield_request import DeletescorebyfieldRequest
from openapi_server.models.putscorebyfield_request import PutscorebyfieldRequest
from openapi_server.models.putscores_request import PutscoresRequest
from openapi_server import util


async def deletescorebyfield(request: web.Request, accept, acronym, id, field_name, body) -> web.Response:
    """Delete score by field

    Allows you to remove a key from a specific field.

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param field_name: Name of the field to remove score from
    :type field_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeletescorebyfieldRequest.from_dict(body)
    return web.Response(status=200)


async def putscorebyfield(request: web.Request, accept, acronym, id, field_name, body) -> web.Response:
    """Put score by field

    It allows to punctuate in a specific field.

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param field_name: Name of the field to score
    :type field_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutscorebyfieldRequest.from_dict(body)
    return web.Response(status=200)


async def putscores(request: web.Request, accept, acronym, id, body) -> web.Response:
    """Put scores

    It allows punctuate in more than one field and more than one key.

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PutscoresRequest.from_dict(d) for d in body]
    return web.Response(status=200)
