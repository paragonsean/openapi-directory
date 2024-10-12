from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def workflows_step_completed(request: web.Request, token, workflow_step_execute_id, outputs=None) -> web.Response:
    """workflows_step_completed

    Indicate that an app&#39;s step in a workflow completed execution.

    :param token: Authentication token. Requires scope: &#x60;workflow.steps:execute&#x60;
    :type token: str
    :param workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
    :type workflow_step_execute_id: str
    :param outputs: Key-value object of outputs from your step. Keys of this object reflect the configured &#x60;key&#x60; properties of your [&#x60;outputs&#x60;](/reference/workflows/workflow_step#output) array from your &#x60;workflow_step&#x60; object.
    :type outputs: str

    """
    return web.Response(status=200)


async def workflows_step_failed(request: web.Request, token, workflow_step_execute_id, error) -> web.Response:
    """workflows_step_failed

    Indicate that an app&#39;s step in a workflow failed to execute.

    :param token: Authentication token. Requires scope: &#x60;workflow.steps:execute&#x60;
    :type token: str
    :param workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
    :type workflow_step_execute_id: str
    :param error: A JSON-based object with a &#x60;message&#x60; property that should contain a human readable error message.
    :type error: str

    """
    return web.Response(status=200)


async def workflows_update_step(request: web.Request, token, workflow_step_edit_id, inputs=None, outputs=None, step_name=None, step_image_url=None) -> web.Response:
    """workflows_update_step

    Update the configuration for a workflow extension step.

    :param token: Authentication token. Requires scope: &#x60;workflow.steps:execute&#x60;
    :type token: str
    :param workflow_step_edit_id: A context identifier provided with &#x60;view_submission&#x60; payloads used to call back to &#x60;workflows.updateStep&#x60;.
    :type workflow_step_edit_id: str
    :param inputs: A JSON key-value map of inputs required from a user during configuration. This is the data your app expects to receive when the workflow step starts. **Please note**: the embedded variable format is set and replaced by the workflow system. You cannot create custom variables that will be replaced at runtime. [Read more about variables in workflow steps here](/workflows/steps#variables).
    :type inputs: str
    :param outputs: An JSON array of output objects used during step execution. This is the data your app agrees to provide when your workflow step was executed.
    :type outputs: str
    :param step_name: An optional field that can be used to override the step name that is shown in the Workflow Builder.
    :type step_name: str
    :param step_image_url: An optional field that can be used to override app image that is shown in the Workflow Builder.
    :type step_image_url: str

    """
    return web.Response(status=200)
