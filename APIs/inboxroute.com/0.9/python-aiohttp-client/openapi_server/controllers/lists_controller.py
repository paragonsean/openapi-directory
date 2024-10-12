from typing import List, Dict
from aiohttp import web

from openapi_server.models.contact_list_page import ContactListPage
from openapi_server.models.contact_list_update import ContactListUpdate
from openapi_server.models.contacts_get401_response_inner import ContactsGet401ResponseInner
from openapi_server.models.contacts_get404_response_inner import ContactsGet404ResponseInner
from openapi_server.models.contacts_get422_response_inner import ContactsGet422ResponseInner
from openapi_server.models.new_id import NewId
from openapi_server import util


async def contacts_lists_get(request: web.Request, offset=None, limit=None, sort=None) -> web.Response:
    """contacts_lists_get

    Get a paged result of contact lists.

    :param offset: Skip that many records
    :type offset: int
    :param limit: Maximum number of items in page
    :type limit: int
    :param sort: Property to sort by. Append &#39;-&#39; for descending order.
    :type sort: str

    """
    return web.Response(status=200)


async def contacts_lists_listid_delete(request: web.Request, listid) -> web.Response:
    """contacts_lists_listid_delete

    Delete an existing contact list

    :param listid: Unique 16 characters ID of the contact list
    :type listid: str

    """
    return web.Response(status=200)


async def contacts_lists_listid_put(request: web.Request, listid, contactlist=None) -> web.Response:
    """contacts_lists_listid_put

    Update an existing contact list

    :param listid: Unique 16 characters ID of the contact list
    :type listid: str
    :param contactlist: Contact list properties to update
    :type contactlist: dict | bytes

    """
    contactlist = ContactListUpdate.from_dict(contactlist)
    return web.Response(status=200)


async def contacts_lists_post(request: web.Request, contactlist=None) -> web.Response:
    """contacts_lists_post

    Add a new contact list

    :param contactlist: Contact list initial properties
    :type contactlist: dict | bytes

    """
    contactlist = ContactListUpdate.from_dict(contactlist)
    return web.Response(status=200)
