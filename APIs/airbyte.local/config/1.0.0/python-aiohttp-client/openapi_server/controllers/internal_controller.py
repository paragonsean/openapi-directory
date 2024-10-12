from typing import List, Dict
from aiohttp import web

from openapi_server.models.attempt_normalization_status_read_list import AttemptNormalizationStatusReadList
from openapi_server.models.connection_state import ConnectionState
from openapi_server.models.connection_state_create_or_update import ConnectionStateCreateOrUpdate
from openapi_server.models.discover_catalog_result import DiscoverCatalogResult
from openapi_server.models.internal_operation_result import InternalOperationResult
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.job_id_request_body import JobIdRequestBody
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.save_attempt_sync_config_request_body import SaveAttemptSyncConfigRequestBody
from openapi_server.models.save_stats_request_body import SaveStatsRequestBody
from openapi_server.models.set_workflow_in_attempt_request_body import SetWorkflowInAttemptRequestBody
from openapi_server.models.source_discover_schema_write_request_body import SourceDiscoverSchemaWriteRequestBody
from openapi_server import util


async def create_or_update_state_0(request: web.Request, body) -> web.Response:
    """Create or update the state for a connection.

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionStateCreateOrUpdate.from_dict(body)
    return web.Response(status=200)


async def get_attempt_normalization_statuses_for_job_0(request: web.Request, body=None) -> web.Response:
    """Get normalization status to determine if we can bypass normalization phase

    

    :param body: 
    :type body: dict | bytes

    """
    body = JobIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def save_stats_0(request: web.Request, body) -> web.Response:
    """For worker to set sync stats of a running attempt.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SaveStatsRequestBody.from_dict(body)
    return web.Response(status=200)


async def save_sync_config_0(request: web.Request, body) -> web.Response:
    """For worker to save the AttemptSyncConfig for an attempt.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SaveAttemptSyncConfigRequestBody.from_dict(body)
    return web.Response(status=200)


async def set_workflow_in_attempt_0(request: web.Request, body) -> web.Response:
    """For worker to register the workflow id in attempt.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SetWorkflowInAttemptRequestBody.from_dict(body)
    return web.Response(status=200)


async def write_discover_catalog_result_0(request: web.Request, body) -> web.Response:
    """Should only called from worker, to write result from discover activity back to DB.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDiscoverSchemaWriteRequestBody.from_dict(body)
    return web.Response(status=200)
