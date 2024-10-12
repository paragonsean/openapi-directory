from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_insight_monitored_media_server_request import CreateOrganizationInsightMonitoredMediaServerRequest
from openapi_server.models.get_network_insight_application_health_by_time200_response_inner import GetNetworkInsightApplicationHealthByTime200ResponseInner
from openapi_server.models.get_organization_insight_applications200_response_inner import GetOrganizationInsightApplications200ResponseInner
from openapi_server.models.get_organization_insight_monitored_media_servers200_response_inner import GetOrganizationInsightMonitoredMediaServers200ResponseInner
from openapi_server.models.update_organization_insight_monitored_media_server_request import UpdateOrganizationInsightMonitoredMediaServerRequest
from openapi_server import util


async def create_organization_insight_monitored_media_server(request: web.Request, organization_id, body) -> web.Response:
    """Add a media server to be monitored for this organization

    Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInsightMonitoredMediaServerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_insight_monitored_media_server(request: web.Request, organization_id, monitored_media_server_id) -> web.Response:
    """Delete a monitored media server from this organization

    Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str
    :param monitored_media_server_id: 
    :type monitored_media_server_id: str

    """
    return web.Response(status=200)


async def get_network_insight_application_health_by_time(request: web.Request, network_id, application_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Get application health by time

    Get application health by time

    :param network_id: 
    :type network_id: str
    :param application_id: 
    :type application_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_organization_insight_applications(request: web.Request, organization_id) -> web.Response:
    """List all Insight tracked applications

    List all Insight tracked applications

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_insight_monitored_media_server(request: web.Request, organization_id, monitored_media_server_id) -> web.Response:
    """Return a monitored media server for this organization

    Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str
    :param monitored_media_server_id: 
    :type monitored_media_server_id: str

    """
    return web.Response(status=200)


async def get_organization_insight_monitored_media_servers(request: web.Request, organization_id) -> web.Response:
    """List the monitored media servers for this organization

    List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_insight_monitored_media_server(request: web.Request, organization_id, monitored_media_server_id, body=None) -> web.Response:
    """Update a monitored media server for this organization

    Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str
    :param monitored_media_server_id: 
    :type monitored_media_server_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationInsightMonitoredMediaServerRequest.from_dict(body)
    return web.Response(status=200)
