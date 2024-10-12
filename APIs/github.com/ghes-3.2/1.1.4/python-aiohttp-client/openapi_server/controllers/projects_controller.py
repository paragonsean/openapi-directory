from typing import List, Dict
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.orgs_update422_response import OrgsUpdate422Response
from openapi_server.models.project import Project
from openapi_server.models.project_card import ProjectCard
from openapi_server.models.project_collaborator_permission import ProjectCollaboratorPermission
from openapi_server.models.project_column import ProjectColumn
from openapi_server.models.projects_add_collaborator_request import ProjectsAddCollaboratorRequest
from openapi_server.models.projects_create_card_request import ProjectsCreateCardRequest
from openapi_server.models.projects_create_for_authenticated_user_request import ProjectsCreateForAuthenticatedUserRequest
from openapi_server.models.projects_create_for_org_request import ProjectsCreateForOrgRequest
from openapi_server.models.projects_delete_card403_response import ProjectsDeleteCard403Response
from openapi_server.models.projects_move_card403_response import ProjectsMoveCard403Response
from openapi_server.models.projects_move_card503_response import ProjectsMoveCard503Response
from openapi_server.models.projects_move_card_request import ProjectsMoveCardRequest
from openapi_server.models.projects_move_column_request import ProjectsMoveColumnRequest
from openapi_server.models.projects_update_card_request import ProjectsUpdateCardRequest
from openapi_server.models.projects_update_column_request import ProjectsUpdateColumnRequest
from openapi_server.models.projects_update_request import ProjectsUpdateRequest
from openapi_server.models.reactions_create_for_commit_comment415_response import ReactionsCreateForCommitComment415Response
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.validation_error_simple import ValidationErrorSimple
from openapi_server import util


async def projects_add_collaborator(request: web.Request, project_id, username, body=None) -> web.Response:
    """Add project collaborator

    Adds a collaborator to an organization project and sets their permission level. You must be an organization owner or a project &#x60;admin&#x60; to add a collaborator.

    :param project_id: The unique identifier of the project.
    :type project_id: int
    :param username: The handle for the GitHub user account.
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsAddCollaboratorRequest.from_dict(body)
    return web.Response(status=200)


async def projects_create_card(request: web.Request, column_id, body) -> web.Response:
    """Create a project card

    

    :param column_id: The unique identifier of the column.
    :type column_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsCreateCardRequest.from_dict(body)
    return web.Response(status=200)


async def projects_create_column(request: web.Request, project_id, body) -> web.Response:
    """Create a project column

    

    :param project_id: The unique identifier of the project.
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsUpdateColumnRequest.from_dict(body)
    return web.Response(status=200)


async def projects_create_for_authenticated_user(request: web.Request, body) -> web.Response:
    """Create a user project

    Creates a user project board. Returns a &#x60;410 Gone&#x60; status if the user does not have existing classic projects. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsCreateForAuthenticatedUserRequest.from_dict(body)
    return web.Response(status=200)


async def projects_create_for_org(request: web.Request, org, body) -> web.Response:
    """Create an organization project

    Creates an organization project board. Returns a &#x60;410 Gone&#x60; status if projects are disabled in the organization or if the organization does not have existing classic projects. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

    :param org: The organization name. The name is not case sensitive.
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsCreateForOrgRequest.from_dict(body)
    return web.Response(status=200)


async def projects_create_for_repo(request: web.Request, owner, repo, body) -> web.Response:
    """Create a repository project

    Creates a repository project board. Returns a &#x60;410 Gone&#x60; status if projects are disabled in the repository or if the repository does not have existing classic projects. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsCreateForOrgRequest.from_dict(body)
    return web.Response(status=200)


async def projects_delete(request: web.Request, project_id) -> web.Response:
    """Delete a project

    Deletes a project board. Returns a &#x60;404 Not Found&#x60; status if projects are disabled.

    :param project_id: The unique identifier of the project.
    :type project_id: int

    """
    return web.Response(status=200)


async def projects_delete_card(request: web.Request, card_id) -> web.Response:
    """Delete a project card

    

    :param card_id: The unique identifier of the card.
    :type card_id: int

    """
    return web.Response(status=200)


async def projects_delete_column(request: web.Request, column_id) -> web.Response:
    """Delete a project column

    

    :param column_id: The unique identifier of the column.
    :type column_id: int

    """
    return web.Response(status=200)


async def projects_get(request: web.Request, project_id) -> web.Response:
    """Get a project

    Gets a project by its &#x60;id&#x60;. Returns a &#x60;404 Not Found&#x60; status if projects are disabled. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

    :param project_id: The unique identifier of the project.
    :type project_id: int

    """
    return web.Response(status=200)


async def projects_get_card(request: web.Request, card_id) -> web.Response:
    """Get a project card

    

    :param card_id: The unique identifier of the card.
    :type card_id: int

    """
    return web.Response(status=200)


async def projects_get_column(request: web.Request, column_id) -> web.Response:
    """Get a project column

    

    :param column_id: The unique identifier of the column.
    :type column_id: int

    """
    return web.Response(status=200)


async def projects_get_permission_for_user(request: web.Request, project_id, username) -> web.Response:
    """Get project permission for a user

    Returns the collaborator&#39;s permission level for an organization project. Possible values for the &#x60;permission&#x60; key: &#x60;admin&#x60;, &#x60;write&#x60;, &#x60;read&#x60;, &#x60;none&#x60;. You must be an organization owner or a project &#x60;admin&#x60; to review a user&#39;s permission level.

    :param project_id: The unique identifier of the project.
    :type project_id: int
    :param username: The handle for the GitHub user account.
    :type username: str

    """
    return web.Response(status=200)


async def projects_list_cards(request: web.Request, column_id, archived_state=None, per_page=None, page=None) -> web.Response:
    """List project cards

    

    :param column_id: The unique identifier of the column.
    :type column_id: int
    :param archived_state: Filters the project cards that are returned by the card&#39;s state.
    :type archived_state: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def projects_list_collaborators(request: web.Request, project_id, affiliation=None, per_page=None, page=None) -> web.Response:
    """List project collaborators

    Lists the collaborators for an organization project. For a project, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. You must be an organization owner or a project &#x60;admin&#x60; to list collaborators.

    :param project_id: The unique identifier of the project.
    :type project_id: int
    :param affiliation: Filters the collaborators by their affiliation. &#x60;outside&#x60; means outside collaborators of a project that are not a member of the project&#39;s organization. &#x60;direct&#x60; means collaborators with permissions to a project, regardless of organization membership status. &#x60;all&#x60; means all collaborators the authenticated user can see.
    :type affiliation: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def projects_list_columns(request: web.Request, project_id, per_page=None, page=None) -> web.Response:
    """List project columns

    

    :param project_id: The unique identifier of the project.
    :type project_id: int
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def projects_list_for_org(request: web.Request, org, state=None, per_page=None, page=None) -> web.Response:
    """List organization projects

    Lists the projects in an organization. Returns a &#x60;404 Not Found&#x60; status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

    :param org: The organization name. The name is not case sensitive.
    :type org: str
    :param state: Indicates the state of the projects to return.
    :type state: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def projects_list_for_repo(request: web.Request, owner, repo, state=None, per_page=None, page=None) -> web.Response:
    """List repository projects

    Lists the projects in a repository. Returns a &#x60;404 Not Found&#x60; status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

    :param owner: The account owner of the repository. The name is not case sensitive.
    :type owner: str
    :param repo: The name of the repository. The name is not case sensitive.
    :type repo: str
    :param state: Indicates the state of the projects to return.
    :type state: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def projects_list_for_user(request: web.Request, username, state=None, per_page=None, page=None) -> web.Response:
    """List user projects

    

    :param username: The handle for the GitHub user account.
    :type username: str
    :param state: Indicates the state of the projects to return.
    :type state: str
    :param per_page: The number of results per page (max 100).
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def projects_move_card(request: web.Request, card_id, body) -> web.Response:
    """Move a project card

    

    :param card_id: The unique identifier of the card.
    :type card_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsMoveCardRequest.from_dict(body)
    return web.Response(status=200)


async def projects_move_column(request: web.Request, column_id, body) -> web.Response:
    """Move a project column

    

    :param column_id: The unique identifier of the column.
    :type column_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsMoveColumnRequest.from_dict(body)
    return web.Response(status=200)


async def projects_remove_collaborator(request: web.Request, project_id, username) -> web.Response:
    """Remove user as a collaborator

    Removes a collaborator from an organization project. You must be an organization owner or a project &#x60;admin&#x60; to remove a collaborator.

    :param project_id: The unique identifier of the project.
    :type project_id: int
    :param username: The handle for the GitHub user account.
    :type username: str

    """
    return web.Response(status=200)


async def projects_update(request: web.Request, project_id, body=None) -> web.Response:
    """Update a project

    Updates a project board&#39;s information. Returns a &#x60;404 Not Found&#x60; status if projects are disabled. If you do not have sufficient privileges to perform this action, a &#x60;401 Unauthorized&#x60; or &#x60;410 Gone&#x60; status is returned.

    :param project_id: The unique identifier of the project.
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def projects_update_card(request: web.Request, card_id, body=None) -> web.Response:
    """Update an existing project card

    

    :param card_id: The unique identifier of the card.
    :type card_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsUpdateCardRequest.from_dict(body)
    return web.Response(status=200)


async def projects_update_column(request: web.Request, column_id, body) -> web.Response:
    """Update an existing project column

    

    :param column_id: The unique identifier of the column.
    :type column_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectsUpdateColumnRequest.from_dict(body)
    return web.Response(status=200)
