from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_activity import APIPagedResponseBuildSystemSharedDTOActivity
from openapi_server.models.build_system_shared_dto_activity import BuildSystemSharedDTOActivity
from openapi_server import util


async def activities_delete_activity(request: web.Request, activity_id) -> web.Response:
    """Mark the delete flag for the Activity

    Deletes an Activity. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

    :param activity_id: The id of the activity to delete
    :type activity_id: int

    """
    return web.Response(status=200)


async def activities_get_activities(request: web.Request, limit=None, offset=None, is_include_deleted=None) -> web.Response:
    """Get Activities

    Gets a collection of Activities. When successful, the response is a PagedResponse of Activities.                If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param is_include_deleted: Does it include deleted activity, or not
    :type is_include_deleted: bool

    """
    return web.Response(status=200)


async def activities_get_activity(request: web.Request, activity_id, is_include_deleted=None) -> web.Response:
    """Get an Activity by ID

    Gets an Activity by ID. When successful, the response is the requested Activity.  If unsuccessful,              an appropriate ApiError is returned.

    :param activity_id: The ID of the Activity to get.
    :type activity_id: int
    :param is_include_deleted: Does it include deleted activity, or not
    :type is_include_deleted: bool

    """
    return web.Response(status=200)


async def activities_post_activity(request: web.Request, body) -> web.Response:
    """Create an Activity

    Creates an Activity.  The body of the POST is the Activity to create.  The ActivityID will be assigned              on creation of the Activity.  When successful, the response is the ActivityID.  If unsuccessful, an               appropriate ApiError is returned.

    :param body: The activity to create.  The ActivityID will be assigned on creation of the Activity.
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOActivity.from_dict(body)
    return web.Response(status=200)


async def activities_put_activity(request: web.Request, activity_id, body) -> web.Response:
    """Update an Activity

    Updates an Activity.  The body of the PUT is the updated Activity.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

    :param activity_id: The id of the activity to update
    :type activity_id: int
    :param body: The updated activity
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOActivity.from_dict(body)
    return web.Response(status=200)
