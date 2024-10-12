from typing import List, Dict
from aiohttp import web

from openapi_server.models.aquifers_files_list200_response import AquifersFilesList200Response
from openapi_server.models.person_list import PersonList
from openapi_server.models.person_name import PersonName
from openapi_server import util


async def drillers_files_list(request: web.Request, person_guid) -> web.Response:
    """drillers_files_list

    list files found for the aquifer identified in the uri

    :param person_guid: 
    :type person_guid: str

    """
    return web.Response(status=200)


async def drillers_list(request: web.Request, search=None, ordering=None, limit=None, offset=None) -> web.Response:
    """drillers_list

    Returns a list of all person records

    :param search: A search term.
    :type search: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def drillers_names_list(request: web.Request, search=None) -> web.Response:
    """drillers_names_list

    Search for a person in the Register

    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)
