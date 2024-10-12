from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.create_hook_option import CreateHookOption
from openapi_server.models.create_label_option import CreateLabelOption
from openapi_server.models.create_org_option import CreateOrgOption
from openapi_server.models.create_repo_option import CreateRepoOption
from openapi_server.models.create_team_option import CreateTeamOption
from openapi_server.models.edit_hook_option import EditHookOption
from openapi_server.models.edit_label_option import EditLabelOption
from openapi_server.models.edit_org_option import EditOrgOption
from openapi_server.models.edit_team_option import EditTeamOption
from openapi_server.models.hook import Hook
from openapi_server.models.label import Label
from openapi_server.models.organization import Organization
from openapi_server.models.organization_permissions import OrganizationPermissions
from openapi_server.models.repository import Repository
from openapi_server.models.team import Team
from openapi_server.models.team_search200_response import TeamSearch200Response
from openapi_server.models.user import User
from openapi_server import util


async def create_org_repo(request: web.Request, org, body=None) -> web.Response:
    """Create a repository in an organization

    

    :param org: name of organization
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateRepoOption.from_dict(body)
    return web.Response(status=200)


async def create_org_repo_deprecated(request: web.Request, org, body=None) -> web.Response:
    """Create a repository in an organization

    

    :param org: name of organization
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateRepoOption.from_dict(body)
    return web.Response(status=200)


async def org_add_team_member(request: web.Request, id, username) -> web.Response:
    """Add a team member

    

    :param id: id of the team
    :type id: int
    :param username: username of the user to add
    :type username: str

    """
    return web.Response(status=200)


async def org_add_team_repository(request: web.Request, id, org, repo) -> web.Response:
    """Add a repository to a team

    

    :param id: id of the team
    :type id: int
    :param org: organization that owns the repo to add
    :type org: str
    :param repo: name of the repo to add
    :type repo: str

    """
    return web.Response(status=200)


async def org_conceal_member(request: web.Request, org, username) -> web.Response:
    """Conceal a user&#39;s membership

    

    :param org: name of the organization
    :type org: str
    :param username: username of the user
    :type username: str

    """
    return web.Response(status=200)


async def org_create(request: web.Request, body) -> web.Response:
    """Create an organization

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrgOption.from_dict(body)
    return web.Response(status=200)


async def org_create_hook(request: web.Request, org, body) -> web.Response:
    """Create a hook

    

    :param org: name of the organization
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateHookOption.from_dict(body)
    return web.Response(status=200)


async def org_create_label(request: web.Request, org, body=None) -> web.Response:
    """Create a label for an organization

    

    :param org: name of the organization
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateLabelOption.from_dict(body)
    return web.Response(status=200)


async def org_create_team(request: web.Request, org, body=None) -> web.Response:
    """Create a team

    

    :param org: name of the organization
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTeamOption.from_dict(body)
    return web.Response(status=200)


async def org_delete(request: web.Request, org) -> web.Response:
    """Delete an organization

    

    :param org: organization that is to be deleted
    :type org: str

    """
    return web.Response(status=200)


async def org_delete_hook(request: web.Request, org, id) -> web.Response:
    """Delete a hook

    

    :param org: name of the organization
    :type org: str
    :param id: id of the hook to delete
    :type id: int

    """
    return web.Response(status=200)


async def org_delete_label(request: web.Request, org, id) -> web.Response:
    """Delete a label

    

    :param org: name of the organization
    :type org: str
    :param id: id of the label to delete
    :type id: int

    """
    return web.Response(status=200)


async def org_delete_member(request: web.Request, org, username) -> web.Response:
    """Remove a member from an organization

    

    :param org: name of the organization
    :type org: str
    :param username: username of the user
    :type username: str

    """
    return web.Response(status=200)


async def org_delete_team(request: web.Request, id) -> web.Response:
    """Delete a team

    

    :param id: id of the team to delete
    :type id: int

    """
    return web.Response(status=200)


async def org_edit(request: web.Request, org, body) -> web.Response:
    """Edit an organization

    

    :param org: name of the organization to edit
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditOrgOption.from_dict(body)
    return web.Response(status=200)


async def org_edit_hook(request: web.Request, org, id, body=None) -> web.Response:
    """Update a hook

    

    :param org: name of the organization
    :type org: str
    :param id: id of the hook to update
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditHookOption.from_dict(body)
    return web.Response(status=200)


async def org_edit_label(request: web.Request, org, id, body=None) -> web.Response:
    """Update a label

    

    :param org: name of the organization
    :type org: str
    :param id: id of the label to edit
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditLabelOption.from_dict(body)
    return web.Response(status=200)


async def org_edit_team(request: web.Request, id, body=None) -> web.Response:
    """Edit a team

    

    :param id: id of the team to edit
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditTeamOption.from_dict(body)
    return web.Response(status=200)


async def org_get(request: web.Request, org) -> web.Response:
    """Get an organization

    

    :param org: name of the organization to get
    :type org: str

    """
    return web.Response(status=200)


async def org_get_all(request: web.Request, page=None, limit=None) -> web.Response:
    """Get list of organizations

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_get_hook(request: web.Request, org, id) -> web.Response:
    """Get a hook

    

    :param org: name of the organization
    :type org: str
    :param id: id of the hook to get
    :type id: int

    """
    return web.Response(status=200)


async def org_get_label(request: web.Request, org, id) -> web.Response:
    """Get a single label

    

    :param org: name of the organization
    :type org: str
    :param id: id of the label to get
    :type id: int

    """
    return web.Response(status=200)


async def org_get_team(request: web.Request, id) -> web.Response:
    """Get a team

    

    :param id: id of the team to get
    :type id: int

    """
    return web.Response(status=200)


async def org_get_user_permissions(request: web.Request, username, org) -> web.Response:
    """Get user permissions in organization

    

    :param username: username of user
    :type username: str
    :param org: name of the organization
    :type org: str

    """
    return web.Response(status=200)


async def org_is_member(request: web.Request, org, username) -> web.Response:
    """Check if a user is a member of an organization

    

    :param org: name of the organization
    :type org: str
    :param username: username of the user
    :type username: str

    """
    return web.Response(status=200)


async def org_is_public_member(request: web.Request, org, username) -> web.Response:
    """Check if a user is a public member of an organization

    

    :param org: name of the organization
    :type org: str
    :param username: username of the user
    :type username: str

    """
    return web.Response(status=200)


async def org_list_activity_feeds(request: web.Request, org, _date=None, page=None, limit=None) -> web.Response:
    """List an organization&#39;s activity feeds

    

    :param org: name of the org
    :type org: str
    :param _date: the date of the activities to be found
    :type _date: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def org_list_current_user_orgs(request: web.Request, page=None, limit=None) -> web.Response:
    """List the current user&#39;s organizations

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_hooks(request: web.Request, org, page=None, limit=None) -> web.Response:
    """List an organization&#39;s webhooks

    

    :param org: name of the organization
    :type org: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_labels(request: web.Request, org, page=None, limit=None) -> web.Response:
    """List an organization&#39;s labels

    

    :param org: name of the organization
    :type org: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_members(request: web.Request, org, page=None, limit=None) -> web.Response:
    """List an organization&#39;s members

    

    :param org: name of the organization
    :type org: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_public_members(request: web.Request, org, page=None, limit=None) -> web.Response:
    """List an organization&#39;s public members

    

    :param org: name of the organization
    :type org: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_repos(request: web.Request, org, page=None, limit=None) -> web.Response:
    """List an organization&#39;s repos

    

    :param org: name of the organization
    :type org: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_team_activity_feeds(request: web.Request, id, _date=None, page=None, limit=None) -> web.Response:
    """List a team&#39;s activity feeds

    

    :param id: id of the team
    :type id: int
    :param _date: the date of the activities to be found
    :type _date: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def org_list_team_member(request: web.Request, id, username) -> web.Response:
    """List a particular member of team

    

    :param id: id of the team
    :type id: int
    :param username: username of the member to list
    :type username: str

    """
    return web.Response(status=200)


async def org_list_team_members(request: web.Request, id, page=None, limit=None) -> web.Response:
    """List a team&#39;s members

    

    :param id: id of the team
    :type id: int
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_team_repo(request: web.Request, id, org, repo) -> web.Response:
    """List a particular repo of team

    

    :param id: id of the team
    :type id: int
    :param org: organization that owns the repo to list
    :type org: str
    :param repo: name of the repo to list
    :type repo: str

    """
    return web.Response(status=200)


async def org_list_team_repos(request: web.Request, id, page=None, limit=None) -> web.Response:
    """List a team&#39;s repos

    

    :param id: id of the team
    :type id: int
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_teams(request: web.Request, org, page=None, limit=None) -> web.Response:
    """List an organization&#39;s teams

    

    :param org: name of the organization
    :type org: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_list_user_orgs(request: web.Request, username, page=None, limit=None) -> web.Response:
    """List a user&#39;s organizations

    

    :param username: username of user
    :type username: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def org_publicize_member(request: web.Request, org, username) -> web.Response:
    """Publicize a user&#39;s membership

    

    :param org: name of the organization
    :type org: str
    :param username: username of the user
    :type username: str

    """
    return web.Response(status=200)


async def org_remove_team_member(request: web.Request, id, username) -> web.Response:
    """Remove a team member

    

    :param id: id of the team
    :type id: int
    :param username: username of the user to remove
    :type username: str

    """
    return web.Response(status=200)


async def org_remove_team_repository(request: web.Request, id, org, repo) -> web.Response:
    """Remove a repository from a team

    This does not delete the repository, it only removes the repository from the team.

    :param id: id of the team
    :type id: int
    :param org: organization that owns the repo to remove
    :type org: str
    :param repo: name of the repo to remove
    :type repo: str

    """
    return web.Response(status=200)


async def team_search(request: web.Request, org, q=None, include_desc=None, page=None, limit=None) -> web.Response:
    """Search for teams within an organization

    

    :param org: name of the organization
    :type org: str
    :param q: keywords to search
    :type q: str
    :param include_desc: include search within team description (defaults to true)
    :type include_desc: bool
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)
