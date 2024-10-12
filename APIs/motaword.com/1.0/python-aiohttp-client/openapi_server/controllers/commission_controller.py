from typing import List, Dict
from aiohttp import web

from openapi_server.models.commission_list import CommissionList
from openapi_server.models.error import Error
from openapi_server.models.report_filter import ReportFilter
from openapi_server import util


async def get_commissions(request: web.Request, ) -> web.Response:
    """Returns a commission list of current client.

    


    """
    return web.Response(status=200)


async def get_commissions_by_filter(request: web.Request, body=None) -> web.Response:
    """Returns a commission list of current client.

    

    :param body: 
    :type body: dict | bytes

    """
    body = ReportFilter.from_dict(body)
    return web.Response(status=200)
