from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_a_database200_response import QueryADatabase200Response
from openapi_server.models.query_a_database_request import QueryADatabaseRequest
from openapi_server.models.retrieve_a_database200_response import RetrieveADatabase200Response
from openapi_server.models.update_a_database200_response import UpdateADatabase200Response
from openapi_server.models.update_a_database_request import UpdateADatabaseRequest
from openapi_server import util


async def query_a_database(request: web.Request, id, notion_version=None, body=None) -> web.Response:
    """Query a database

    Query a database

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = QueryADatabaseRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_a_database(request: web.Request, id, notion_version=None) -> web.Response:
    """Retrieve a database

    Retrieves a database object using the ID specified in the request path. 

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str

    """
    return web.Response(status=200)


async def update_a_database(request: web.Request, id, notion_version=None, body=None) -> web.Response:
    """Update a database

    Update a database

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateADatabaseRequest.from_dict(body)
    return web.Response(status=200)
