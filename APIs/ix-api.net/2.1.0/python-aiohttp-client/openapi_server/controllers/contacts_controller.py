from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contact import Contact
from openapi_server.models.contact_request import ContactRequest
from openapi_server.models.contact_request_partial import ContactRequestPartial
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server import util


async def contacts_create(request: web.Request, body=None) -> web.Response:
    """contacts_create

    Create a new contact.

    :param body: A contact creation request
    :type body: dict | bytes

    """
    body = ContactRequest.from_dict(body)
    return web.Response(status=200)


async def contacts_destroy(request: web.Request, id) -> web.Response:
    """contacts_destroy

    Remove a contact.  Please note, that a contact can only be removed if it is not longer in use in a network service or config through a role assignment.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def contacts_list(request: web.Request, id=None, managing_account=None, consuming_account=None, external_ref=None) -> web.Response:
    """contacts_list

    List available contacts managed by the authorized account.

    :param id: Filter by id
    :type id: List[str]
    :param managing_account: Filter by managing_account
    :type managing_account: str
    :param consuming_account: Filter by consuming_account
    :type consuming_account: str
    :param external_ref: Filter by external_ref
    :type external_ref: str

    """
    return web.Response(status=200)


async def contacts_partial_update(request: web.Request, id, body=None) -> web.Response:
    """contacts_partial_update

    Update parts of a contact

    :param id: Get by id
    :type id: str
    :param body: A contact creation request
    :type body: dict | bytes

    """
    body = ContactRequestPartial.from_dict(body)
    return web.Response(status=200)


async def contacts_read(request: web.Request, id) -> web.Response:
    """contacts_read

    Get a contact by it&#39;s id

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def contacts_update(request: web.Request, id, body=None) -> web.Response:
    """contacts_update

    Update a contact

    :param id: Get by id
    :type id: str
    :param body: A contact creation request
    :type body: dict | bytes

    """
    body = ContactRequest.from_dict(body)
    return web.Response(status=200)
