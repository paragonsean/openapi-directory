from typing import List, Dict
from aiohttp import web

from openapi_server.models.getdataentityfields import Getdataentityfields
from openapi_server.models.listdataentity import Listdataentity
from openapi_server import util


async def getdataentitystructure(request: web.Request, content_type, accept, acronym) -> web.Response:
    """Get data entity structure

    Returns the data entity structure with its respective fields and data type.    ### Response status code    1. Status Code &#x60;403&#x60;: Access not allowed  2. Status Code &#x60;200&#x60;: Retrieves data entity structure    &gt; All headers listed below are required.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Identifies the kind of data
    :type acronym: str

    """
    return web.Response(status=200)


async def listdataentities(request: web.Request, content_type, accept) -> web.Response:
    """List data entities

    Retrieves the list of existing data entities in the store.    ### Response status code    1. Status Code &#x60;403&#x60;: Access not allowed  2. Status Code &#x60;200&#x60;: Retrieves data entity list    &gt; All headers listed below are required.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str

    """
    return web.Response(status=200)
