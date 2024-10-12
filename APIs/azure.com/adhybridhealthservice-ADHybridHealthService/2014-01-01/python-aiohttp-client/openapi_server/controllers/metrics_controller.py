from typing import List, Dict
from aiohttp import web

from openapi_server.models.connector_metadata import ConnectorMetadata
from openapi_server.models.metric_metadata import MetricMetadata
from openapi_server.models.metric_metadata_list import MetricMetadataList
from openapi_server.models.metric_sets import MetricSets
from openapi_server.models.metrics import Metrics
from openapi_server import util


async def service_get_metrics(request: web.Request, service_name, metric_name, group_name, api_version, group_key=None, from_date=None, to_date=None) -> web.Response:
    """service_get_metrics

    Gets the server related metrics for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param group_key: The group key
    :type group_key: str
    :param from_date: The start date.
    :type from_date: str
    :param to_date: The end date.
    :type to_date: str

    """
    from_date = util.deserialize_datetime(from_date)
    to_date = util.deserialize_datetime(to_date)
    return web.Response(status=200)


async def service_members_get_connector_metadata(request: web.Request, service_name, service_member_id, metric_name, api_version) -> web.Response:
    """service_members_get_connector_metadata

    Gets the list of connectors and run profile names.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The service member id.
    :type service_member_id: str
    :type service_member_id: str
    :param metric_name: The name of the metric.
    :type metric_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def service_members_get_metrics(request: web.Request, service_name, metric_name, group_name, service_member_id, api_version, group_key=None, from_date=None, to_date=None) -> web.Response:
    """service_members_get_metrics

    Gets the server related metrics for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param service_member_id: The server id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param group_key: The group key
    :type group_key: str
    :param from_date: The start date.
    :type from_date: str
    :param to_date: The end date.
    :type to_date: str

    """
    from_date = util.deserialize_datetime(from_date)
    to_date = util.deserialize_datetime(to_date)
    return web.Response(status=200)


async def services_get_metric_metadata(request: web.Request, service_name, metric_name, api_version) -> web.Response:
    """services_get_metric_metadata

    Gets the service related metrics information.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_get_metric_metadata_for_group(request: web.Request, service_name, metric_name, group_name, api_version, group_key=None, from_date=None, to_date=None) -> web.Response:
    """services_get_metric_metadata_for_group

    Gets the service related metrics for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param group_key: The group key
    :type group_key: str
    :param from_date: The start date.
    :type from_date: str
    :param to_date: The end date.
    :type to_date: str

    """
    from_date = util.deserialize_datetime(from_date)
    to_date = util.deserialize_datetime(to_date)
    return web.Response(status=200)


async def services_list_metric_metadata(request: web.Request, service_name, api_version, filter=None, perf_counter=None) -> web.Response:
    """services_list_metric_metadata

    Gets the service related metrics information.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The metric metadata property filter to apply.
    :type filter: str
    :param perf_counter: Indicates if only performance counter metrics are requested.
    :type perf_counter: bool

    """
    return web.Response(status=200)


async def services_list_metrics_average(request: web.Request, service_name, metric_name, group_name, api_version) -> web.Response:
    """services_list_metrics_average

    Gets the average of the metric values for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_metrics_sum(request: web.Request, service_name, metric_name, group_name, api_version) -> web.Response:
    """services_list_metrics_sum

    Gets the sum of the metric values for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
