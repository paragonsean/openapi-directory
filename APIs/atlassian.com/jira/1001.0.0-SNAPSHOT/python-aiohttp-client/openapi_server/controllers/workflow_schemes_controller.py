from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_workflow import DefaultWorkflow
from openapi_server.models.issue_type_workflow_mapping import IssueTypeWorkflowMapping
from openapi_server.models.issue_types_workflow_mapping import IssueTypesWorkflowMapping
from openapi_server.models.page_bean_workflow_scheme import PageBeanWorkflowScheme
from openapi_server.models.workflow_scheme import WorkflowScheme
from openapi_server import util


async def create_workflow_scheme(request: web.Request, body) -> web.Response:
    """Create workflow scheme

    Creates a workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = WorkflowScheme.from_dict(body)
    return web.Response(status=200)


async def delete_default_workflow(request: web.Request, id, update_draft_if_needed=None) -> web.Response:
    """Delete default workflow

    Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira&#39;s system workflow (the *jira* workflow).  Note that active workflow schemes cannot be edited. If the workflow scheme is active, set &#x60;updateDraftIfNeeded&#x60; to &#x60;true&#x60; and a draft workflow scheme is created or updated with the default workflow reset. The draft workflow scheme can be published in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param update_draft_if_needed: Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to &#x60;false&#x60;.
    :type update_draft_if_needed: bool

    """
    return web.Response(status=200)


async def delete_workflow_mapping(request: web.Request, id, workflow_name, update_draft_if_needed=None) -> web.Response:
    """Delete issue types for workflow in workflow scheme

    Deletes the workflow-issue type mapping for a workflow in a workflow scheme.  Note that active workflow schemes cannot be edited. If the workflow scheme is active, set &#x60;updateDraftIfNeeded&#x60; to &#x60;true&#x60; and a draft workflow scheme is created or updated with the workflow-issue type mapping deleted. The draft workflow scheme can be published in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param workflow_name: The name of the workflow.
    :type workflow_name: str
    :param update_draft_if_needed: Set to true to create or update the draft of a workflow scheme and delete the mapping from the draft, when the workflow scheme cannot be edited. Defaults to &#x60;false&#x60;.
    :type update_draft_if_needed: bool

    """
    return web.Response(status=200)


async def delete_workflow_scheme(request: web.Request, id) -> web.Response:
    """Delete workflow scheme

    Deletes a workflow scheme. Note that a workflow scheme cannot be deleted if it is active (that is, being used by at least one project).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as &#x60;schemeId&#x60;. For example, *schemeId&#x3D;10301*.
    :type id: int

    """
    return web.Response(status=200)


async def delete_workflow_scheme_issue_type(request: web.Request, id, issue_type, update_draft_if_needed=None) -> web.Response:
    """Delete workflow for issue type in workflow scheme

    Deletes the issue type-workflow mapping for an issue type in a workflow scheme.  Note that active workflow schemes cannot be edited. If the workflow scheme is active, set &#x60;updateDraftIfNeeded&#x60; to &#x60;true&#x60; and a draft workflow scheme is created or updated with the issue type-workflow mapping deleted. The draft workflow scheme can be published in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param issue_type: The ID of the issue type.
    :type issue_type: str
    :param update_draft_if_needed: Set to true to create or update the draft of a workflow scheme and update the mapping in the draft, when the workflow scheme cannot be edited. Defaults to &#x60;false&#x60;.
    :type update_draft_if_needed: bool

    """
    return web.Response(status=200)


async def get_all_workflow_schemes(request: web.Request, start_at=None, max_results=None) -> web.Response:
    """Get all workflow schemes

    Returns a [paginated](#pagination) list of all workflow schemes, not including draft workflow schemes.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_default_workflow(request: web.Request, id, return_draft_if_exists=None) -> web.Response:
    """Get default workflow

    Returns the default workflow for a workflow scheme. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param return_draft_if_exists: Set to &#x60;true&#x60; to return the default workflow for the workflow scheme&#39;s draft rather than scheme itself. If the workflow scheme does not have a draft, then the default workflow for the workflow scheme is returned.
    :type return_draft_if_exists: bool

    """
    return web.Response(status=200)


async def get_workflow(request: web.Request, id, workflow_name=None, return_draft_if_exists=None) -> web.Response:
    """Get issue types for workflows in workflow scheme

    Returns the workflow-issue type mappings for a workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param workflow_name: The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.
    :type workflow_name: str
    :param return_draft_if_exists: Returns the mapping from the workflow scheme&#39;s draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned.
    :type return_draft_if_exists: bool

    """
    return web.Response(status=200)


async def get_workflow_scheme(request: web.Request, id, return_draft_if_exists=None) -> web.Response:
    """Get workflow scheme

    Returns a workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as &#x60;schemeId&#x60;. For example, *schemeId&#x3D;10301*.
    :type id: int
    :param return_draft_if_exists: Returns the workflow scheme&#39;s draft rather than scheme itself, if set to true. If the workflow scheme does not have a draft, then the workflow scheme is returned.
    :type return_draft_if_exists: bool

    """
    return web.Response(status=200)


async def get_workflow_scheme_issue_type(request: web.Request, id, issue_type, return_draft_if_exists=None) -> web.Response:
    """Get workflow for issue type in workflow scheme

    Returns the issue type-workflow mapping for an issue type in a workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param issue_type: The ID of the issue type.
    :type issue_type: str
    :param return_draft_if_exists: Returns the mapping from the workflow scheme&#39;s draft rather than the workflow scheme, if set to true. If no draft exists, the mapping from the workflow scheme is returned.
    :type return_draft_if_exists: bool

    """
    return web.Response(status=200)


async def set_workflow_scheme_issue_type(request: web.Request, id, issue_type, body) -> web.Response:
    """Set workflow for issue type in workflow scheme

    Sets the workflow for an issue type in a workflow scheme.  Note that active workflow schemes cannot be edited. If the workflow scheme is active, set &#x60;updateDraftIfNeeded&#x60; to &#x60;true&#x60; in the request body and a draft workflow scheme is created or updated with the new issue type-workflow mapping. The draft workflow scheme can be published in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param issue_type: The ID of the issue type.
    :type issue_type: str
    :param body: The issue type-project mapping.
    :type body: dict | bytes

    """
    body = IssueTypeWorkflowMapping.from_dict(body)
    return web.Response(status=200)


async def update_default_workflow(request: web.Request, id, body) -> web.Response:
    """Update default workflow

    Sets the default workflow for a workflow scheme.  Note that active workflow schemes cannot be edited. If the workflow scheme is active, set &#x60;updateDraftIfNeeded&#x60; to &#x60;true&#x60; in the request object and a draft workflow scheme is created or updated with the new default workflow. The draft workflow scheme can be published in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param body: The new default workflow.
    :type body: dict | bytes

    """
    body = DefaultWorkflow.from_dict(body)
    return web.Response(status=200)


async def update_workflow_mapping(request: web.Request, id, workflow_name, body) -> web.Response:
    """Set issue types for workflow in workflow scheme

    Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow.  Note that active workflow schemes cannot be edited. If the workflow scheme is active, set &#x60;updateDraftIfNeeded&#x60; to &#x60;true&#x60; in the request body and a draft workflow scheme is created or updated with the new workflow-issue types mappings. The draft workflow scheme can be published in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme.
    :type id: int
    :param workflow_name: The name of the workflow.
    :type workflow_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypesWorkflowMapping.from_dict(body)
    return web.Response(status=200)


async def update_workflow_scheme(request: web.Request, id, body) -> web.Response:
    """Update workflow scheme

    Updates a workflow scheme, including the name, default workflow, issue type to project mappings, and more. If the workflow scheme is active (that is, being used by at least one project), then a draft workflow scheme is created or updated instead, provided that &#x60;updateDraftIfNeeded&#x60; is set to &#x60;true&#x60;.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme. Find this ID by editing the desired workflow scheme in Jira. The ID is shown in the URL as &#x60;schemeId&#x60;. For example, *schemeId&#x3D;10301*.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WorkflowScheme.from_dict(body)
    return web.Response(status=200)
