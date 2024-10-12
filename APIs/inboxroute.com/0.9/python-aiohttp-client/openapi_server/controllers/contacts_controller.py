from typing import List, Dict
from aiohttp import web

from openapi_server.models.contact_page import ContactPage
from openapi_server.models.contact_update import ContactUpdate
from openapi_server.models.contacts_get401_response_inner import ContactsGet401ResponseInner
from openapi_server.models.contacts_get404_response_inner import ContactsGet404ResponseInner
from openapi_server.models.contacts_get422_response_inner import ContactsGet422ResponseInner
from openapi_server import util


async def contacts_contactid_delete(request: web.Request, contactid) -> web.Response:
    """contacts_contactid_delete

    Delete an existing contact

    :param contactid: Unique 16 characters ID of the contact
    :type contactid: str

    """
    return web.Response(status=200)


async def contacts_contactid_put(request: web.Request, contactid, contact) -> web.Response:
    """contacts_contactid_put

    Update an existing contact

    :param contactid: Unique 16 characters ID of the contact
    :type contactid: str
    :param contact: Contact properties to update
    :type contact: dict | bytes

    """
    contact = ContactUpdate.from_dict(contact)
    return web.Response(status=200)


async def contacts_get(request: web.Request, listid=None, offset=None, limit=None, sort=None) -> web.Response:
    """contacts_get

    Get a paged result of contacts from a list

    :param listid: Unique 16 characters ID of the contact list to get contacts of
    :type listid: str
    :param offset: Skip that many records
    :type offset: int
    :param limit: Maximum number of items in page
    :type limit: int
    :param sort: Property to sort by. Append &#39;-&#39; for descending order.
    :type sort: str

    """
    return web.Response(status=200)
