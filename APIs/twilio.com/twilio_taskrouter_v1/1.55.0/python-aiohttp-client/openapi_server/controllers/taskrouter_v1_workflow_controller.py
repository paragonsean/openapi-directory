from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_workflow_response import ListWorkflowResponse
from openapi_server.models.taskrouter_v1_workspace_workflow import TaskrouterV1WorkspaceWorkflow
from openapi_server import util


async def create_workflow(request: web.Request, workspace_sid, configuration, friendly_name, assignment_callback_url=None, fallback_assignment_callback_url=None, task_reservation_timeout=None) -> web.Response:
    """create_workflow

    

    :param workspace_sid: The SID of the Workspace that the new Workflow to create belongs to.
    :type workspace_sid: str
    :param configuration: A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information.
    :type configuration: str
    :param friendly_name: A descriptive string that you create to describe the Workflow resource. For example, &#x60;Inbound Call Workflow&#x60; or &#x60;2014 Outbound Campaign&#x60;.
    :type friendly_name: str
    :param assignment_callback_url: The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details.
    :type assignment_callback_url: str
    :param fallback_assignment_callback_url: The URL that we should call when a call to the &#x60;assignment_callback_url&#x60; fails.
    :type fallback_assignment_callback_url: str
    :param task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to &#x60;86,400&#x60; (24 hours) and the default is &#x60;120&#x60;.
    :type task_reservation_timeout: int

    """
    return web.Response(status=200)


async def delete_workflow(request: web.Request, workspace_sid, sid) -> web.Response:
    """delete_workflow

    

    :param workspace_sid: The SID of the Workspace with the Workflow to delete.
    :type workspace_sid: str
    :param sid: The SID of the Workflow resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_workflow(request: web.Request, workspace_sid, sid) -> web.Response:
    """fetch_workflow

    

    :param workspace_sid: The SID of the Workspace with the Workflow to fetch.
    :type workspace_sid: str
    :param sid: The SID of the Workflow resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_workflow(request: web.Request, workspace_sid, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_workflow

    

    :param workspace_sid: The SID of the Workspace with the Workflow to read.
    :type workspace_sid: str
    :param friendly_name: The &#x60;friendly_name&#x60; of the Workflow resources to read.
    :type friendly_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_workflow(request: web.Request, workspace_sid, sid, assignment_callback_url=None, configuration=None, fallback_assignment_callback_url=None, friendly_name=None, re_evaluate_tasks=None, task_reservation_timeout=None) -> web.Response:
    """update_workflow

    

    :param workspace_sid: The SID of the Workspace with the Workflow to update.
    :type workspace_sid: str
    :param sid: The SID of the Workflow resource to update.
    :type sid: str
    :param assignment_callback_url: The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details.
    :type assignment_callback_url: str
    :param configuration: A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information.
    :type configuration: str
    :param fallback_assignment_callback_url: The URL that we should call when a call to the &#x60;assignment_callback_url&#x60; fails.
    :type fallback_assignment_callback_url: str
    :param friendly_name: A descriptive string that you create to describe the Workflow resource. For example, &#x60;Inbound Call Workflow&#x60; or &#x60;2014 Outbound Campaign&#x60;.
    :type friendly_name: str
    :param re_evaluate_tasks: Whether or not to re-evaluate Tasks. The default is &#x60;false&#x60;, which means Tasks in the Workflow will not be processed through the assignment loop again.
    :type re_evaluate_tasks: str
    :param task_reservation_timeout: How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to &#x60;86,400&#x60; (24 hours) and the default is &#x60;120&#x60;.
    :type task_reservation_timeout: int

    """
    return web.Response(status=200)
