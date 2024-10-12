from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_mappings_get200_response import AdminMappingsGet200Response
from openapi_server.models.admin_recordings_snapshot_post_request import AdminRecordingsSnapshotPostRequest
from openapi_server.models.admin_recordings_start_post_request import AdminRecordingsStartPostRequest
from openapi_server.models.admin_recordings_status_get200_response import AdminRecordingsStatusGet200Response
from openapi_server import util


async def admin_recordings_snapshot_post(request: web.Request, body) -> web.Response:
    """Take a snapshot recording

    

    :param body: 
    :type body: dict | bytes

    """
    body = AdminRecordingsSnapshotPostRequest.from_dict(body)
    return web.Response(status=200)


async def admin_recordings_start_post(request: web.Request, body) -> web.Response:
    """Start recording

    Begin recording stub mappings

    :param body: 
    :type body: dict | bytes

    """
    body = AdminRecordingsStartPostRequest.from_dict(body)
    return web.Response(status=200)


async def admin_recordings_status_get(request: web.Request, ) -> web.Response:
    """Get recording status

    


    """
    return web.Response(status=200)


async def admin_recordings_stop_post(request: web.Request, ) -> web.Response:
    """Stop recording

    End recording of stub mappings


    """
    return web.Response(status=200)
