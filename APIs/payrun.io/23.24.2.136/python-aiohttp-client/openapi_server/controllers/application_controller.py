from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_secret import ApplicationSecret
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server import util


async def delete_application_secret(request: web.Request, secret_id, authorization, api_version) -> web.Response:
    """Deletes Application secret

    Deletes an Application secret from the given resource location

    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_application_secret(request: web.Request, secret_id, authorization, api_version) -> web.Response:
    """Get Application secret

    Get the public visible Application secret object

    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_application_secrets(request: web.Request, authorization, api_version) -> web.Response:
    """Get all Application secret links

    Get all the Application secret links

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_application_secret(request: web.Request, authorization, api_version) -> web.Response:
    """Create a new Application secret

    Create new Application secret using auto generated resource location key

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_application_secret(request: web.Request, secret_id, authorization, api_version) -> web.Response:
    """Create a new Application secret

    Create / update an Application secret at the given resource location

    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
