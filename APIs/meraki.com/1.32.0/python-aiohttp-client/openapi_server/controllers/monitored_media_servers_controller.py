from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_insight_monitored_media_server_request import CreateOrganizationInsightMonitoredMediaServerRequest
from openapi_server.models.get_organization_insight_monitored_media_servers200_response_inner import GetOrganizationInsightMonitoredMediaServers200ResponseInner
from openapi_server.models.update_organization_insight_monitored_media_server_request import UpdateOrganizationInsightMonitoredMediaServerRequest
from openapi_server import util


async def create_organization_insight_monitored_media_server_1(request: web.Request, organization_id, body) -> web.Response:
    """Add a media server to be monitored for this organization

    Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationInsightMonitoredMediaServerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_insight_monitored_media_server_1(request: web.Request, organization_id, monitored_media_server_id) -> web.Response:
    """Delete a monitored media server from this organization

    Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str
    :param monitored_media_server_id: 
    :type monitored_media_server_id: str

    """
    return web.Response(status=200)


async def get_organization_insight_monitored_media_server_1(request: web.Request, organization_id, monitored_media_server_id) -> web.Response:
    """Return a monitored media server for this organization

    Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str
    :param monitored_media_server_id: 
    :type monitored_media_server_id: str

    """
    return web.Response(status=200)


async def get_organization_insight_monitored_media_servers_1(request: web.Request, organization_id) -> web.Response:
    """List the monitored media servers for this organization

    List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_insight_monitored_media_server_1(request: web.Request, organization_id, monitored_media_server_id, body=None) -> web.Response:
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
