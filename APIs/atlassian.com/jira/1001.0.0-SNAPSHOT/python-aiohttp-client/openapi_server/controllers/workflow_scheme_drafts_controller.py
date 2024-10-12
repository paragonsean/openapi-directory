from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_workflow import DefaultWorkflow
from openapi_server.models.issue_type_workflow_mapping import IssueTypeWorkflowMapping
from openapi_server.models.issue_types_workflow_mapping import IssueTypesWorkflowMapping
from openapi_server.models.publish_draft_workflow_scheme import PublishDraftWorkflowScheme
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.workflow_scheme import WorkflowScheme
from openapi_server import util


async def create_workflow_scheme_draft_from_parent(request: web.Request, id) -> web.Response:
    """Create draft workflow scheme

    Create a draft workflow scheme from an active workflow scheme, by copying the active workflow scheme. Note that an active workflow scheme can only have one draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the active workflow scheme that the draft is created from.
    :type id: int

    """
    return web.Response(status=200)


async def delete_draft_default_workflow(request: web.Request, id) -> web.Response:
    """Delete draft default workflow

    Resets the default workflow for a workflow scheme&#39;s draft. That is, the default workflow is set to Jira&#39;s system workflow (the *jira* workflow).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int

    """
    return web.Response(status=200)


async def delete_draft_workflow_mapping(request: web.Request, id, workflow_name) -> web.Response:
    """Delete issue types for workflow in draft workflow scheme

    Deletes the workflow-issue type mapping for a workflow in a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int
    :param workflow_name: The name of the workflow.
    :type workflow_name: str

    """
    return web.Response(status=200)


async def delete_workflow_scheme_draft(request: web.Request, id) -> web.Response:
    """Delete draft workflow scheme

    Deletes a draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the active workflow scheme that the draft was created from.
    :type id: int

    """
    return web.Response(status=200)


async def delete_workflow_scheme_draft_issue_type(request: web.Request, id, issue_type) -> web.Response:
    """Delete workflow for issue type in draft workflow scheme

    Deletes the issue type-workflow mapping for an issue type in a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int
    :param issue_type: The ID of the issue type.
    :type issue_type: str

    """
    return web.Response(status=200)


async def get_draft_default_workflow(request: web.Request, id) -> web.Response:
    """Get draft default workflow

    Returns the default workflow for a workflow scheme&#39;s draft. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int

    """
    return web.Response(status=200)


async def get_draft_workflow(request: web.Request, id, workflow_name=None) -> web.Response:
    """Get issue types for workflows in draft workflow scheme

    Returns the workflow-issue type mappings for a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int
    :param workflow_name: The name of a workflow in the scheme. Limits the results to the workflow-issue type mapping for the specified workflow.
    :type workflow_name: str

    """
    return web.Response(status=200)


async def get_workflow_scheme_draft(request: web.Request, id) -> web.Response:
    """Get draft workflow scheme

    Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. The draft is modified, then the changes in the draft are copied back to the active workflow scheme. See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.   Note that:   *  Only active workflow schemes can have draft workflow schemes.  *  An active workflow scheme can only have one draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the active workflow scheme that the draft was created from.
    :type id: int

    """
    return web.Response(status=200)


async def get_workflow_scheme_draft_issue_type(request: web.Request, id, issue_type) -> web.Response:
    """Get workflow for issue type in draft workflow scheme

    Returns the issue type-workflow mapping for an issue type in a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int
    :param issue_type: The ID of the issue type.
    :type issue_type: str

    """
    return web.Response(status=200)


async def publish_draft_workflow_scheme(request: web.Request, id, body, validate_only=None) -> web.Response:
    """Publish draft workflow scheme

    Publishes a draft workflow scheme.  Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to update issues with the original workflow status to the new workflow status.  This operation is [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int
    :param body: Details of the status mappings.
    :type body: dict | bytes
    :param validate_only: Whether the request only performs a validation.
    :type validate_only: bool

    """
    body = PublishDraftWorkflowScheme.from_dict(body)
    return web.Response(status=200)


async def set_workflow_scheme_draft_issue_type(request: web.Request, id, issue_type, body) -> web.Response:
    """Set workflow for issue type in draft workflow scheme

    Sets the workflow for an issue type in a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int
    :param issue_type: The ID of the issue type.
    :type issue_type: str
    :param body: The issue type-project mapping.
    :type body: dict | bytes

    """
    body = IssueTypeWorkflowMapping.from_dict(body)
    return web.Response(status=200)


async def update_draft_default_workflow(request: web.Request, id, body) -> web.Response:
    """Update draft default workflow

    Sets the default workflow for a workflow scheme&#39;s draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int
    :param body: The object for the new default workflow.
    :type body: dict | bytes

    """
    body = DefaultWorkflow.from_dict(body)
    return web.Response(status=200)


async def update_draft_workflow_mapping(request: web.Request, id, workflow_name, body) -> web.Response:
    """Set issue types for workflow in workflow scheme

    Sets the issue types for a workflow in a workflow scheme&#39;s draft. The workflow can also be set as the default workflow for the draft workflow scheme. Unmapped issues types are mapped to the default workflow.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the workflow scheme that the draft belongs to.
    :type id: int
    :param workflow_name: The name of the workflow.
    :type workflow_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypesWorkflowMapping.from_dict(body)
    return web.Response(status=200)


async def update_workflow_scheme_draft(request: web.Request, id, body) -> web.Response:
    """Update draft workflow scheme

    Updates a draft workflow scheme. If a draft workflow scheme does not exist for the active workflow scheme, then a draft is created. Note that an active workflow scheme can only have one draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the active workflow scheme that the draft was created from.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WorkflowScheme.from_dict(body)
    return web.Response(status=200)
