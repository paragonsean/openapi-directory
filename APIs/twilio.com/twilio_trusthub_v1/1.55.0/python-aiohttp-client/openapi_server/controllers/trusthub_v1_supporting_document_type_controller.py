from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_supporting_document_type_response import ListSupportingDocumentTypeResponse
from openapi_server.models.trusthub_v1_supporting_document_type import TrusthubV1SupportingDocumentType
from openapi_server import util


async def fetch_supporting_document_type(request: web.Request, sid) -> web.Response:
    """fetch_supporting_document_type

    Fetch a specific Supporting Document Type Instance.

    :param sid: The unique string that identifies the Supporting Document Type resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_supporting_document_type(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_supporting_document_type

    Retrieve a list of all Supporting Document Types.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
