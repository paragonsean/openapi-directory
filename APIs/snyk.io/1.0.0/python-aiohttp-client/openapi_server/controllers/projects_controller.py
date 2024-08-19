from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_a_tag_to_a_project200_response import AddATagToAProject200Response
from openapi_server.models.add_a_tag_to_a_project_request import AddATagToAProjectRequest
from openapi_server.models.add_ignore_request import AddIgnoreRequest
from openapi_server.models.applying_attributes200_response import ApplyingAttributes200Response
from openapi_server.models.applying_attributes_request import ApplyingAttributesRequest
from openapi_server.models.create_jira_issue200_response import CreateJiraIssue200Response
from openapi_server.models.create_jira_issue_request import CreateJiraIssueRequest
from openapi_server.models.get_project_dependency_graph200_response import GetProjectDependencyGraph200Response
from openapi_server.models.list_all_aggregated_issues200_response import ListAllAggregatedIssues200Response
from openapi_server.models.list_all_aggregated_issues_request import ListAllAggregatedIssuesRequest
from openapi_server.models.list_all_project_snapshot_issue_paths200_response import ListAllProjectSnapshotIssuePaths200Response
from openapi_server.models.list_all_project_snapshots200_response import ListAllProjectSnapshots200Response
from openapi_server.models.list_all_project_snapshots_request import ListAllProjectSnapshotsRequest
from openapi_server.models.list_all_projects200_response import ListAllProjects200Response
from openapi_server.models.list_all_projects_request import ListAllProjectsRequest
from openapi_server.models.list_project_settings200_response import ListProjectSettings200Response
from openapi_server.models.move_project_to_a_different_organization_request import MoveProjectToADifferentOrganizationRequest
from openapi_server.models.retrieve_a_single_project200_response import RetrieveASingleProject200Response
from openapi_server.models.update_a_project_request import UpdateAProjectRequest
from openapi_server.models.update_project_settings_request import UpdateProjectSettingsRequest
from openapi_server import util


async def activate(request: web.Request, org_id, project_id) -> web.Response:
    """Activate

    Activating a project will:  - Add a repository webhook for supported integrations.  - Enable pull request tests for new vulnerabilities.  - Open Fix pull request for newly disclosed vulnerabilities.  - Enable recurring tests, sending email alerts about newly disclosed vulnerabilities.

    :param org_id: The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID.
    :type project_id: str

    """
    return web.Response(status=200)


async def add_a_tag_to_a_project(request: web.Request, org_id, project_id, body=None) -> web.Response:
    """Add a tag to a project

    ​

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to apply the tag to
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddATagToAProjectRequest.from_dict(body)
    return web.Response(status=200)


async def add_ignore(request: web.Request, org_id, project_id, issue_id, body=None) -> web.Response:
    """Add ignore

    

    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str
    :param issue_id: Automatically added
    :type issue_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddIgnoreRequest.from_dict(body)
    return web.Response(status=200)


async def applying_attributes(request: web.Request, org_id, project_id, body=None) -> web.Response:
    """Applying attributes

    Applies an attribute to the provided project. It is possible to assign multiple values to each attribute, but you can only assign values to one of the predefined attribute categories, using the predefined options for this category. Assigning an attribute requires the caller to be either an Organization Administrator or a Group Administrator. Assigning an attribute will override any existing values that the specific attribute already has set. In order to clear out an attribute value, an empty array can be set.

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to remove a tag from
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApplyingAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def create_jira_issue(request: web.Request, issue_id, org_id, project_id, body=None) -> web.Response:
    """Create jira issue

    

    :param issue_id: The issue ID to create Jira issue for.
    :type issue_id: str
    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateJiraIssueRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate(request: web.Request, org_id, project_id) -> web.Response:
    """Deactivate

    Deactivating a project will:  - Disable pull request tests for new vulnerabilities.  - Disable Fix pull request from being opened for newly disclosed vulnerabilities.  - Disable recurring tests - email alerts about newly disclosed vulnerabilities will be turned off.  - If the repository has no other active projects, then remove any webhooks related to the project.

    :param org_id: The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID.
    :type project_id: str

    """
    return web.Response(status=200)


async def delete_a_project(request: web.Request, org_id, project_id) -> web.Response:
    """Delete a project

    

    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str

    """
    return web.Response(status=200)


async def delete_ignores(request: web.Request, org_id, project_id, issue_id) -> web.Response:
    """Delete ignores

    

    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str
    :param issue_id: Automatically added
    :type issue_id: str

    """
    return web.Response(status=200)


async def delete_project_settings(request: web.Request, org_id, project_id) -> web.Response:
    """Delete project settings

    Deleting project settings will set the project to inherit default settings from its integration.

    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str

    """
    return web.Response(status=200)


async def get_project_dependency_graph(request: web.Request, org_id, project_id) -> web.Response:
    """Get Project dependency graph

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to return issues for.
    :type project_id: str

    """
    return web.Response(status=200)


async def list_all_aggregated_issues(request: web.Request, org_id, project_id, body=None) -> web.Response:
    """List all Aggregated issues

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to return issues for.
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListAllAggregatedIssuesRequest.from_dict(body)
    return web.Response(status=200)


async def list_all_ignores(request: web.Request, org_id, project_id) -> web.Response:
    """List all ignores

    Temporary ignores include an &#x60;expires&#x60; attribute, while permanent ignores do not.

    :param org_id: The organization ID to list ignores for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to list ignores for.
    :type project_id: str

    """
    return web.Response(status=200)


async def list_all_jira_issues(request: web.Request, org_id, project_id) -> web.Response:
    """List all jira issues

    

    :param org_id: The organization ID to list Jira issues for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to list Jira issues for.
    :type project_id: str

    """
    return web.Response(status=200)


async def list_all_project_issue_paths(request: web.Request, org_id, project_id, issue_id, snapshot_id=None, per_page=None, page=None) -> web.Response:
    """List all project issue paths

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID for which to return issue paths.
    :type project_id: str
    :param issue_id: The issue ID for which to return issue paths.
    :type issue_id: str
    :param snapshot_id: The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this.
    :type snapshot_id: str
    :param per_page: The number of results to return per page (1 - 1000, inclusive).
    :type per_page: 
    :param page: The page of results to return.
    :type page: 

    """
    return web.Response(status=200)


async def list_all_project_snapshot_aggregated_issues(request: web.Request, org_id, project_id, snapshot_id, body=None) -> web.Response:
    """List all project snapshot aggregated issues

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID.
    :type project_id: str
    :param snapshot_id: The snapshot ID. If set to latest, the most recent snapshot will be used.
    :type snapshot_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListAllAggregatedIssuesRequest.from_dict(body)
    return web.Response(status=200)


async def list_all_project_snapshot_issue_paths(request: web.Request, org_id, project_id, snapshot_id, issue_id, per_page=None, page=None) -> web.Response:
    """List all project snapshot issue paths

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID for which to return issue paths.
    :type project_id: str
    :param snapshot_id: The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this.
    :type snapshot_id: str
    :param issue_id: The issue ID for which to return issue paths.
    :type issue_id: str
    :param per_page: The number of results to return per page (1 - 1000, inclusive).
    :type per_page: 
    :param page: The page of results to return.
    :type page: 

    """
    return web.Response(status=200)


async def list_all_project_snapshots(request: web.Request, org_id, project_id, per_page=None, page=None, body=None) -> web.Response:
    """List all project snapshots

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to return snapshots for.
    :type project_id: str
    :param per_page: The number of results to return (the default is 10, the maximum is 100).
    :type per_page: 
    :param page: The offset from which to start returning results from.
    :type page: 
    :param body: 
    :type body: dict | bytes

    """
    body = ListAllProjectSnapshotsRequest.from_dict(body)
    return web.Response(status=200)


async def list_all_projects(request: web.Request, org_id, body=None) -> web.Response:
    """List all projects

    

    :param org_id: The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListAllProjectsRequest.from_dict(body)
    return web.Response(status=200)


async def list_project_settings(request: web.Request, org_id, project_id) -> web.Response:
    """List project settings

    

    :param org_id: The organization ID to which the project belongs. The API_KEY must have access to this organization.
    :type org_id: str
    :param project_id: The project ID
    :type project_id: str

    """
    return web.Response(status=200)


async def move_project_to_a_different_organization(request: web.Request, org_id, project_id, body=None) -> web.Response:
    """Move project to a different organization

    Note: when moving a project to a new organization, the historical data used for reporting does not move with it.

    :param org_id: The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed.
    :type org_id: str
    :param project_id: The project ID.
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveProjectToADifferentOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def remove_a_tag_from_a_project(request: web.Request, org_id, project_id, body=None) -> web.Response:
    """Remove a tag from a project

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to remove a tag from
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddATagToAProjectRequest.from_dict(body)
    return web.Response(status=200)


async def replace_ignores(request: web.Request, org_id, project_id, issue_id) -> web.Response:
    """Replace ignores

    

    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str
    :param issue_id: Automatically added
    :type issue_id: str

    """
    return web.Response(status=200)


async def retrieve_a_single_project(request: web.Request, org_id, project_id) -> web.Response:
    """Retrieve a single project

    

    :param org_id: The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID.
    :type project_id: str

    """
    return web.Response(status=200)


async def retrieve_ignore(request: web.Request, org_id, project_id, issue_id) -> web.Response:
    """Retrieve ignore

    

    :param org_id: The organization ID to modify ignores for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param project_id: The project ID to modify ignores for.
    :type project_id: str
    :param issue_id: The issue ID to modify ignores for. Can be a vulnerability or a license Issue.
    :type issue_id: str

    """
    return web.Response(status=200)


async def update_a_project(request: web.Request, org_id, project_id, body=None) -> web.Response:
    """Update a project

    

    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAProjectRequest.from_dict(body)
    return web.Response(status=200)


async def update_project_settings(request: web.Request, org_id, project_id, body=None) -> web.Response:
    """Update project settings

    

    :param org_id: Automatically added
    :type org_id: str
    :param project_id: Automatically added
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateProjectSettingsRequest.from_dict(body)
    return web.Response(status=200)
