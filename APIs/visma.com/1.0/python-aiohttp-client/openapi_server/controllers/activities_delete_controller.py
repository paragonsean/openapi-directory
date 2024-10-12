from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def activities_delete_activity(request: web.Request, guid) -> web.Response:
    """Delete an activity

    Returns: No Content (204) if succeeded. Not found (404) if activity can&#39;t be found.

    :param guid: ID for the activity to delete
    :type guid: str

    """
    return web.Response(status=200)


async def activities_delete_exceptions(request: web.Request, guid) -> web.Response:
    """Resets exceptions from a recurring activity.

    Returns: No Content (204) if succeeded. Not found (404) if activity can&#39;t be found or is not recurring.

    :param guid: ID of the recurring activity
    :type guid: str

    """
    return web.Response(status=200)


async def activity_participants_delete_activity_participant(request: web.Request, activity_guid, activity_participant_guid) -> web.Response:
    """Delete activity participant.

    Returns: No Content (204) if succeeded. Not found (404) if participant can&#39;t be found.

    :param activity_guid: ID of the activity from which to delete the participant. If an activity occurrence guid is given, this will create an exception to the recurring activity and delete the participant from that.
    :type activity_guid: str
    :param activity_participant_guid: ID of the participant
    :type activity_participant_guid: str

    """
    return web.Response(status=200)
