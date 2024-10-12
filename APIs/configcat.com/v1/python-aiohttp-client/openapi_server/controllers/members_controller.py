from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user_to_group_request import AddUserToGroupRequest
from openapi_server.models.invite_members_request import InviteMembersRequest
from openapi_server.models.member_model import MemberModel
from openapi_server.models.user_model import UserModel
from openapi_server import util


async def add_member_to_group(request: web.Request, organization_id, user_id, body) -> web.Response:
    """Update Member Permissions

    This endpoint adds a Member identified by the &#x60;userId&#x60; to one or more Permission Groups.  This endpoint can also be used to move a Member between Permission Groups within a Product. Only a single Permission Group can be set per Product.

    :param organization_id: The identifier of the Organization.
    :type organization_id: str
    :type organization_id: str
    :param user_id: The identifier of the Member.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddUserToGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_member(request: web.Request, organization_id, user_id) -> web.Response:
    """Delete Member from Organization

    This endpoint removes a Member identified by the &#x60;userId&#x60; from the  given Organization identified by the &#x60;organizationId&#x60; parameter.

    :param organization_id: The identifier of the Organization.
    :type organization_id: str
    :type organization_id: str
    :param user_id: The identifier of the Member.
    :type user_id: str

    """
    return web.Response(status=200)


async def delete_product_member(request: web.Request, product_id, user_id) -> web.Response:
    """Delete Member from Product

    This endpoint removes a Member identified by the &#x60;userId&#x60; from the  given Product identified by the &#x60;productId&#x60; parameter.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param user_id: The identifier of the Member.
    :type user_id: str

    """
    return web.Response(status=200)


async def get_organization_members(request: web.Request, organization_id) -> web.Response:
    """List Organization Members

    This endpoint returns the list of Members that belongs  to the given Organization, identified by the &#x60;organizationId&#x60; parameter.

    :param organization_id: The identifier of the Organization.
    :type organization_id: str
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_product_members(request: web.Request, product_id) -> web.Response:
    """List Product Members

    This endpoint returns the list of Members that belongs  to the given Product, identified by the &#x60;productId&#x60; parameter.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def invite_member(request: web.Request, product_id, body) -> web.Response:
    """Invite Member

    This endpoint invites a Member into the given Product identified by the &#x60;productId&#x60; parameter.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = InviteMembersRequest.from_dict(body)
    return web.Response(status=200)
