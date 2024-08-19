from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_model import ActivityModel
from openapi_server.models.activity_participant_model import ActivityParticipantModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server import util


async def activities_patch_activity(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a activity or a part of it

    

    :param guid: ID of the activity. Can also be comma separate list of IDs to patch multiple activities with one call. When multiple IDs are given, returns model which has list of succeeded activities and list of errors.
    :type guid: str
    :param body: JSON Patch document of ActivityModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def activities_post_activity(request: web.Request, body=None) -> web.Response:
    """Insert a activity

    

    :param body: ActivityModel
    :type body: dict | bytes

    """
    body = ActivityModel.from_dict(body)
    return web.Response(status=200)


async def activity_participants_patch_activity_participants(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a activity participant or a part of it

    Only IsConfirmed property can be updated.

    :param guid: ID of the activity participant
    :type guid: str
    :param body: JSON patch document of ActivityParticipantModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def activity_participants_post_activity_participant(request: web.Request, body=None) -> web.Response:
    """Adds an activity participant

    

    :param body: ActivityParticipantModel
    :type body: dict | bytes

    """
    body = ActivityParticipantModel.from_dict(body)
    return web.Response(status=200)
