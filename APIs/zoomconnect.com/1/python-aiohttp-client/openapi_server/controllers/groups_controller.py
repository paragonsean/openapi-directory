from typing import List, Dict
from aiohttp import web

from openapi_server.models.web_service_group import WebServiceGroup
from openapi_server.models.web_service_groups import WebServiceGroups
from openapi_server import util


async def api_rest_v1_groups_all_get(request: web.Request, ) -> web.Response:
    """all

    Returns all groups


    """
    return web.Response(status=200)


async def api_rest_v1_groups_create_post(request: web.Request, body=None) -> web.Response:
    """create

    Create a  group

    :param body: webServiceGroup
    :type body: dict | bytes

    """
    body = WebServiceGroup.from_dict(body)
    return web.Response(status=200)


async def api_rest_v1_groups_group_id_add_contact_contact_id_get(request: web.Request, group_id, contact_id) -> web.Response:
    """addContact

    Add a contact to a group

    :param group_id: groupId
    :type group_id: str
    :param contact_id: contactId
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_groups_group_id_add_contact_contact_id_post(request: web.Request, group_id, contact_id) -> web.Response:
    """addContact

    Add a contact to a group

    :param group_id: groupId
    :type group_id: str
    :param contact_id: contactId
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_groups_group_id_delete(request: web.Request, group_id) -> web.Response:
    """delete

    Deletes a  group

    :param group_id: groupId
    :type group_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_groups_group_id_get(request: web.Request, group_id) -> web.Response:
    """get

    Returns details for a single group

    :param group_id: groupId
    :type group_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_groups_group_id_post(request: web.Request, group_id, body=None) -> web.Response:
    """update

    Update a  group

    :param group_id: groupId
    :type group_id: str
    :param body: webServiceGroup
    :type body: dict | bytes

    """
    body = WebServiceGroup.from_dict(body)
    return web.Response(status=200)


async def api_rest_v1_groups_group_id_remove_contact_contact_id_get(request: web.Request, group_id, contact_id) -> web.Response:
    """removeContact

    Remove a contact from a group

    :param group_id: groupId
    :type group_id: str
    :param contact_id: contactId
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_rest_v1_groups_group_id_remove_contact_contact_id_post(request: web.Request, group_id, contact_id) -> web.Response:
    """removeContact

    Remove a contact from a group

    :param group_id: groupId
    :type group_id: str
    :param contact_id: contactId
    :type contact_id: str

    """
    return web.Response(status=200)
