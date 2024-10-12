from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_activity_run import APIPagedResponseBuildSystemSharedDTOActivityRun
from openapi_server.models.build_system_shared_dto_activity_run import BuildSystemSharedDTOActivityRun
from openapi_server.models.build_system_shared_dto_activity_run_status import BuildSystemSharedDTOActivityRunStatus
from openapi_server import util


async def activity_runs_get_activity_run(request: web.Request, activity_run_id) -> web.Response:
    """Get an ActivityRun by ID

    Gets an ActivityRun by ID. When successful, the response is the requested ActivityRun.  If unsuccessful,              an appropriate ApiError is returned.

    :param activity_run_id: The ID of the ActivityRun to get.
    :type activity_run_id: int

    """
    return web.Response(status=200)


async def activity_runs_get_activity_run_status(request: web.Request, activity_run_id) -> web.Response:
    """Get the ActivityRunStatus of an ActivityRun

    Gets the ActivityRunStatus of an ActivityRun.  When successful, the response is the requested ActivityRunStatus.              If unsuccessful, an appropriate ApiError is returned.

    :param activity_run_id: The ID of the ActivityRun to get ActivityRunStatus for.
    :type activity_run_id: int

    """
    return web.Response(status=200)


async def activity_runs_get_activity_runs(request: web.Request, limit=None, offset=None, status=None) -> web.Response:
    """Get ActivityRuns

    Gets a collection of ActivityRuns. When successful, the response is a PagedResponse of ActivityRuns.                If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param status: Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.              If not specified, the default status filter is “InProgress”.
    :type status: str

    """
    return web.Response(status=200)


async def activity_runs_put_activity_run(request: web.Request, activity_run_id, body) -> web.Response:
    """Update an ActivityRun

    Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

    :param activity_run_id: The ID of the ActivityRun to update ActivityRunStatus for.
    :type activity_run_id: int
    :param body: The updated ActivityRun.
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOActivityRun.from_dict(body)
    return web.Response(status=200)


async def activity_runs_put_activity_run_status(request: web.Request, activity_run_id, body) -> web.Response:
    """Update the ActivityRunStatus of an ActivityRun

    Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

    :param activity_run_id: The ID of the ActivityRun to update ActivityRunStatus for.
    :type activity_run_id: int
    :param body: The updated ActivityRunStatus.
    :type body: dict | bytes

    """
    body = BuildSystemSharedDTOActivityRunStatus.from_dict(body)
    return web.Response(status=200)
