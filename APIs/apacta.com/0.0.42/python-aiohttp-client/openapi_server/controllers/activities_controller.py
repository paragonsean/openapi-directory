from typing import List, Dict
from aiohttp import web

from openapi_server.models.activities_get200_response import ActivitiesGet200Response
from openapi_server.models.activities_post_request import ActivitiesPostRequest
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server import util


async def activities_activity_id_delete(request: web.Request, activity_id) -> web.Response:
    """Delete an activity

    

    :param activity_id: 
    :type activity_id: str
    :type activity_id: str

    """
    return web.Response(status=200)


async def activities_activity_id_put(request: web.Request, activity_id, body) -> web.Response:
    """Edit an activity

    

    :param activity_id: 
    :type activity_id: str
    :type activity_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActivitiesPostRequest.from_dict(body)
    return web.Response(status=200)


async def activities_bulk_delete_delete(request: web.Request, body) -> web.Response:
    """Bulk delete activities

    

    :param body: Activities ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def activities_get(request: web.Request, ) -> web.Response:
    """Get a list of activities

    


    """
    return web.Response(status=200)


async def activities_post(request: web.Request, body) -> web.Response:
    """Create an activity

    

    :param body: 
    :type body: dict | bytes

    """
    body = ActivitiesPostRequest.from_dict(body)
    return web.Response(status=200)
