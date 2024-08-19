from typing import List, Dict
from aiohttp import web

from openapi_server.models.campaigns_remove200_response import CampaignsRemove200Response
from openapi_server.models.contact_request import ContactRequest
from openapi_server.models.contact_response import ContactResponse
from openapi_server.models.contacts_create201_response import ContactsCreate201Response
from openapi_server.models.contacts_response import ContactsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def contacts_create(request: web.Request, account_id, merge_strategy=None, body=None) -> web.Response:
    """Create contact

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param merge_strategy: Determines how existing contacts with matching mobile numbers are treated
    :type merge_strategy: str
    :param body: 
    :type body: dict | bytes

    """
    body = ContactRequest.from_dict(body)
    return web.Response(status=200)


async def contacts_fetch(request: web.Request, account_id, contact_id) -> web.Response:
    """Fetch contact by ID

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param contact_id: ID of contact to return
    :type contact_id: str

    """
    return web.Response(status=200)


async def contacts_fetch_all(request: web.Request, account_id, offset=None, limit=None, first_name=None, last_name=None, mobile=None, email=None, tags=None) -> web.Response:
    """Fetch contacts

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param offset: Results to skip when paginating through a result set
    :type offset: int
    :param limit: Maximum number of results to return
    :type limit: int
    :param first_name: Filter by first name or part of
    :type first_name: str
    :param last_name: Filter by last name or part of
    :type last_name: str
    :param mobile: Filter by mobile or part of
    :type mobile: str
    :param email: Filter by email or part of
    :type email: str
    :param tags: Filter by tag(s)
    :type tags: str

    """
    return web.Response(status=200)


async def contacts_remove(request: web.Request, account_id, contact_id) -> web.Response:
    """Deletes a contact

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param contact_id: Contact id to delete
    :type contact_id: str

    """
    return web.Response(status=200)


async def contacts_update(request: web.Request, account_id, contact_id) -> web.Response:
    """Updates a contact

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param contact_id: ID of contact
    :type contact_id: str

    """
    return web.Response(status=200)
