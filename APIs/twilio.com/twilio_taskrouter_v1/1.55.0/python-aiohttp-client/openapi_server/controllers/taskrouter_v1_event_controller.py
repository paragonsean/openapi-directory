from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_event_response import ListEventResponse
from openapi_server.models.taskrouter_v1_workspace_event import TaskrouterV1WorkspaceEvent
from openapi_server import util


async def fetch_event(request: web.Request, workspace_sid, sid) -> web.Response:
    """fetch_event

    

    :param workspace_sid: The SID of the Workspace with the Event to fetch.
    :type workspace_sid: str
    :param sid: The SID of the Event resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_event(request: web.Request, workspace_sid, end_date=None, event_type=None, minutes=None, reservation_sid=None, start_date=None, task_queue_sid=None, task_sid=None, worker_sid=None, workflow_sid=None, task_channel=None, sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_event

    

    :param workspace_sid: The SID of the Workspace with the Events to read. Returns only the Events that pertain to the specified Workspace.
    :type workspace_sid: str
    :param end_date: Only include Events that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    :type end_date: str
    :param event_type: The type of Events to read. Returns only Events of the type specified.
    :type event_type: str
    :param minutes: The period of events to read in minutes. Returns only Events that occurred since this many minutes in the past. The default is &#x60;15&#x60; minutes. Task Attributes for Events occuring more 43,200 minutes ago will be redacted.
    :type minutes: int
    :param reservation_sid: The SID of the Reservation with the Events to read. Returns only Events that pertain to the specified Reservation.
    :type reservation_sid: str
    :param start_date: Only include Events from on or after this date and time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Task Attributes for Events older than 30 days will be redacted.
    :type start_date: str
    :param task_queue_sid: The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to the specified TaskQueue.
    :type task_queue_sid: str
    :param task_sid: The SID of the Task with the Events to read. Returns only the Events that pertain to the specified Task.
    :type task_sid: str
    :param worker_sid: The SID of the Worker with the Events to read. Returns only the Events that pertain to the specified Worker.
    :type worker_sid: str
    :param workflow_sid: The SID of the Workflow with the Events to read. Returns only the Events that pertain to the specified Workflow.
    :type workflow_sid: str
    :param task_channel: The TaskChannel with the Events to read. Returns only the Events that pertain to the specified TaskChannel.
    :type task_channel: str
    :param sid: The SID of the Event resource to read.
    :type sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    end_date = util.deserialize_datetime(end_date)
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)
