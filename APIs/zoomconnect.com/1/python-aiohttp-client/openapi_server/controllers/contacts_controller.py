from typing import List, Dict
from aiohttp import web

from openapi_server.models.web_service_contact import WebServiceContact
from openapi_server.models.web_service_contacts import WebServiceContacts
from openapi_server import util


async def api_rest_v1_contacts_all_get(request: web.Request, ) -> web.Response:
    """all

    Returns all contacts


    """
    return web.Response(status=200)


async def api_rest_v1_contacts_contact_id_add_from_group_group_id_get(request: web.Request, contact_id, group_id) -> web.Response:
    """removeFromGroup

    Remove a contact from a group

    :param contact_id: contactId
    :type contact_id: str
    :param group_id: groupId
    :type group_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_contacts_contact_id_add_from_group_group_id_post(request: web.Request, contact_id, group_id) -> web.Response:
    """removeFromGroup

    Remove a contact from a group

    :param contact_id: contactId
    :type contact_id: str
    :param group_id: groupId
    :type group_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_contacts_contact_id_add_to_group_group_id_get(request: web.Request, contact_id, group_id) -> web.Response:
    """addToGroup

    Add a contact to a group

    :param contact_id: contactId
    :type contact_id: str
    :param group_id: groupId
    :type group_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_contacts_contact_id_add_to_group_group_id_post(request: web.Request, contact_id, group_id) -> web.Response:
    """addToGroup

    Add a contact to a group

    :param contact_id: contactId
    :type contact_id: str
    :param group_id: groupId
    :type group_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_contacts_contact_id_delete(request: web.Request, contact_id) -> web.Response:
    """delete

    Deletes a  contact

    :param contact_id: contactId
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_contacts_contact_id_get(request: web.Request, contact_id) -> web.Response:
    """get

    Returns details for a single contact

    :param contact_id: contactId
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_contacts_contact_id_post(request: web.Request, contact_id, body=None) -> web.Response:
    """update

    Updates a  contact

    :param contact_id: contactId
    :type contact_id: str
    :param body: webServiceContact
    :type body: dict | bytes

    """
    body = WebServiceContact.from_dict(body)
    return web.Response(status=200)


async def api_rest_v1_contacts_create_post(request: web.Request, body=None) -> web.Response:
    """create

    Creates a  contact

    :param body: webServiceContact
    :type body: dict | bytes

    """
    body = WebServiceContact.from_dict(body)
    return web.Response(status=200)
