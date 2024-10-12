from typing import List, Dict
from aiohttp import web

from openapi_server.models.the_root_schema import TheRootSchema
from openapi_server import util


async def auto_complete(request: web.Request, content_type, accept, product_name_contains) -> web.Response:
    """Product Search Autocomplete

    Retrieves product&#39;s information related to the searched string.  &#x60;{{searchString}} is the part of string the user is looking for.  E.g.: &#x60;ref&#x60; | &#x60;refrig&#x60; | &#x60;refrigerator&#x60;

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param product_name_contains: Part of the string that will be searched.
    :type product_name_contains: str

    """
    return web.Response(status=200)
