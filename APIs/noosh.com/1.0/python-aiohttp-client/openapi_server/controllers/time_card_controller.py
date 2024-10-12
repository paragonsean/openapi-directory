from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.time_card_detail_vo import TimeCardDetailVO
from openapi_server.models.time_card_list_vo import TimeCardListVO
from openapi_server.models.time_card_received_detail_vo import TimeCardReceivedDetailVO
from openapi_server import util


async def get_my_time_card(request: web.Request, workgroup_id, time_card_id) -> web.Response:
    """Get a specific my time cards

    Get a specific my time cards

    :param workgroup_id: 
    :type workgroup_id: str
    :param time_card_id: 
    :type time_card_id: str

    """
    return web.Response(status=200)


async def get_my_time_card_list(request: web.Request, workgroup_id) -> web.Response:
    """List my time cards

    List my time cards

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_received_time_card(request: web.Request, workgroup_id, time_card_id) -> web.Response:
    """List a specific received time cards

    List a specific received time cards

    :param workgroup_id: 
    :type workgroup_id: str
    :param time_card_id: 
    :type time_card_id: str

    """
    return web.Response(status=200)


async def get_received_time_card_list(request: web.Request, workgroup_id) -> web.Response:
    """List received time cards

    List received time cards

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)
