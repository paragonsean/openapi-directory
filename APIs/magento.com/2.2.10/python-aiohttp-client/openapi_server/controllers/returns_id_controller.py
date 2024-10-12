from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rma_data_rma_interface import RmaDataRmaInterface
from openapi_server.models.rma_rma_management_v1_save_rma_post_request import RmaRmaManagementV1SaveRmaPostRequest
from openapi_server import util


async def rma_rma_management_v1_save_rma_put(request: web.Request, id, body=None) -> web.Response:
    """returns/{id}

    Save RMA

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RmaRmaManagementV1SaveRmaPostRequest.from_dict(body)
    return web.Response(status=200)


async def rma_rma_repository_v1_delete_delete(request: web.Request, id, body=None) -> web.Response:
    """returns/{id}

    Delete RMA

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RmaRmaManagementV1SaveRmaPostRequest.from_dict(body)
    return web.Response(status=200)


async def rma_rma_repository_v1_get_get(request: web.Request, id) -> web.Response:
    """returns/{id}

    Return data object for specified RMA id

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
