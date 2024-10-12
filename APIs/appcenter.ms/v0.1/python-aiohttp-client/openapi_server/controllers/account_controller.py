from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_invitations_create_by_email_request import AppInvitationsCreateByEmailRequest
from openapi_server.models.app_invitations_create_request import AppInvitationsCreateRequest
from openapi_server.models.app_invitations_list200_response import AppInvitationsList200Response
from openapi_server.models.app_invitations_list200_response_invited_by import AppInvitationsList200ResponseInvitedBy
from openapi_server.models.app_invitations_update_permissions_request import AppInvitationsUpdatePermissionsRequest
from openapi_server.models.apps_create_request import AppsCreateRequest
from openapi_server.models.apps_get_teams200_response_inner import AppsGetTeams200ResponseInner
from openapi_server.models.apps_list200_response_inner import AppsList200ResponseInner
from openapi_server.models.apps_list200_response_inner_all_of_azure_subscription import AppsList200ResponseInnerAllOfAzureSubscription
from openapi_server.models.apps_update_request import AppsUpdateRequest
from openapi_server.models.apps_update_user_permissions_request import AppsUpdateUserPermissionsRequest
from openapi_server.models.azure_subscription_link_for_app_request import AzureSubscriptionLinkForAppRequest
from openapi_server.models.distribution_groups_add_apps_request import DistributionGroupsAddAppsRequest
from openapi_server.models.distribution_groups_add_apps_request_apps_inner import DistributionGroupsAddAppsRequestAppsInner
from openapi_server.models.distribution_groups_add_user200_response_inner import DistributionGroupsAddUser200ResponseInner
from openapi_server.models.distribution_groups_add_user_request import DistributionGroupsAddUserRequest
from openapi_server.models.distribution_groups_bulk_delete_apps_request import DistributionGroupsBulkDeleteAppsRequest
from openapi_server.models.distribution_groups_create_request import DistributionGroupsCreateRequest
from openapi_server.models.distribution_groups_details_for_org200_response_inner import DistributionGroupsDetailsForOrg200ResponseInner
from openapi_server.models.distribution_groups_get_apps200_response_inner import DistributionGroupsGetApps200ResponseInner
from openapi_server.models.distribution_groups_list200_response_inner import DistributionGroupsList200ResponseInner
from openapi_server.models.distribution_groups_list_all_testers_for_org200_response_inner import DistributionGroupsListAllTestersForOrg200ResponseInner
from openapi_server.models.distribution_groups_list_users200_response_inner import DistributionGroupsListUsers200ResponseInner
from openapi_server.models.distribution_groups_remove_user200_response_inner import DistributionGroupsRemoveUser200ResponseInner
from openapi_server.models.distribution_groups_update_request import DistributionGroupsUpdateRequest
from openapi_server.models.invitations_sent200_response_inner import InvitationsSent200ResponseInner
from openapi_server.models.org_invitations_delete_request import OrgInvitationsDeleteRequest
from openapi_server.models.org_invitations_list_pending200_response_inner import OrgInvitationsListPending200ResponseInner
from openapi_server.models.org_invitations_update_request import OrgInvitationsUpdateRequest
from openapi_server.models.organizations_create_or_update_request import OrganizationsCreateOrUpdateRequest
from openapi_server.models.organizations_list200_response_inner import OrganizationsList200ResponseInner
from openapi_server.models.organizations_list_administered200_response import OrganizationsListAdministered200Response
from openapi_server.models.organizations_list_administered200_response_organizations import OrganizationsListAdministered200ResponseOrganizations
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse
from openapi_server.models.organizations_list_administered_default_response_error import OrganizationsListAdministeredDefaultResponseError
from openapi_server.models.organizations_update_request import OrganizationsUpdateRequest
from openapi_server.models.sharedconnection_connections200_response_inner import SharedconnectionConnections200ResponseInner
from openapi_server.models.teams_create_team_request import TeamsCreateTeamRequest
from openapi_server.models.teams_get_users200_response import TeamsGetUsers200Response
from openapi_server.models.teams_list_all200_response_inner import TeamsListAll200ResponseInner
from openapi_server.models.teams_list_apps200_response_inner import TeamsListApps200ResponseInner
from openapi_server.models.teams_update_permissions_request import TeamsUpdatePermissionsRequest
from openapi_server.models.teams_update_request import TeamsUpdateRequest
from openapi_server.models.user_api_tokens_list200_response_inner import UserApiTokensList200ResponseInner
from openapi_server.models.user_api_tokens_new201_response import UserApiTokensNew201Response
from openapi_server.models.user_api_tokens_new_request import UserApiTokensNewRequest
from openapi_server.models.users_get_user_metadata200_response import UsersGetUserMetadata200Response
from openapi_server.models.users_get_user_metadata_default_response import UsersGetUserMetadataDefaultResponse
from openapi_server.models.users_list_for_org200_response_inner import UsersListForOrg200ResponseInner
from openapi_server.models.users_update_request import UsersUpdateRequest
from openapi_server import util


async def app_api_tokens_delete(request: web.Request, owner_name, app_name, api_token_id) -> web.Response:
    """app_api_tokens_delete

    Delete the App Api Token object with the specific ID

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param api_token_id: The unique ID (UUID) of the api token
    :type api_token_id: str

    """
    return web.Response(status=200)


async def app_api_tokens_list(request: web.Request, owner_name, app_name) -> web.Response:
    """app_api_tokens_list

    Returns App API tokens for the app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def app_api_tokens_new(request: web.Request, owner_name, app_name, body=None) -> web.Response:
    """app_api_tokens_new

    Creates a new App API token

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Description of the token
    :type body: dict | bytes

    """
    body = UserApiTokensNewRequest.from_dict(body)
    return web.Response(status=200)


async def app_invitations_accept(request: web.Request, invitation_token, body=None) -> web.Response:
    """app_invitations_accept

    Accepts a pending invitation for the specified user

    :param invitation_token: The app invitation token that was sent to the user
    :type invitation_token: str
    :param body: allow empty body for custom http-client lib
    :type body: 

    """
    return web.Response(status=200)


async def app_invitations_create(request: web.Request, owner_name, app_name, body=None) -> web.Response:
    """app_invitations_create

    Invites a new or existing user to an app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The email of the user to invite
    :type body: dict | bytes

    """
    body = AppInvitationsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_invitations_create_by_email(request: web.Request, owner_name, app_name, user_email, body=None) -> web.Response:
    """app_invitations_create_by_email

    Invites a new or existing user to an app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param user_email: The email of the user to invite
    :type user_email: str
    :param body: The role of the user to be added
    :type body: dict | bytes

    """
    body = AppInvitationsCreateByEmailRequest.from_dict(body)
    return web.Response(status=200)


async def app_invitations_delete(request: web.Request, owner_name, app_name, user_email) -> web.Response:
    """app_invitations_delete

    Removes a user&#39;s invitation to an app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param user_email: The email of the user to invite
    :type user_email: str

    """
    return web.Response(status=200)


async def app_invitations_list(request: web.Request, owner_name, app_name) -> web.Response:
    """app_invitations_list

    Gets the pending invitations for the app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def app_invitations_reject(request: web.Request, invitation_token, body=None) -> web.Response:
    """app_invitations_reject

    Rejects a pending invitation for the specified user

    :param invitation_token: The app invitation token that was sent to the user
    :type invitation_token: str
    :param body: allow empty body for custom http-client lib
    :type body: 

    """
    return web.Response(status=200)


async def app_invitations_update_permissions(request: web.Request, owner_name, app_name, user_email, body) -> web.Response:
    """app_invitations_update_permissions

    Update pending invitation permission

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param user_email: The email of the user to invite
    :type user_email: str
    :param body: The value to update the user permission in the invite.
    :type body: dict | bytes

    """
    body = AppInvitationsUpdatePermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def apps_create(request: web.Request, body) -> web.Response:
    """apps_create

    Creates a new app and returns it to the caller

    :param body: The data for the app
    :type body: dict | bytes

    """
    body = AppsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def apps_create_for_org(request: web.Request, org_name, body) -> web.Response:
    """apps_create_for_org

    Creates a new app for the organization and returns it to the caller

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param body: The data for the app
    :type body: dict | bytes

    """
    body = AppsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def apps_delete(request: web.Request, app_name, owner_name) -> web.Response:
    """apps_delete

    Delete an app

    :param app_name: The name of the application
    :type app_name: str
    :param owner_name: The name of the owner
    :type owner_name: str

    """
    return web.Response(status=200)


async def apps_delete_avatar(request: web.Request, owner_name, app_name) -> web.Response:
    """apps_delete_avatar

    Deletes the uploaded app avatar

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def apps_get(request: web.Request, owner_name, app_name) -> web.Response:
    """apps_get

    Return a specific app with the given app name which belongs to the given owner.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def apps_get_for_org_user(request: web.Request, org_name, user_name) -> web.Response:
    """apps_get_for_org_user

    Get a user apps information from an organization by name

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param user_name: The slug name of the user
    :type user_name: str

    """
    return web.Response(status=200)


async def apps_get_teams(request: web.Request, app_name, owner_name) -> web.Response:
    """apps_get_teams

    Returns the details of all teams that have access to the app.

    :param app_name: The name of the application
    :type app_name: str
    :param owner_name: The name of the owner
    :type owner_name: str

    """
    return web.Response(status=200)


async def apps_list(request: web.Request, order_by=None) -> web.Response:
    """apps_list

    Returns a list of apps

    :param order_by: The name of the attribute by which to order the response by. By default, apps are in order of creation. All results are ordered in ascending order.
    :type order_by: str

    """
    return web.Response(status=200)


async def apps_list_for_org(request: web.Request, org_name) -> web.Response:
    """apps_list_for_org

    Returns a list of apps for the organization

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def apps_list_testers(request: web.Request, owner_name, app_name) -> web.Response:
    """apps_list_testers

    Returns the testers associated with the app specified with the given app name which belongs to the given owner.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def apps_remove_user(request: web.Request, owner_name, app_name, user_email) -> web.Response:
    """apps_remove_user

    Removes the user from the app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param user_email: The user email of the user to delete
    :type user_email: str

    """
    return web.Response(status=200)


async def apps_transfer_ownership(request: web.Request, owner_name, app_name, destination_owner_name, body=None) -> web.Response:
    """apps_transfer_ownership

    Transfers ownership of an app to a different user or organization

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param destination_owner_name: The name of the owner (user or organization) to which the app is being transferred
    :type destination_owner_name: str
    :param body: allow empty body for custom http-client lib
    :type body: 

    """
    return web.Response(status=200)


async def apps_transfer_to_org(request: web.Request, owner_name, app_name, body=None) -> web.Response:
    """apps_transfer_to_org

    Transfers ownership of an app to a new organization

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: allow empty body for custom http-client lib
    :type body: 

    """
    return web.Response(status=200)


async def apps_update(request: web.Request, app_name, owner_name, body=None) -> web.Response:
    """apps_update

    Partially updates a single app

    :param app_name: The name of the application
    :type app_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param body: The partial data for the app
    :type body: dict | bytes

    """
    body = AppsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def apps_update_avatar(request: web.Request, owner_name, app_name, avatar=None) -> web.Response:
    """apps_update_avatar

    Sets the app avatar

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param avatar: The image for an app avatar to upload.
    :type avatar: str

    """
    return web.Response(status=200)


async def apps_update_user_permissions(request: web.Request, owner_name, app_name, user_email, body) -> web.Response:
    """apps_update_user_permissions

    Update user permission for the app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param user_email: The user email of the user to patch
    :type user_email: str
    :param body: The value to update the user permission for the app.
    :type body: dict | bytes

    """
    body = AppsUpdateUserPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def azure_subscription_delete_for_app(request: web.Request, azure_subscription_id, owner_name, app_name) -> web.Response:
    """azure_subscription_delete_for_app

    Delete the azure subscriptions for the app

    :param azure_subscription_id: The unique ID (UUID) of the azure subscription
    :type azure_subscription_id: str
    :type azure_subscription_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def azure_subscription_link_for_app(request: web.Request, owner_name, app_name, body) -> web.Response:
    """azure_subscription_link_for_app

    Link azure subscription to an app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The azure subscription data needed to be link to the app.
    :type body: dict | bytes

    """
    body = AzureSubscriptionLinkForAppRequest.from_dict(body)
    return web.Response(status=200)


async def azure_subscription_list_for_app(request: web.Request, owner_name, app_name) -> web.Response:
    """azure_subscription_list_for_app

    Returns a list of azure subscriptions for the app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def azure_subscription_list_for_org(request: web.Request, org_name) -> web.Response:
    """azure_subscription_list_for_org

    Returns a list of azure subscriptions for the organization

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def azure_subscription_list_for_user(request: web.Request, ) -> web.Response:
    """azure_subscription_list_for_user

    Returns a list of azure subscriptions for the user


    """
    return web.Response(status=200)


async def distribution_group_invitations_accept_all(request: web.Request, body=None) -> web.Response:
    """distribution_group_invitations_accept_all

    Accepts all pending invitations to distribution groups for the specified user

    :param body: allow empty body for custom http-client lib
    :type body: 

    """
    return web.Response(status=200)


async def distribution_groups_add_apps(request: web.Request, org_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_add_apps

    Add apps to distribution group in an org

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The name of the apps to be added to the distribution group. The apps have to be owned by the organization.
    :type body: dict | bytes

    """
    body = DistributionGroupsAddAppsRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_add_user(request: web.Request, owner_name, app_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_add_user

    Adds the members to the specified distribution group

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The list of members to add
    :type body: dict | bytes

    """
    body = DistributionGroupsAddUserRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_add_users_for_org(request: web.Request, org_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_add_users_for_org

    Accepts an array of user email addresses to get added to the specified group

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: list of user email addresses that should get added as members to the specified group
    :type body: dict | bytes

    """
    body = DistributionGroupsAddUserRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_bulk_delete_apps(request: web.Request, org_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_bulk_delete_apps

    Delete apps from distribution group in an org

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The name of the apps to be deleted from the distribution group. The apps have to be owned by the organization.
    :type body: dict | bytes

    """
    body = DistributionGroupsBulkDeleteAppsRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_bulk_delete_users(request: web.Request, org_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_bulk_delete_users

    Delete testers from distribution group in an org

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The list of members to add
    :type body: dict | bytes

    """
    body = DistributionGroupsAddUserRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_create(request: web.Request, owner_name, app_name, body) -> web.Response:
    """distribution_groups_create

    Creates a new distribution group and returns it to the caller

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The attributes to update for the distribution group
    :type body: dict | bytes

    """
    body = DistributionGroupsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_create_for_org(request: web.Request, org_name, body) -> web.Response:
    """distribution_groups_create_for_org

    Creates a disribution goup which can be shared across apps under an organization

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param body: The attributes to update for the distribution group
    :type body: dict | bytes

    """
    body = DistributionGroupsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_delete(request: web.Request, app_name, owner_name, distribution_group_name) -> web.Response:
    """distribution_groups_delete

    Deletes a distribution group

    :param app_name: The name of the application
    :type app_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str

    """
    return web.Response(status=200)


async def distribution_groups_delete_for_org(request: web.Request, org_name, distribution_group_name) -> web.Response:
    """distribution_groups_delete_for_org

    Deletes a single distribution group from an org with a given distribution group name

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str

    """
    return web.Response(status=200)


async def distribution_groups_details_for_org(request: web.Request, org_name, apps_limit=None) -> web.Response:
    """distribution_groups_details_for_org

    Returns a list of distribution groups with details for an organization

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param apps_limit: The max number of apps to include in the response
    :type apps_limit: 

    """
    return web.Response(status=200)


async def distribution_groups_get(request: web.Request, owner_name, app_name, distribution_group_name) -> web.Response:
    """distribution_groups_get

    Returns a single distribution group for a given distribution group name

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str

    """
    return web.Response(status=200)


async def distribution_groups_get_apps(request: web.Request, org_name, distribution_group_name) -> web.Response:
    """distribution_groups_get_apps

    Get apps from a distribution group in an org

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str

    """
    return web.Response(status=200)


async def distribution_groups_get_for_org(request: web.Request, org_name, distribution_group_name) -> web.Response:
    """distribution_groups_get_for_org

    Returns a single distribution group in org for a given distribution group name

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str

    """
    return web.Response(status=200)


async def distribution_groups_list(request: web.Request, owner_name, app_name) -> web.Response:
    """distribution_groups_list

    Returns a list of distribution groups in the app specified

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def distribution_groups_list_all_testers_for_org(request: web.Request, org_name) -> web.Response:
    """distribution_groups_list_all_testers_for_org

    Returns a unique list of users including the whole organization members plus testers in any shared group of that org

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def distribution_groups_list_for_org(request: web.Request, org_name) -> web.Response:
    """distribution_groups_list_for_org

    Returns a list of distribution groups in the org specified

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def distribution_groups_list_users(request: web.Request, owner_name, app_name, distribution_group_name, exclude_pending_invitations=None) -> web.Response:
    """distribution_groups_list_users

    Returns a list of member details in the distribution group specified

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param exclude_pending_invitations: Whether to exclude pending invitations in the response
    :type exclude_pending_invitations: bool

    """
    return web.Response(status=200)


async def distribution_groups_list_users_for_org(request: web.Request, org_name, distribution_group_name) -> web.Response:
    """distribution_groups_list_users_for_org

    Returns a list of member in the distribution group specified

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str

    """
    return web.Response(status=200)


async def distribution_groups_patch_for_org(request: web.Request, org_name, distribution_group_name, body=None) -> web.Response:
    """distribution_groups_patch_for_org

    Update one given distribution group name in an org

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The attributes to update for the distribution group
    :type body: dict | bytes

    """
    body = DistributionGroupsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_remove_user(request: web.Request, owner_name, app_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_remove_user

    Remove the users from the distribution group

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The list of members to add
    :type body: dict | bytes

    """
    body = DistributionGroupsAddUserRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_resend_invite(request: web.Request, owner_name, app_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_resend_invite

    Resend distribution group app invite notification to previously invited testers

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The list of members to add
    :type body: dict | bytes

    """
    body = DistributionGroupsAddUserRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_resend_shared_invite(request: web.Request, org_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_resend_shared_invite

    Resend shared distribution group invite notification to previously invited testers

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The list of members to add
    :type body: dict | bytes

    """
    body = DistributionGroupsAddUserRequest.from_dict(body)
    return web.Response(status=200)


async def distribution_groups_update(request: web.Request, owner_name, app_name, distribution_group_name, body) -> web.Response:
    """distribution_groups_update

    Updates the attributes of distribution group

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param distribution_group_name: The name of the distribution group
    :type distribution_group_name: str
    :param body: The attributes to update for the distribution group
    :type body: dict | bytes

    """
    body = DistributionGroupsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def invitations_sent(request: web.Request, ) -> web.Response:
    """invitations_sent

    Returns all invitations sent by the caller


    """
    return web.Response(status=200)


async def org_invitations(request: web.Request, org_name, email, body=None) -> web.Response:
    """org_invitations

    Removes a user&#39;s invitation to an organization

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param email: The email address of the user to send the password reset mail to.
    :type email: str
    :param body: allow empty body for custom http-client lib
    :type body: 

    """
    return web.Response(status=200)


async def org_invitations_accept(request: web.Request, invitation_token, body=None) -> web.Response:
    """org_invitations_accept

    Accepts a pending organization invitation for the specified user

    :param invitation_token: The app invitation token that was sent to the user
    :type invitation_token: str
    :param body: allow empty body for custom http-client lib
    :type body: 

    """
    return web.Response(status=200)


async def org_invitations_create(request: web.Request, org_name, body) -> web.Response:
    """org_invitations_create

    Invites a new or existing user to an organization

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param body: The email of the user to invite
    :type body: dict | bytes

    """
    body = AppInvitationsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def org_invitations_delete(request: web.Request, org_name, body) -> web.Response:
    """org_invitations_delete

    Removes a user&#39;s invitation to an organization

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param body: The email of the user whose invitation should be removed
    :type body: dict | bytes

    """
    body = OrgInvitationsDeleteRequest.from_dict(body)
    return web.Response(status=200)


async def org_invitations_list_pending(request: web.Request, org_name) -> web.Response:
    """org_invitations_list_pending

    Gets the pending invitations for the organization

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def org_invitations_reject(request: web.Request, invitation_token, body=None) -> web.Response:
    """org_invitations_reject

    Rejects a pending organization invitation

    :param invitation_token: The app invitation token that was sent to the user
    :type invitation_token: str
    :param body: allow empty body for custom http-client lib
    :type body: 

    """
    return web.Response(status=200)


async def org_invitations_send_new_invitation(request: web.Request, org_name, email, body=None) -> web.Response:
    """org_invitations_send_new_invitation

    Cancels an existing organization invitation for the user and sends a new one

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param email: The email address of the user to send the password reset mail to.
    :type email: str
    :param body: The role of the user to be added
    :type body: dict | bytes

    """
    body = AppInvitationsCreateByEmailRequest.from_dict(body)
    return web.Response(status=200)


async def org_invitations_update(request: web.Request, org_name, email, body) -> web.Response:
    """org_invitations_update

    Allows the role of an invited user to be changed

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param email: The email address of the user to send the password reset mail to.
    :type email: str
    :param body: The new role of the user
    :type body: dict | bytes

    """
    body = OrgInvitationsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def organization_delete_avatar(request: web.Request, org_name) -> web.Response:
    """organization_delete_avatar

    Deletes the uploaded organization avatar

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def organization_update_avatar(request: web.Request, org_name, avatar=None) -> web.Response:
    """organization_update_avatar

    Sets the organization avatar

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param avatar: The image for an Organization avatar to upload.
    :type avatar: str

    """
    return web.Response(status=200)


async def organizations_create_or_update(request: web.Request, body) -> web.Response:
    """organizations_create_or_update

    Creates a new organization and returns it to the caller

    :param body: The organization data
    :type body: dict | bytes

    """
    body = OrganizationsCreateOrUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def organizations_delete(request: web.Request, org_name) -> web.Response:
    """organizations_delete

    Deletes a single organization

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def organizations_get(request: web.Request, org_name) -> web.Response:
    """organizations_get

    Returns the details of a single organization

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def organizations_list(request: web.Request, ) -> web.Response:
    """organizations_list

    Returns a list of organizations the requesting user has access to


    """
    return web.Response(status=200)


async def organizations_list_administered(request: web.Request, ) -> web.Response:
    """organizations_list_administered

    Returns a list organizations in which the requesting user is an admin


    """
    return web.Response(status=200)


async def organizations_update(request: web.Request, org_name, body) -> web.Response:
    """organizations_update

    Returns a list of organizations the requesting user has access to

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param body: The data for the org
    :type body: dict | bytes

    """
    body = OrganizationsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def sharedconnection_connections(request: web.Request, ) -> web.Response:
    """sharedconnection_connections

    Gets all service connections of the service type for GDPR export.


    """
    return web.Response(status=200)


async def teams_add_app(request: web.Request, org_name, team_name, body) -> web.Response:
    """teams_add_app

    Adds an app to a team

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str
    :param body: The name of the app to be added to the team. The app has to be owned by the organization.
    :type body: dict | bytes

    """
    body = DistributionGroupsAddAppsRequestAppsInner.from_dict(body)
    return web.Response(status=200)


async def teams_add_user(request: web.Request, org_name, team_name, body) -> web.Response:
    """teams_add_user

    Adds a new user to a team that is owned by an organization

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str
    :param body: The email of the user to add to the team
    :type body: dict | bytes

    """
    body = OrgInvitationsDeleteRequest.from_dict(body)
    return web.Response(status=200)


async def teams_create_team(request: web.Request, org_name, body) -> web.Response:
    """teams_create_team

    Creates a team and returns it

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param body: The information used to create the team
    :type body: dict | bytes

    """
    body = TeamsCreateTeamRequest.from_dict(body)
    return web.Response(status=200)


async def teams_delete(request: web.Request, org_name, team_name) -> web.Response:
    """teams_delete

    Deletes a single team

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str

    """
    return web.Response(status=200)


async def teams_get_team(request: web.Request, org_name, team_name) -> web.Response:
    """teams_get_team

    Returns the details of a single team

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str

    """
    return web.Response(status=200)


async def teams_get_users(request: web.Request, org_name, team_name) -> web.Response:
    """teams_get_users

    Returns the users of a team which is owned by an organization

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str

    """
    return web.Response(status=200)


async def teams_list_all(request: web.Request, org_name) -> web.Response:
    """teams_list_all

    Returns the list of all teams in this org

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def teams_list_apps(request: web.Request, org_name, team_name) -> web.Response:
    """teams_list_apps

    Returns the apps a team has access to

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str

    """
    return web.Response(status=200)


async def teams_remove_app(request: web.Request, org_name, team_name, app_name) -> web.Response:
    """teams_remove_app

    Removes an app from a team

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def teams_remove_user(request: web.Request, org_name, team_name, user_name) -> web.Response:
    """teams_remove_user

    Removes a user from a team that is owned by an organization

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str
    :param user_name: The slug name of the user
    :type user_name: str

    """
    return web.Response(status=200)


async def teams_update(request: web.Request, org_name, team_name, body) -> web.Response:
    """teams_update

    Updates a single team

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str
    :param body: The information used to update the team
    :type body: dict | bytes

    """
    body = TeamsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def teams_update_permissions(request: web.Request, org_name, team_name, app_name, body) -> web.Response:
    """teams_update_permissions

    Updates the permissions the team has to the app

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param team_name: The team&#39;s name
    :type team_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsUpdatePermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def user_api_tokens_delete(request: web.Request, api_token_id) -> web.Response:
    """user_api_tokens_delete

    Delete the user api_token object with the specific id

    :param api_token_id: The unique ID (UUID) of the api token
    :type api_token_id: str

    """
    return web.Response(status=200)


async def user_api_tokens_list(request: web.Request, ) -> web.Response:
    """user_api_tokens_list

    Returns api tokens for the authenticated user


    """
    return web.Response(status=200)


async def user_api_tokens_new(request: web.Request, body=None) -> web.Response:
    """user_api_tokens_new

    Creates a new User API token

    :param body: Description of the token
    :type body: dict | bytes

    """
    body = UserApiTokensNewRequest.from_dict(body)
    return web.Response(status=200)


async def users_get(request: web.Request, ) -> web.Response:
    """users_get

    Returns the user profile data


    """
    return web.Response(status=200)


async def users_get_for_org(request: web.Request, org_name, user_name) -> web.Response:
    """users_get_for_org

    Get a user information from an organization by name - if there is explicit permission return it, if not if not return highest implicit permission

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param user_name: The slug name of the user
    :type user_name: str

    """
    return web.Response(status=200)


async def users_get_user_metadata(request: web.Request, ) -> web.Response:
    """users_get_user_metadata

    


    """
    return web.Response(status=200)


async def users_list(request: web.Request, owner_name, app_name) -> web.Response:
    """users_list

    Returns the users associated with the app specified with the given app name which belongs to the given owner.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def users_list_for_org(request: web.Request, org_name) -> web.Response:
    """users_list_for_org

    Returns a list of users that belong to an organization

    :param org_name: The organization&#39;s name
    :type org_name: str

    """
    return web.Response(status=200)


async def users_remove_from_org(request: web.Request, org_name, user_name) -> web.Response:
    """users_remove_from_org

    Removes a user from an organization.

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param user_name: The slug name of the user
    :type user_name: str

    """
    return web.Response(status=200)


async def users_update(request: web.Request, body) -> web.Response:
    """users_update

    Updates the user profile and returns the updated user data

    :param body: The data for the created user
    :type body: dict | bytes

    """
    body = UsersUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def users_update_org_role(request: web.Request, org_name, user_name, body) -> web.Response:
    """users_update_org_role

    Updates the given organization user

    :param org_name: The organization&#39;s name
    :type org_name: str
    :param user_name: The slug name of the user
    :type user_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrgInvitationsUpdateRequest.from_dict(body)
    return web.Response(status=200)
