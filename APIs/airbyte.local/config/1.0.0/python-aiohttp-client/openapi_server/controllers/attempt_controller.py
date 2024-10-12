from typing import List, Dict
from aiohttp import web

from openapi_server.models.internal_operation_result import InternalOperationResult
from openapi_server.models.save_attempt_sync_config_request_body import SaveAttemptSyncConfigRequestBody
from openapi_server.models.save_stats_request_body import SaveStatsRequestBody
from openapi_server.models.set_workflow_in_attempt_request_body import SetWorkflowInAttemptRequestBody
from openapi_server import util


async def save_stats(request: web.Request, body) -> web.Response:
    """For worker to set sync stats of a running attempt.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SaveStatsRequestBody.from_dict(body)
    return web.Response(status=200)


async def save_sync_config(request: web.Request, body) -> web.Response:
    """For worker to save the AttemptSyncConfig for an attempt.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SaveAttemptSyncConfigRequestBody.from_dict(body)
    return web.Response(status=200)


async def set_workflow_in_attempt(request: web.Request, body) -> web.Response:
    """For worker to register the workflow id in attempt.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SetWorkflowInAttemptRequestBody.from_dict(body)
    return web.Response(status=200)
