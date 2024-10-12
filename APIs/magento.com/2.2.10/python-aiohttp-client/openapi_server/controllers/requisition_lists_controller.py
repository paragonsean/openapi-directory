from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.requisition_list_data_requisition_list_interface import RequisitionListDataRequisitionListInterface
from openapi_server.models.requisition_list_requisition_list_repository_v1_save_post_request import RequisitionListRequisitionListRepositoryV1SavePostRequest
from openapi_server import util


async def requisition_list_requisition_list_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """requisition_lists

    Save Requisition List

    :param body: 
    :type body: dict | bytes

    """
    body = RequisitionListRequisitionListRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
