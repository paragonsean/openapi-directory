from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_project_stats import ClientProjectStats
from openapi_server.models.client_string_stats import ClientStringStats
from openapi_server.models.commission_stats import CommissionStats
from openapi_server.models.error import Error
from openapi_server.models.popular_language_pairs import PopularLanguagePairs
from openapi_server.models.report_filter import ReportFilter
from openapi_server import util


async def get_commission_stats(request: web.Request, ) -> web.Response:
    """Returns the total commissions stats.

    


    """
    return web.Response(status=200)


async def get_commission_stats_by_filter(request: web.Request, body=None) -> web.Response:
    """Returns the total commissions stats by report filter.

    

    :param body: 
    :type body: dict | bytes

    """
    body = ReportFilter.from_dict(body)
    return web.Response(status=200)


async def get_popular_pairs(request: web.Request, ) -> web.Response:
    """View your popular language pairs

    


    """
    return web.Response(status=200)


async def get_project_stats(request: web.Request, ) -> web.Response:
    """View your project statistics

    


    """
    return web.Response(status=200)


async def get_string_stats(request: web.Request, ) -> web.Response:
    """View your translation statistics

    


    """
    return web.Response(status=200)
