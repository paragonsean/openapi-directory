from typing import List, Dict
from aiohttp import web

from openapi_server.models.company import Company
from openapi_server.models.company_dropdown_list import CompanyDropdownList
from openapi_server.models.company_list import CompanyList
from openapi_server.models.new_company import NewCompany
from openapi_server.models.update_company import UpdateCompany
from openapi_server import util


async def company_get(request: web.Request, updated_after=None, page_size=None, page_number=None, sort=None) -> web.Response:
    """Gets list of Companies

    

    :param updated_after: 
    :type updated_after: str
    :param page_size: Number of results per page
    :type page_size: int
    :param page_number: 1 based page number to retrieve
    :type page_number: int
    :param sort: (optional) Supply one of: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;CompanyName\&quot;,\&quot;DateUpdated desc\&quot;,\&quot;DateCreated desc\&quot;, \&quot;CompanyName desc\&quot;
    :type sort: str

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def company_get_by_id(request: web.Request, id) -> web.Response:
    """Gets Company by Company ID

    

    :param id: Company ID Number
    :type id: int

    """
    return web.Response(status=200)


async def company_lookup(request: web.Request, page_size=None, page_number=None, search=None) -> web.Response:
    """Gets minimal list of Companies.

    Certain roles see a restricted set of companies based on their project memberships

    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param search: Search string to match against Company title
    :type search: str

    """
    return web.Response(status=200)


async def company_post(request: web.Request, model) -> web.Response:
    """Create a Company

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewCompany.from_dict(model)
    return web.Response(status=200)


async def company_put(request: web.Request, model) -> web.Response:
    """Update a Company record.

    Requires CompanyID and a list of field names to update. The FieldsToUpdate field accepts a string array containing field names that should be updated.

    :param model: 
    :type model: dict | bytes

    """
    model = UpdateCompany.from_dict(model)
    return web.Response(status=200)
