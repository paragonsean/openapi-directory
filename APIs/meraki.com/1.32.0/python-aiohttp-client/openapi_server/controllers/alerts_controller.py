from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_sensor_alerts_profile_request import CreateNetworkSensorAlertsProfileRequest
from openapi_server.models.create_organization_alerts_profile_request import CreateOrganizationAlertsProfileRequest
from openapi_server.models.get_network_alerts_history200_response_inner import GetNetworkAlertsHistory200ResponseInner
from openapi_server.models.get_network_health_alerts200_response_inner import GetNetworkHealthAlerts200ResponseInner
from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response
from openapi_server.models.get_network_sensor_alerts_overview_by_metric200_response_inner import GetNetworkSensorAlertsOverviewByMetric200ResponseInner
from openapi_server.models.get_network_sensor_alerts_profiles200_response_inner import GetNetworkSensorAlertsProfiles200ResponseInner
from openapi_server.models.update_network_alerts_settings_request import UpdateNetworkAlertsSettingsRequest
from openapi_server.models.update_network_sensor_alerts_profile_request import UpdateNetworkSensorAlertsProfileRequest
from openapi_server.models.update_organization_alerts_profile_request import UpdateOrganizationAlertsProfileRequest
from openapi_server import util


async def create_network_sensor_alerts_profile_1(request: web.Request, network_id, body) -> web.Response:
    """Creates a sensor alert profile for a network.

    Creates a sensor alert profile for a network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSensorAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_alerts_profile_1(request: web.Request, organization_id, body) -> web.Response:
    """Create an organization-wide alert configuration

    Create an organization-wide alert configuration

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_sensor_alerts_profile_1(request: web.Request, network_id, id) -> web.Response:
    """Deletes a sensor alert profile from a network.

    Deletes a sensor alert profile from a network.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organization_alerts_profile_1(request: web.Request, organization_id, alert_config_id) -> web.Response:
    """Removes an organization-wide alert config

    Removes an organization-wide alert config

    :param organization_id: 
    :type organization_id: str
    :param alert_config_id: 
    :type alert_config_id: str

    """
    return web.Response(status=200)


async def get_network_alerts_history_1(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the alert history for this network

    Return the alert history for this network

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_alerts_settings_1(request: web.Request, network_id) -> web.Response:
    """Return the alert configuration for this network

    Return the alert configuration for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_health_alerts_2(request: web.Request, network_id) -> web.Response:
    """Return all global alerts on this network

    Return all global alerts on this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_current_overview_by_metric_1(request: web.Request, network_id) -> web.Response:
    """Return an overview of currently alerting sensors by metric

    Return an overview of currently alerting sensors by metric

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_overview_by_metric_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, interval=None) -> web.Response:
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


async def get_network_sensor_alerts_profile_1(request: web.Request, network_id, id) -> web.Response:
    """Show details of a sensor alert profile for a network.

    Show details of a sensor alert profile for a network.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_profiles_1(request: web.Request, network_id) -> web.Response:
    """Lists all sensor alert profiles for a network.

    Lists all sensor alert profiles for a network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_alerts_profiles_1(request: web.Request, organization_id) -> web.Response:
    """List all organization-wide alert configurations

    List all organization-wide alert configurations

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_network_alerts_settings_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the alert configuration for this network

    Update the alert configuration for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAlertsSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_sensor_alerts_profile_1(request: web.Request, network_id, id, body=None) -> web.Response:
    """Updates a sensor alert profile for a network.

    Updates a sensor alert profile for a network.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSensorAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_alerts_profile_1(request: web.Request, organization_id, alert_config_id, body=None) -> web.Response:
    """Update an organization-wide alert config

    Update an organization-wide alert config

    :param organization_id: 
    :type organization_id: str
    :param alert_config_id: 
    :type alert_config_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)
