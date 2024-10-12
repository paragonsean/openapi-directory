from typing import List, Dict
from aiohttp import web

from openapi_server.models.v1_scorings_consolidated_daily200_response import V1ScoringsConsolidatedDaily200Response
from openapi_server import util


async def v1_scorings_consolidated(request: web.Request, device_token=None, start_date=None, end_date=None, tag=None, instance_id=None, app_id=None, company_id=None) -> web.Response:
    """/v1/Scorings/consolidated

    /v1/Scorings/consolidated

    :param device_token: 
    :type device_token: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str
    :param tag: 
    :type tag: str
    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str
    :param company_id: 
    :type company_id: str

    """
    return web.Response(status=200)


async def v1_scorings_consolidated_daily(request: web.Request, device_token=None, start_date=None, end_date=None, tag=None, instance_id=None, app_id=None, company_id=None) -> web.Response:
    """/v1/Scorings/consolidated/daily

    /v1/Scorings/consolidated/daily

    :param device_token: 
    :type device_token: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str
    :param tag: 
    :type tag: str
    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str
    :param company_id: 
    :type company_id: str

    """
    return web.Response(status=200)


async def v1_statistics_consolidated(request: web.Request, device_token=None, start_date=None, end_date=None, tag=None, instance_id=None, app_id=None, company_id=None) -> web.Response:
    """/v1/Statistics/consolidated

    /v1/Statistics/consolidated

    :param device_token: 
    :type device_token: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str
    :param tag: 
    :type tag: str
    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str
    :param company_id: 
    :type company_id: str

    """
    return web.Response(status=200)


async def v1_statistics_consolidated_daily(request: web.Request, device_token=None, start_date=None, end_date=None, tag=None, instance_id=None, app_id=None, company_id=None) -> web.Response:
    """/v1/Statistics/consolidated/daily

    /v1/Statistics/consolidated/daily

    :param device_token: 
    :type device_token: str
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str
    :param tag: 
    :type tag: str
    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str
    :param company_id: 
    :type company_id: str

    """
    return web.Response(status=200)
