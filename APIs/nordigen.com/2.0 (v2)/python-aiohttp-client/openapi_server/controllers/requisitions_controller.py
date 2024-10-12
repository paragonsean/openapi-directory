from typing import List, Dict
from aiohttp import web

from openapi_server.models.paginated_requisition_list import PaginatedRequisitionList
from openapi_server.models.requisition import Requisition
from openapi_server.models.requisition_request import RequisitionRequest
from openapi_server.models.spectacular_requisition import SpectacularRequisition
from openapi_server import util


async def delete_requisition_by_id_v2(request: web.Request, id) -> web.Response:
    """delete_requisition_by_id_v2

    Delete requisition and its end user agreement

    :param id: A UUID string identifying this requisition.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def requisition_by_id(request: web.Request, id) -> web.Response:
    """requisition_by_id

    Retrieve a requisition by ID

    :param id: A UUID string identifying this requisition.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def requisition_created(request: web.Request, body) -> web.Response:
    """requisition_created

    Create a new requisition

    :param body: 
    :type body: dict | bytes

    """
    body = RequisitionRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_all_requisitions(request: web.Request, limit=None, offset=None) -> web.Response:
    """retrieve_all_requisitions

    Retrieve all requisitions belonging to the company

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)
