from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def v1_statistics_consolidated_0(request: web.Request, device_token=None, start_date=None, end_date=None, tag=None, instance_id=None, app_id=None, company_id=None) -> web.Response:
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


async def v1_statistics_consolidated_daily_0(request: web.Request, device_token=None, start_date=None, end_date=None, tag=None, instance_id=None, app_id=None, company_id=None) -> web.Response:
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
