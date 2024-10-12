from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.report_by_category_request import ReportByCategoryRequest
from openapi_server.models.report_by_category_response import ReportByCategoryResponse
from openapi_server.models.report_by_channel_request import ReportByChannelRequest
from openapi_server.models.report_by_channel_response import ReportByChannelResponse
from openapi_server.models.report_by_day_request import ReportByDayRequest
from openapi_server.models.report_by_day_response import ReportByDayResponse
from openapi_server.models.report_by_product_request import ReportByProductRequest
from openapi_server.models.report_by_product_response import ReportByProductResponse
from openapi_server import util


async def get_store_report_by_category(request: web.Request, store_id, body) -> web.Response:
    """Get the report by category

    Get the report by category

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReportByCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def get_store_report_by_channel(request: web.Request, store_id, body) -> web.Response:
    """Get the report by channel

    Get the report by channel

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReportByChannelRequest.from_dict(body)
    return web.Response(status=200)


async def get_store_report_by_day(request: web.Request, store_id, body) -> web.Response:
    """Get the report by day for a StoreId

    Get the report by day for a StoreId

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReportByDayRequest.from_dict(body)
    return web.Response(status=200)


async def get_store_report_by_day_per_store(request: web.Request, body) -> web.Response:
    """Get the report by day for a StoreId

    Get the report by day for a StoreId

    :param body: 
    :type body: dict | bytes

    """
    body = ReportByDayRequest.from_dict(body)
    return web.Response(status=200)


async def get_store_report_by_product(request: web.Request, store_id, body) -> web.Response:
    """Get the report by product

    Get the report by product

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReportByProductRequest.from_dict(body)
    return web.Response(status=200)
