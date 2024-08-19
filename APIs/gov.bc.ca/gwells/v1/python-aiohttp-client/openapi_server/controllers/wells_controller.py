from typing import List, Dict
from aiohttp import web

from openapi_server.models.aquifers_files_list200_response import AquifersFilesList200Response
from openapi_server.models.well_detail import WellDetail
from openapi_server.models.well_tag_search import WellTagSearch
from openapi_server.models.wells_list200_response import WellsList200Response
from openapi_server import util


async def wells_files_list(request: web.Request, tag) -> web.Response:
    """wells_files_list

    list files found for the well identified in the uri

    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)


async def wells_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """wells_list

    returns a list of wells

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def wells_read(request: web.Request, well_tag_number) -> web.Response:
    """wells_read

    Return well detail. This view is open to all, and has no permissions.

    :param well_tag_number: A unique integer value identifying this well.
    :type well_tag_number: int

    """
    return web.Response(status=200)


async def wells_tags_list(request: web.Request, search=None, ordering=None) -> web.Response:
    """wells_tags_list

    seach for wells by tag or owner

    :param search: A search term.
    :type search: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str

    """
    return web.Response(status=200)
