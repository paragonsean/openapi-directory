from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_item_resource import BusinessItemResource
from openapi_server.models.laid_paper_type import LaidPaperType
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_business_item_by_id(request: web.Request, id, laid_paper=None) -> web.Response:
    """Returns business item by ID.

    

    :param id: Business item with the ID specified
    :type id: str
    :param laid_paper: Business item by laid paper type
    :type laid_paper: dict | bytes

    """
    laid_paper = .from_dict(laid_paper)
    return web.Response(status=200)
