from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_list import OperationList
from openapi_server.models.usage_aggregate_page import UsageAggregatePage
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Returns the list of supported REST operations.

    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscriber_usage_aggregates_list(request: web.Request, subscription_id, api_version, reported_start_time, reported_end_time, aggregation_granularity=None, subscriber_id=None, continuation_token=None) -> web.Response:
    """subscriber_usage_aggregates_list

    Gets a collection of SubscriberUsageAggregates, which are UsageAggregates from users.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param reported_start_time: The reported start time (inclusive).
    :type reported_start_time: str
    :param reported_end_time: The reported end time (exclusive).
    :type reported_end_time: str
    :param aggregation_granularity: The aggregation granularity.
    :type aggregation_granularity: str
    :param subscriber_id: The tenant subscription identifier.
    :type subscriber_id: str
    :param continuation_token: The continuation token.
    :type continuation_token: str

    """
    reported_start_time = util.deserialize_datetime(reported_start_time)
    reported_end_time = util.deserialize_datetime(reported_end_time)
    return web.Response(status=200)


async def update_encryption(request: web.Request, subscription_id, api_version) -> web.Response:
    """update_encryption

    Update the encryption.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
