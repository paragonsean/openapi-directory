from typing import List, Dict
from aiohttp import web

from openapi_server.models.source_input import SourceInput
from openapi_server.models.sourceresponse import Sourceresponse
from openapi_server.models.sources import Sources
from openapi_server import util


async def create_source(request: web.Request, vestorly_auth, source, access_token=None) -> web.Response:
    """create_source

    Create source

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param source: Source
    :type source: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    source = SourceInput.from_dict(source)
    return web.Response(status=200)


async def find_sources(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_sources

    Returns all sources

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def get_source_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """get_source_by_id

    Get Source By ID

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: ID of source to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def update_source_by_id(request: web.Request, vestorly_auth, id, source, access_token=None) -> web.Response:
    """update_source_by_id

    Update Source By ID

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: ID of source to fetch
    :type id: str
    :param source: Source
    :type source: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    source = SourceInput.from_dict(source)
    return web.Response(status=200)
