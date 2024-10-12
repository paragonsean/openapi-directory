from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_of_workflow_scheme_associations import ContainerOfWorkflowSchemeAssociations
from openapi_server.models.workflow_scheme_project_association import WorkflowSchemeProjectAssociation
from openapi_server import util


async def assign_scheme_to_project(request: web.Request, body) -> web.Response:
    """Assign workflow scheme to project

    Assigns a workflow scheme to a project. This operation is performed only when there are no issues in the project.  Workflow schemes can only be assigned to classic projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = WorkflowSchemeProjectAssociation.from_dict(body)
    return web.Response(status=200)


async def get_workflow_scheme_project_associations(request: web.Request, project_id) -> web.Response:
    """Get workflow scheme project associations

    Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. Any team-managed or non-existent projects in the request are ignored and no errors are returned.  If the project is associated with the &#x60;Default Workflow Scheme&#x60; no ID is returned. This is because the way the &#x60;Default Workflow Scheme&#x60; is stored means it has no ID.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id: The ID of a project to return the workflow schemes for. To include multiple projects, provide an ampersand-Jim: oneseparated list. For example, &#x60;projectId&#x3D;10000&amp;projectId&#x3D;10001&#x60;.
    :type project_id: List[int]

    """
    return web.Response(status=200)
