from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_workspace_response import ListWorkspaceResponse
from openapi_server.models.taskrouter_v1_workspace import TaskrouterV1Workspace
from openapi_server.models.workspace_enum_queue_order import WorkspaceEnumQueueOrder
from openapi_server import util


async def create_workspace(request: web.Request, friendly_name, event_callback_url=None, events_filter=None, multi_task_enabled=None, prioritize_queue_order=None, template=None) -> web.Response:
    """create_workspace

    

    :param friendly_name: A descriptive string that you create to describe the Workspace resource. It can be up to 64 characters long. For example: &#x60;Customer Support&#x60; or &#x60;2014 Election Campaign&#x60;.
    :type friendly_name: str
    :param event_callback_url: The URL we should call when an event occurs. If provided, the Workspace will publish events to this URL, for example, to collect data for reporting. See [Workspace Events](https://www.twilio.com/docs/taskrouter/api/event) for more information. This parameter supports Twilio&#39;s [Webhooks (HTTP callbacks) Connection Overrides](https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides).
    :type event_callback_url: str
    :param events_filter: The list of Workspace events for which to call event_callback_url. For example, if &#x60;EventsFilter&#x3D;task.created, task.canceled, worker.activity.update&#x60;, then TaskRouter will call event_callback_url only when a task is created, canceled, or a Worker activity is updated.
    :type events_filter: str
    :param multi_task_enabled: Whether to enable multi-tasking. Can be: &#x60;true&#x60; to enable multi-tasking, or &#x60;false&#x60; to disable it. However, all workspaces should be created as multi-tasking. The default is &#x60;true&#x60;. Multi-tasking allows Workers to handle multiple Tasks simultaneously. When enabled (&#x60;true&#x60;), each Worker can receive parallel reservations up to the per-channel maximums defined in the Workers section. In single-tasking mode (legacy mode), each Worker will only receive a new reservation when the previous task is completed. Learn more at [Multitasking](https://www.twilio.com/docs/taskrouter/multitasking).
    :type multi_task_enabled: bool
    :param prioritize_queue_order: 
    :type prioritize_queue_order: str
    :param template: An available template name. Can be: &#x60;NONE&#x60; or &#x60;FIFO&#x60; and the default is &#x60;NONE&#x60;. Pre-configures the Workspace with the Workflow and Activities specified in the template. &#x60;NONE&#x60; will create a Workspace with only a set of default activities. &#x60;FIFO&#x60; will configure TaskRouter with a set of default activities and a single TaskQueue for first-in, first-out distribution, which can be useful when you are getting started with TaskRouter.
    :type template: str

    """
    return web.Response(status=200)


async def delete_workspace(request: web.Request, sid) -> web.Response:
    """delete_workspace

    

    :param sid: The SID of the Workspace resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_workspace(request: web.Request, sid) -> web.Response:
    """fetch_workspace

    

    :param sid: The SID of the Workspace resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_workspace(request: web.Request, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_workspace

    

    :param friendly_name: The &#x60;friendly_name&#x60; of the Workspace resources to read. For example &#x60;Customer Support&#x60; or &#x60;2014 Election Campaign&#x60;.
    :type friendly_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_workspace(request: web.Request, sid, default_activity_sid=None, event_callback_url=None, events_filter=None, friendly_name=None, multi_task_enabled=None, prioritize_queue_order=None, timeout_activity_sid=None) -> web.Response:
    """update_workspace

    

    :param sid: The SID of the Workspace resource to update.
    :type sid: str
    :param default_activity_sid: The SID of the Activity that will be used when new Workers are created in the Workspace.
    :type default_activity_sid: str
    :param event_callback_url: The URL we should call when an event occurs. See [Workspace Events](https://www.twilio.com/docs/taskrouter/api/event) for more information. This parameter supports Twilio&#39;s [Webhooks (HTTP callbacks) Connection Overrides](https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides).
    :type event_callback_url: str
    :param events_filter: The list of Workspace events for which to call event_callback_url. For example if &#x60;EventsFilter&#x3D;task.created,task.canceled,worker.activity.update&#x60;, then TaskRouter will call event_callback_url only when a task is created, canceled, or a Worker activity is updated.
    :type events_filter: str
    :param friendly_name: A descriptive string that you create to describe the Workspace resource. For example: &#x60;Sales Call Center&#x60; or &#x60;Customer Support Team&#x60;.
    :type friendly_name: str
    :param multi_task_enabled: Whether to enable multi-tasking. Can be: &#x60;true&#x60; to enable multi-tasking, or &#x60;false&#x60; to disable it. However, all workspaces should be maintained as multi-tasking. There is no default when omitting this parameter. A multi-tasking Workspace can&#39;t be updated to single-tasking unless it is not a Flex Project and another (legacy) single-tasking Workspace exists. Multi-tasking allows Workers to handle multiple Tasks simultaneously. In multi-tasking mode, each Worker can receive parallel reservations up to the per-channel maximums defined in the Workers section. In single-tasking mode (legacy mode), each Worker will only receive a new reservation when the previous task is completed. Learn more at [Multitasking](https://www.twilio.com/docs/taskrouter/multitasking).
    :type multi_task_enabled: bool
    :param prioritize_queue_order: 
    :type prioritize_queue_order: str
    :param timeout_activity_sid: The SID of the Activity that will be assigned to a Worker when a Task reservation times out without a response.
    :type timeout_activity_sid: str

    """
    return web.Response(status=200)
