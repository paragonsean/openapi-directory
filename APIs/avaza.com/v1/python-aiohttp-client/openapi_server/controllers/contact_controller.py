from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_contact import CompanyContact
from openapi_server.models.contact_list import ContactList
from openapi_server.models.new_company_contact import NewCompanyContact
from openapi_server import util


async def contact_get(request: web.Request, updated_after=None, page_size=None, page_number=None, sort=None, company_idfk=None) -> web.Response:
    """Gets list of Contacts

    

    :param updated_after: 
    :type updated_after: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param sort: 
    :type sort: str
    :param company_idfk: 
    :type company_idfk: int

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def contact_get_by_id(request: web.Request, id) -> web.Response:
    """Gets Contact by Contact ID

    

    :param id: Contact ID number
    :type id: int

    """
    return web.Response(status=200)


async def contact_post(request: web.Request, model) -> web.Response:
    """Create a Contact

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewCompanyContact.from_dict(model)
    return web.Response(status=200)
