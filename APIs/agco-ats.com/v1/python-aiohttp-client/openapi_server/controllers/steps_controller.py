from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_step import APIPagedResponseBuildSystemSharedDTOStep
from openapi_server.models.build_system_shared_dto_step import BuildSystemSharedDTOStep
from openapi_server import util


async def steps_get_step(request: web.Request, step_id, is_include_deleted=None) -> web.Response:
    """Get a Step by ID

    Gets a Step by ID. When successful, the response is the requested Step.              If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

    :param step_id: The ID of the Step to get.
    :type step_id: int
    :param is_include_deleted: Does it include deleted step, or not
    :type is_include_deleted: bool

    """
    return web.Response(status=200)


async def steps_get_steps(request: web.Request, limit=None, offset=None, include_deleted=None) -> web.Response:
    """Get Steps

    Gets a collection of Steps. When successful, the response is a PagedResponse of Steps.              If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param include_deleted: Does it include deleted step, or not
    :type include_deleted: bool

    """
    return web.Response(status=200)


async def steps_post_step(request: web.Request, body) -> web.Response:
    """Create a Step

    No Documentation Found.

    :param body: The step to create
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOStep.from_dict(body)
    return web.Response(status=200)


async def steps_put_step(request: web.Request, step_id, body) -> web.Response:
    """Update a Step

    No Documentation Found.

    :param step_id: The step ID of the step to update
    :type step_id: int
    :param body: The updated step
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOStep.from_dict(body)
    return web.Response(status=200)
