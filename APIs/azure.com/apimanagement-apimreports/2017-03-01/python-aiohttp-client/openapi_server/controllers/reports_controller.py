from typing import List, Dict
from aiohttp import web

from openapi_server.models.report_collection import ReportCollection
from openapi_server.models.request_report_collection import RequestReportCollection
from openapi_server import util


async def reports_list_by_api(request: web.Request, filter, api_version, top=None, skip=None) -> web.Response:
    """reports_list_by_api

    Lists report records by API.

    :param filter: The filter to apply on the operation.
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_geo(request: web.Request, api_version, filter=None, top=None, skip=None) -> web.Response:
    """reports_list_by_geo

    Lists report records by geography.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_operation(request: web.Request, filter, api_version, top=None, skip=None) -> web.Response:
    """reports_list_by_operation

    Lists report records by API Operations.

    :param filter: The filter to apply on the operation.
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_product(request: web.Request, filter, api_version, top=None, skip=None) -> web.Response:
    """reports_list_by_product

    Lists report records by Product.

    :param filter: The filter to apply on the operation.
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_request(request: web.Request, filter, api_version, top=None, skip=None) -> web.Response:
    """reports_list_by_request

    Lists report records by Request.

    :param filter: The filter to apply on the operation.
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_subscription(request: web.Request, api_version, filter=None, top=None, skip=None) -> web.Response:
    """reports_list_by_subscription

    Lists report records by subscription.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_time(request: web.Request, interval, api_version, filter=None, top=None, skip=None) -> web.Response:
    """reports_list_by_time

    Lists report records by Time.

    :param interval: By time interval. Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO  8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations).This code can be used to convert TimeSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds))
    :type interval: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def reports_list_by_user(request: web.Request, filter, api_version, top=None, skip=None) -> web.Response:
    """reports_list_by_user

    Lists report records by User.

    :param filter: The filter to apply on the operation.
    :type filter: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
