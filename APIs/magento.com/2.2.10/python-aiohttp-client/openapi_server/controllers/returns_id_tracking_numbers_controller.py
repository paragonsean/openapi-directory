from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rma_data_track_search_result_interface import RmaDataTrackSearchResultInterface
from openapi_server.models.rma_track_management_v1_add_track_post_request import RmaTrackManagementV1AddTrackPostRequest
from openapi_server import util


async def rma_track_management_v1_add_track_post(request: web.Request, id, body=None) -> web.Response:
    """returns/{id}/tracking-numbers

    Add track

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RmaTrackManagementV1AddTrackPostRequest.from_dict(body)
    return web.Response(status=200)


async def rma_track_management_v1_get_tracks_get(request: web.Request, id) -> web.Response:
    """returns/{id}/tracking-numbers

    Get track list

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
