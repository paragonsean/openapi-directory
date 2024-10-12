from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.delete_user_request import DeleteUserRequest
from openapi_server.models.link_request import LinkRequest
from openapi_server.models.upsert_user201_response import UpsertUser201Response
from openapi_server.models.upsert_user_request import UpsertUserRequest
from openapi_server import util


async def delete_user(request: web.Request, body) -> web.Response:
    """Delete user

    Endpoint to delete a user.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteUserRequest.from_dict(body)
    return web.Response(status=200)


async def link(request: web.Request, body) -> web.Response:
    """Link web activity to user

    💡 You don&#39;t need to use this endpoint if you use our JavaScript snippet in your application.  This endpoint is used to link web activity to a user in your application. This will help you discover which channels and campaigns work best.  When our JavaScript snippet is embedded on your website, blog or landing pages, a cookie named \&quot;__journey\&quot; will be set.  This will only work if your website and application are under the same top level domain.  Website, blog or landing pages * www.my-domain.tld * blog.my-domain.tld * landing-page.my-domain.tld  Application * app.my-domain.tld  The cookie on my-domain.tld will also be send to your app domain.  You should call this endpoint after the user succesfully logged in (so that you know the user&#39;s ID). Use the value of the cookie as device ID.

    :param body: 
    :type body: dict | bytes

    """
    body = LinkRequest.from_dict(body)
    return web.Response(status=200)


async def upsert_user(request: web.Request, body) -> web.Response:
    """Create or update user

    Endpoint to create or update a user.

    :param body: 
    :type body: dict | bytes

    """
    body = UpsertUserRequest.from_dict(body)
    return web.Response(status=200)
