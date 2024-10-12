from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_verification_template_response import ListVerificationTemplateResponse
from openapi_server import util


async def list_verification_template(request: web.Request, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_verification_template

    List all the available templates for a given Account.

    :param friendly_name: String filter used to query templates with a given friendly name.
    :type friendly_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
