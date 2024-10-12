from typing import List, Dict
from aiohttp import web

from openapi_server.models.contacts_list_vo import ContactsListVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.user_details_expand_vo import UserDetailsExpandVO
from openapi_server import util


async def get_billing_recipients(request: web.Request, workgroup_id) -> web.Response:
    """List Billing Recipients

    List Billing Recipients

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_contact_list(request: web.Request, workgroup_id) -> web.Response:
    """List the contacts

    List the contacts

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_contact_user_info(request: web.Request, workgroup_id, user_id) -> web.Response:
    """Contact Info

    Contact Info

    :param workgroup_id: 
    :type workgroup_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
