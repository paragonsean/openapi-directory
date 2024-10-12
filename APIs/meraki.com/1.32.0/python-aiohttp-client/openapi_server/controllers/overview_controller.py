from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response
from openapi_server.models.get_network_sensor_alerts_overview_by_metric200_response_inner import GetNetworkSensorAlertsOverviewByMetric200ResponseInner
from openapi_server.models.get_organization_adaptive_policy_overview200_response import GetOrganizationAdaptivePolicyOverview200Response
from openapi_server.models.get_organization_api_requests_overview_response_codes_by_interval200_response_inner import GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner
from openapi_server.models.get_organization_clients_overview200_response import GetOrganizationClientsOverview200Response
from openapi_server.models.get_organization_devices_statuses_overview200_response import GetOrganizationDevicesStatusesOverview200Response
from openapi_server import util


async def get_device_camera_analytics_overview_2(request: web.Request, serial, t0=None, t1=None, timespan=None, object_type=None) -> web.Response:
    """Returns an overview of aggregate analytics data for a timespan

    Returns an overview of aggregate analytics data for a timespan

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
    :type timespan: float
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_network_clients_overview_2(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Return overview statistics for network clients

    Return overview statistics for network clients

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_current_overview_by_metric_3(request: web.Request, network_id) -> web.Response:
    """Return an overview of currently alerting sensors by metric

    Return an overview of currently alerting sensors by metric

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_overview_by_metric_2(request: web.Request, network_id, t0=None, t1=None, timespan=None, interval=None) -> web.Response:
    """Return an overview of alert occurrences over a timespan, by metric

    Return an overview of alert occurrences over a timespan, by metric

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param interval: The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.
    :type interval: int

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_overview_2(request: web.Request, organization_id) -> web.Response:
    """Returns adaptive policy aggregate statistics for an organization

    Returns adaptive policy aggregate statistics for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_api_requests_overview_2(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return an aggregated overview of API requests data

    Return an aggregated overview of API requests data

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_api_requests_overview_response_codes_by_interval_2(request: web.Request, organization_id, t0=None, t1=None, timespan=None, interval=None, version=None, operation_ids=None, source_ips=None, admin_ids=None, user_agent=None) -> web.Response:
    """Tracks organizations&#39; API requests by response code across a given time period

    Tracks organizations&#39; API requests by response code across a given time period

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
    :type timespan: float
    :param interval: The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
    :type interval: int
    :param version: Filter by API version of the endpoint. Allowable values are: [0, 1]
    :type version: int
    :param operation_ids: Filter by operation ID of the endpoint
    :type operation_ids: List[str]
    :param source_ips: Filter by source IP that made the API request
    :type source_ips: List[str]
    :param admin_ids: Filter by admin ID of user that made the API request
    :type admin_ids: List[str]
    :param user_agent: Filter by user agent string for API request. This will filter by a complete or partial match.
    :type user_agent: str

    """
    return web.Response(status=200)


async def get_organization_clients_overview_2(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return summary information around client data usage (in mb) across the given organization.

    Return summary information around client data usage (in mb) across the given organization.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_devices_statuses_overview_3(request: web.Request, organization_id, product_types=None, network_ids=None) -> web.Response:
    """Return an overview of current device statuses

    Return an overview of current device statuses

    :param organization_id: 
    :type organization_id: str
    :param product_types: An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param network_ids: An optional parameter to filter device statuses by network.
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_licenses_overview_2(request: web.Request, organization_id) -> web.Response:
    """Return an overview of the license state for an organization

    Return an overview of the license state for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)
