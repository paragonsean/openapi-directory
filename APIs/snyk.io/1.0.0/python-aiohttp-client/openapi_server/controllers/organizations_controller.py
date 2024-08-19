from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_a_new_organization400_response import CreateANewOrganization400Response
from openapi_server.models.create_a_new_organization_request import CreateANewOrganizationRequest
from openapi_server.models.delete_pending_user_provision200_response import DeletePendingUserProvision200Response
from openapi_server.models.invite_users_request import InviteUsersRequest
from openapi_server.models.org_org_id_notification_settings_get200_response import OrgOrgIdNotificationSettingsGet200Response
from openapi_server.models.provision_a_user_to_the_organization200_response import ProvisionAUserToTheOrganization200Response
from openapi_server.models.provision_a_user_to_the_organization_request import ProvisionAUserToTheOrganizationRequest
from openapi_server.models.set_notification_settings_request import SetNotificationSettingsRequest
from openapi_server.models.update_a_member_in_the_organization_request import UpdateAMemberInTheOrganizationRequest
from openapi_server.models.update_a_member_s_role_in_the_organization_request import UpdateAMemberSRoleInTheOrganizationRequest
from openapi_server.models.update_organization_settings_request import UpdateOrganizationSettingsRequest
from openapi_server.models.view_organization_settings200_response import ViewOrganizationSettings200Response
from openapi_server import util


async def create_a_new_organization(request: web.Request, body=None) -> web.Response:
    """Create a new organization

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateANewOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_pending_user_provision(request: web.Request, org_id) -> web.Response:
    """Delete pending user provision

    

    :param org_id: The organization ID.
    :type org_id: str

    """
    return web.Response(status=200)


async def invite_users(request: web.Request, org_id, body=None) -> web.Response:
    """Invite users

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = InviteUsersRequest.from_dict(body)
    return web.Response(status=200)


async def list_all_the_organizations_a_user_belongs_to(request: web.Request, ) -> web.Response:
    """List all the organizations a user belongs to

    


    """
    return web.Response(status=200)


async def list_members(request: web.Request, org_id, include_group_admins=None) -> web.Response:
    """List Members

    

    :param org_id: The organization ID.
    :type org_id: str
    :param include_group_admins: Include group administrators who also have access to this organization.
    :type include_group_admins: bool

    """
    return web.Response(status=200)


async def list_pending_user_provisions(request: web.Request, org_id) -> web.Response:
    """List pending user provisions

    

    :param org_id: The organization ID.
    :type org_id: str

    """
    return web.Response(status=200)


async def org_org_id_notification_settings_get(request: web.Request, org_id) -> web.Response:
    """Get organization notification settings

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str

    """
    return web.Response(status=200)


async def provision_a_user_to_the_organization(request: web.Request, org_id, body=None) -> web.Response:
    """Provision a user to the organization

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must not exceed the permissions being granted to the provisioned user.
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProvisionAUserToTheOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def remove_a_member_from_the_organization(request: web.Request, org_id, user_id) -> web.Response:
    """Remove a member from the organization

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must admin have access to this organization.
    :type org_id: str
    :param user_id: The user ID we want to remove.
    :type user_id: str

    """
    return web.Response(status=200)


async def remove_organization(request: web.Request, org_id) -> web.Response:
    """Remove organization

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have permission to delete the provided organization. Currently this operation is only supported for organizations without any projects.
    :type org_id: str

    """
    return web.Response(status=200)


async def set_notification_settings(request: web.Request, org_id, body=None) -> web.Response:
    """Set notification settings

    

    :param org_id: Automatically added
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetNotificationSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_a_member_in_the_organization(request: web.Request, org_id, user_id, body=None) -> web.Response:
    """Update a member in the organization

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAMemberInTheOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def update_a_members_role_in_the_organization(request: web.Request, org_id, user_id, body=None) -> web.Response:
    """Update a member&#39;s role in the organization

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param user_id: The user ID.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAMemberSRoleInTheOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_settings(request: web.Request, org_id, body=None) -> web.Response:
    """Update organization settings

    Settings that are not provided will not be modified.

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def view_organization_settings(request: web.Request, org_id) -> web.Response:
    """View organization settings

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str

    """
    return web.Response(status=200)
