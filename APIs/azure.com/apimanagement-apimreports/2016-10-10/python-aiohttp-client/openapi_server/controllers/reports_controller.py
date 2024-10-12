from typing import List, Dict
from aiohttp import web

from openapi_server.models.report_collection import ReportCollection
from openapi_server import util


async def reports_list_by_service(request: web.Request, resource_group_name, service_name, aggregation, api_version, subscription_id, filter=None, top=None, skip=None, interval=None) -> web.Response:
    """reports_list_by_service

    Lists report records.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param aggregation: Report aggregation.
    :type aggregation: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param interval: By time interval. This value is only applicable to ByTime aggregation. Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO  8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations).This code can be used to convert TimSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds))
    :type interval: str

    """
    return web.Response(status=200)
