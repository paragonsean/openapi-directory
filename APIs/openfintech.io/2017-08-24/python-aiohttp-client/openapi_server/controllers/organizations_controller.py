from typing import List, Dict
from aiohttp import web

from openapi_server.models.organization_response import OrganizationResponse
from openapi_server.models.organizations_response import OrganizationsResponse
from openapi_server import util


async def organizations_get(request: web.Request, page_number=None, page_size=None, filter_search=None, filter_name=None, filter_code=None, filter_status=None, filter_industries=None, sort=None) -> web.Response:
    """List of organizations

    This endpoint retrievs the list of organizations present in the system. The data displays general, public information, without reference to the type of activity (for example - name, address, contacts, etc.). 

    :param page_number: Current page number.
    :type page_number: int
    :param page_size: Page size.&lt;br&gt;*Default value: 100* 
    :type page_size: int
    :param filter_search: Full text search with id, name, code.
    :type filter_search: str
    :param filter_name: Filtering by name.
    :type filter_name: str
    :param filter_code: Filtering by code.
    :type filter_code: str
    :param filter_status: Filtration by status.
    :type filter_status: List[str]
    :param filter_industries: Filtering by industries.
    :type filter_industries: str
    :param sort: Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | description | -description | 
    :type sort: List[str]

    """
    return web.Response(status=200)


async def organizations_id_get(request: web.Request, id) -> web.Response:
    """Organization by ID

    Returns organization with specific ID. 

    :param id: Unique ID.
    :type id: str

    """
    return web.Response(status=200)
