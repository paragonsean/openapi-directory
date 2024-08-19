from typing import List, Dict
from aiohttp import web

from openapi_server.models.containers_messages_get200_response import ContainersMessagesGet200Response
from openapi_server.models.containers_version_get_info import ContainersVersionGetInfo
from openapi_server import util


async def containers_messages_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """List messages for the user

    This endpoint retrieves all IBM Containers system messages for the user.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. To retrieve your space ID, run &#x60;cf space &lt;space_name&gt; --guid&#x60; and replace &#x60;&lt;space_name&gt;&#x60; with the name of the space where you want to create or work with your container. 
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def containers_version_get(request: web.Request, ) -> web.Response:
    """List latest API version

    This endpoint retrieves a list of all microservices that are used in the IBM Containers service with their current build version. This method does not require authentication.


    """
    return web.Response(status=200)
