from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.invitation import Invitation
from openapi_server.models.invitation_list import InvitationList
from openapi_server import util


async def invitations_create(request: web.Request, subscription_id, resource_group_name, account_name, share_name, invitation_name, api_version, invitation) -> web.Response:
    """Sends a new invitation to a recipient to access a share.

    Create an invitation 

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share to send the invitation for.
    :type share_name: str
    :param invitation_name: The name of the invitation.
    :type invitation_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param invitation: Invitation details.
    :type invitation: dict | bytes

    """
    invitation = Invitation.from_dict(invitation)
    return web.Response(status=200)


async def invitations_delete(request: web.Request, subscription_id, resource_group_name, account_name, share_name, invitation_name, api_version) -> web.Response:
    """Delete Invitation in a share.

    Delete an invitation in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param invitation_name: The name of the invitation.
    :type invitation_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def invitations_get(request: web.Request, subscription_id, resource_group_name, account_name, share_name, invitation_name, api_version) -> web.Response:
    """Get Invitation in a share.

    Get an invitation in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param invitation_name: The name of the invitation.
    :type invitation_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def invitations_list_by_share(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version, skip_token=None) -> web.Response:
    """List all Invitations in a share.

    List invitations in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: The continuation token
    :type skip_token: str

    """
    return web.Response(status=200)
