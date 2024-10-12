from typing import List, Dict
from aiohttp import web

from openapi_server.models.retrieve_a_page200_response import RetrieveAPage200Response
from openapi_server.models.retrieve_a_page_property_item200_response import RetrieveAPagePropertyItem200Response
from openapi_server.models.update_page_properties200_response import UpdatePageProperties200Response
from openapi_server.models.update_page_properties_request import UpdatePagePropertiesRequest
from openapi_server import util


async def retrieve_a_page(request: web.Request, id, notion_version=None, =None) -> web.Response:
    """Retrieve a Page

    Retrieves a Page object using the ID in the request path. This endpoint exposes page properties, not page content. 

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str
    :param : 
    :type : str

    """
    return web.Response(status=200)


async def retrieve_a_page_property_item(request: web.Request, page_id, property_id) -> web.Response:
    """Retrieve a Page Property Item

    Retrieve a Page Property Item

    :param page_id: 
    :type page_id: str
    :param property_id: 
    :type property_id: str

    """
    return web.Response(status=200)


async def update_page_properties(request: web.Request, id, notion_version=None, body=None) -> web.Response:
    """Update Page properties 

    Updates a page by setting the values of any properties specified in the JSON body of the request. Properties not updated via parameters will remain unchanged. 

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePagePropertiesRequest.from_dict(body)
    return web.Response(status=200)
