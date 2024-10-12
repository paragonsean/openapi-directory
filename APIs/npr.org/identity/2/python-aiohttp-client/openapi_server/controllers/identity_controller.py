from typing import List, Dict
from aiohttp import web

from openapi_server.models.affiliation import Affiliation
from openapi_server.models.error_document import ErrorDocument
from openapi_server.models.user_document import UserDocument
from openapi_server import util


async def delete_user(request: web.Request, authorization) -> web.Response:
    """Delete the user&#39;s account

    Use with caution as some steps are irreverisble. Initiates the user account deletion process, including removal of all user PII and account access.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, authorization) -> web.Response:
    """Get the latest state information about the logged-in user

    After a successful login, the client should send a &#x60;GET&#x60; call approximately once an hour to refresh the user data.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str

    """
    return web.Response(status=200)


async def inherit_from_temp_user(request: web.Request, authorization, temp_user) -> web.Response:
    """Copy listening data from a temporary user account to the logged-in user&#39;s account

    This can and should only be used by clients who have access to the &#x60;temporary_user&#x60; grant type.     Third-party developers do not have access to this grant type by default, and will not need this endpoint.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param temp_user: The temporary user&#39;s ID before the user registered or logged in
    :type temp_user: int

    """
    return web.Response(status=200)


async def post_following(request: web.Request, authorization, body) -> web.Response:
    """Update the following status of the logged-in user for a particular aggregation

    After a successful call, this returns a User document with an updated list of affiliations.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param body: A JSON-serialized object which contains data about a user affiliation such as the aggregation ID, affiliation rating, aggregation URL, days since last listen, and following status.
    :type body: dict | bytes

    """
    body = Affiliation.from_dict(body)
    return web.Response(status=200)


async def update_stations(request: web.Request, authorization, body=None) -> web.Response:
    """Update the logged-in user&#39;s favorite station(s)

    Right now, only the primary station can be changed. Previously selected stations will not be deleted, but the new station will be moved to first in the array.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param body: A JSON-serialized array of station IDs
    :type body: List[int]

    """
    return web.Response(status=200)
