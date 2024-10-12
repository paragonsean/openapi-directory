from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server import util


async def get_template_model(request: web.Request, dto_data_type, authorization, api_version) -> web.Response:
    """Get the object template

    Returns a template instance of the specified data type

    :param dto_data_type: The data transfer object type name. E.g PensionPayInstruction
    :type dto_data_type: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_templates(request: web.Request, authorization, api_version) -> web.Response:
    """Get a list of all available data object tempaltes

    Returns a collection of links to all the available data object templates

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
