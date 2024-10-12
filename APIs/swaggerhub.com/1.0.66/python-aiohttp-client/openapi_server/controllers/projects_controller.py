from typing import List, Dict
from aiohttp import web

from openapi_server.models.project import Project
from openapi_server.models.project_member_list import ProjectMemberList
from openapi_server.models.projects_json import ProjectsJson
from openapi_server import util


async def add_spec_to_project_v2(request: web.Request, owner, project_id, spec_type, name) -> web.Response:
    """Add an API or domain to a project

    Use this operation to add a single API or domain to the specified project.  To add multiple APIs or domains at once, use &#x60;PUT /projects/{owner}/{projectId}&#x60;.

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param project_id: Project name (case-sensitive)
    :type project_id: str
    :param spec_type: Definition type - &#x60;apis&#x60; or &#x60;domains&#x60;.
    :type spec_type: str
    :param name: The name of an API or domain that you want to add to the project. Case-sensitive.
    :type name: str

    """
    return web.Response(status=200)


async def create_project(request: web.Request, owner, project_request) -> web.Response:
    """Create a project in an organization

    

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param project_request: The project data. Properties that are not provided are set to empty values. 
    :type project_request: dict | bytes

    """
    project_request = Project.from_dict(project_request)
    return web.Response(status=200)


async def delete_project_v2(request: web.Request, owner, project_id) -> web.Response:
    """Delete a project

    

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param project_id: Project name (case-sensitive)
    :type project_id: str

    """
    return web.Response(status=200)


async def get_org_projects_v2(request: web.Request, owner, name_only=None, page=None, limit=None, order=None) -> web.Response:
    """Get all projects of an organization

    

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param name_only: Return the project information excluding APIs and domains
    :type name_only: bool
    :param page: Page to return
    :type page: int
    :param limit: Number of results per page (1 .. 100)
    :type limit: int
    :param order: Sort order
    :type order: str

    """
    return web.Response(status=200)


async def get_project_members_v2(request: web.Request, owner, project_id) -> web.Response:
    """Get project members

    

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param project_id: Project name (case-sensitive)
    :type project_id: str

    """
    return web.Response(status=200)


async def get_project_v2(request: web.Request, owner, project_id) -> web.Response:
    """Get project information

    

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param project_id: Project name (case-sensitive)
    :type project_id: str

    """
    return web.Response(status=200)


async def get_user_projects(request: web.Request, name_only=None, page=None, limit=None, sort=None, order=None) -> web.Response:
    """Get all projects that a user has access to

    Returns all projects that the authenticating user has access to. Organization owners get a list of all projects in owned organizations. Other members get a list of just the projects they are member of.

    :param name_only: Return the project information excluding APIs and domains
    :type name_only: bool
    :param page: Page to return
    :type page: int
    :param limit: Number of results per page (1 .. 100)
    :type limit: int
    :param sort: Sort criteria or result set: * NAME * OWNER 
    :type sort: str
    :param order: Sort order
    :type order: str

    """
    return web.Response(status=200)


async def save_project_v2(request: web.Request, owner, project_id, project_request) -> web.Response:
    """Update a project

    Use this operation to update an existing project, for example, add or remove APIs, or change the project description.  When updating a project, the &#x60;apis&#x60; and &#x60;domains&#x60; lists _replace_ the existing ones. This means that to add new APIs and domains to a project, you need to send the &#x60;apis&#x60; and &#x60;domains&#x60; lists containing both the existing and new APIs and domains.  To add a single API or domain to a project, you can use &#x60;PUT /projects/{owner}/{projectId}/{specType}/{name}&#x60; instead.

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param project_id: Project name (case-sensitive)
    :type project_id: str
    :param project_request: The project data. Properties that are not provided are set to empty values. 
    :type project_request: dict | bytes

    """
    project_request = Project.from_dict(project_request)
    return web.Response(status=200)


async def update_project_members_v2(request: web.Request, owner, project_id, project_member_list) -> web.Response:
    """Update a project&#39;s members list

    When updating a project, the &#x60;members&#x60; list _replaces_ the existing one. This means that to add new members to a project, you need to send the &#x60;members&#x60; list containing both the existing and new members. 

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param project_id: Project name (case-sensitive)
    :type project_id: str
    :param project_member_list: A list of users and teams to add to the project
    :type project_member_list: dict | bytes

    """
    project_member_list = ProjectMemberList.from_dict(project_member_list)
    return web.Response(status=200)
