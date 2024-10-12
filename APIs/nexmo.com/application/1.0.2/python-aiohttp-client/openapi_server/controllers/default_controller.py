from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_created import ApplicationCreated
from openapi_server.models.applications import Applications
from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.update_application_request import UpdateApplicationRequest
from openapi_server import util


async def create_application(request: web.Request, body=None) -> web.Response:
    """Create Application

    You use a &#x60;POST&#x60; request to create a new application.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application(request: web.Request, app_id) -> web.Response:
    """Destroy Application

    You use a &#x60;DELETE&#x60; request to delete a single application.

    :param app_id: The ID allocated to your application by Nexmo.
    :type app_id: str

    """
    return web.Response(status=200)


async def retrieve_application(request: web.Request, api_key, api_secret, app_id) -> web.Response:
    """Retrieve Application

    You use a &#x60;GET&#x60; request to retrieve details about a single application.

    :param api_key: You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview)
    :type api_key: str
    :param api_secret: You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview)
    :type api_secret: str
    :param app_id: The ID allocated to your application by Nexmo.
    :type app_id: str

    """
    return web.Response(status=200)


async def retrieve_applications(request: web.Request, api_key, api_secret, page_size=None, page_index=None) -> web.Response:
    """Retrieve all Applications

    You use a &#x60;GET&#x60; request to retrieve details of all applications associated with your account.

    :param api_key: You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview)
    :type api_key: str
    :param api_secret: You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview)
    :type api_secret: str
    :param page_size: Set the number of items returned on each call to this endpoint. The default is 10 records.
    :type page_size: int
    :param page_index: Set the offset from the first page. The default value is &#x60;0&#x60;.
    :type page_index: int

    """
    return web.Response(status=200)


async def update_application(request: web.Request, app_id, body=None) -> web.Response:
    """Update Application

    You use a &#x60;PUT&#x60; request to update an existing application.

    :param app_id: The ID allocated to your application by Nexmo.
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateApplicationRequest.from_dict(body)
    return web.Response(status=200)
