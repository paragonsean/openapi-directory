from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill_publication_list import BillPublicationList
from openapi_server.models.bill_stage_publication_list import BillStagePublicationList
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def api_v1_bills_bill_id_stages_stage_id_publications_get(request: web.Request, bill_id, stage_id) -> web.Response:
    """Return a list of Bill stage publications.

    

    :param bill_id: 
    :type bill_id: int
    :param stage_id: 
    :type stage_id: int

    """
    return web.Response(status=200)


async def get_bill_publication(request: web.Request, bill_id) -> web.Response:
    """Return a list of Bill publications.

    

    :param bill_id: Publications relating to Bill with Bill ID specified
    :type bill_id: int

    """
    return web.Response(status=200)
