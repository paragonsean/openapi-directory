from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.report_filter import ReportFilter
from openapi_server.models.report_filter_list import ReportFilterList
from openapi_server.models.save_report_filter_request import SaveReportFilterRequest
from openapi_server import util


async def delete_report_filter(request: web.Request, store_id, report_filter_id) -> web.Response:
    """Delete the report filter

    

    :param store_id: Your store identifier
    :type store_id: str
    :param report_filter_id: Your report filter identifier
    :type report_filter_id: str

    """
    return web.Response(status=200)


async def get_report_filter(request: web.Request, store_id, report_filter_id) -> web.Response:
    """Get the report filter description

    

    :param store_id: Your store identifier
    :type store_id: str
    :param report_filter_id: Your report filter identifier
    :type report_filter_id: str

    """
    return web.Response(status=200)


async def get_report_filters(request: web.Request, store_id) -> web.Response:
    """Get report filter list for the given store

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def save_report_filter(request: web.Request, store_id, report_filter_id, body) -> web.Response:
    """Save the report filter

    

    :param store_id: Your store identifier
    :type store_id: str
    :param report_filter_id: Your report filter identifier
    :type report_filter_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveReportFilterRequest.from_dict(body)
    return web.Response(status=200)
