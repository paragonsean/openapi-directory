from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.driving_type import DrivingType
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_driving_types200_response import GetDrivingTypes200Response
from openapi_server.models.post_driving_types_request import PostDrivingTypesRequest
from openapi_server import util


async def bulk_delete_driving_types(request: web.Request, body) -> web.Response:
    """Bulk delete driving types

    

    :param body: Driving types ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_driving_types_driving_type_id(request: web.Request, driving_type_id) -> web.Response:
    """Delete driving type

    

    :param driving_type_id: 
    :type driving_type_id: str

    """
    return web.Response(status=200)


async def get_driving_types(request: web.Request, q=None, sort=None, direction=None) -> web.Response:
    """List the driving types of the company

    

    :param q: 
    :type q: str
    :param sort: 
    :type sort: str
    :param direction: 
    :type direction: str

    """
    return web.Response(status=200)


async def get_driving_types_driving_type_id(request: web.Request, driving_type_id, driving_type_id2) -> web.Response:
    """View driving type

    

    :param driving_type_id: 
    :type driving_type_id: str
    :param driving_type_id2: 
    :type driving_type_id2: str

    """
    return web.Response(status=200)


async def post_driving_types(request: web.Request, body=None) -> web.Response:
    """Create driving type

    

    :param body: 
    :type body: dict | bytes

    """
    body = PostDrivingTypesRequest.from_dict(body)
    return web.Response(status=200)


async def put_driving_types_driving_type_id(request: web.Request, driving_type_id) -> web.Response:
    """Edit driving type

    

    :param driving_type_id: 
    :type driving_type_id: str

    """
    return web.Response(status=200)
