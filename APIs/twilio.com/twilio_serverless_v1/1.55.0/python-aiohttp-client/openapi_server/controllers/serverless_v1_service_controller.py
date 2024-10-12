from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.serverless_v1_service import ServerlessV1Service
from openapi_server import util


async def create_service(request: web.Request, friendly_name, unique_name, include_credentials=None, ui_editable=None) -> web.Response:
    """create_service

    Create a new Service resource.

    :param friendly_name: A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
    :type friendly_name: str
    :param unique_name: A user-defined string that uniquely identifies the Service resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the Service resource. This value must be 50 characters or less in length and be unique.
    :type unique_name: str
    :param include_credentials: Whether to inject Account credentials into a function invocation context. The default value is &#x60;true&#x60;.
    :type include_credentials: bool
    :param ui_editable: Whether the Service&#39;s properties and subresources can be edited via the UI. The default value is &#x60;false&#x60;.
    :type ui_editable: bool

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    Delete a Service resource.

    :param sid: The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    Retrieve a specific Service resource.

    :param sid: The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service

    Retrieve a list of all Services.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service(request: web.Request, sid, friendly_name=None, include_credentials=None, ui_editable=None) -> web.Response:
    """update_service

    Update a specific Service resource.

    :param sid: The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
    :type friendly_name: str
    :param include_credentials: Whether to inject Account credentials into a function invocation context.
    :type include_credentials: bool
    :param ui_editable: Whether the Service resource&#39;s properties and subresources can be edited via the UI. The default value is &#x60;false&#x60;.
    :type ui_editable: bool

    """
    return web.Response(status=200)
