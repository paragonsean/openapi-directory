from typing import List, Dict
from aiohttp import web

from openapi_server.models.ack_or_resolve_by_user_request import AckOrResolveByUserRequest
from openapi_server.models.ack_or_resolve_request import AckOrResolveRequest
from openapi_server.models.ack_or_resolve_response import AckOrResolveResponse
from openapi_server.models.active_incident_list import ActiveIncidentList
from openapi_server.models.create_incident_request import CreateIncidentRequest
from openapi_server.models.created_incident import CreatedIncident
from openapi_server.models.reroute_collection import RerouteCollection
from openapi_server.models.reroute_status_response import RerouteStatusResponse
from openapi_server import util


async def api_public_v1_incidents_ack_patch(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Acknowledge an incident or list of incidents

    The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: Ack/Resolve payload
    :type body: dict | bytes

    """
    body = AckOrResolveRequest.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_incidents_by_user_ack_patch(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Acknowledge all incidents for which a user was paged.

    The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: Ack/Resolve payload
    :type body: dict | bytes

    """
    body = AckOrResolveByUserRequest.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_incidents_by_user_resolve_patch(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Resolve all incidents for which a user was paged.

    The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: Ack/Resolve payload
    :type body: dict | bytes

    """
    body = AckOrResolveByUserRequest.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_incidents_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get current incident information

    Get a list of the currently open, acknowledged and recently resolved incidents.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_incidents_post(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Create a new incident

    Create a new incident.  This call replicates the function of our &lt;a href&#x3D;\&quot;https://help.victorops.com/knowledge-base/manual-incident-creation/\&quot;&gt;manual incident creation process&lt;/a&gt;. Monitoring tools and custom integrations should be configured using our &lt;a href&#x3D;\&quot;https://help.victorops.com/knowledge-base/victorops-restendpoint-integration/\&quot;&gt;REST Endpoint&lt;/a&gt;.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: The incident details
    :type body: dict | bytes

    """
    body = CreateIncidentRequest.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_incidents_reroute_post(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Reroute one or more incidents to one or more new routable destinations.

    Reroute one or more incidents to one or more users and/or escalation policies  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: The reroute rules
    :type body: dict | bytes

    """
    body = RerouteCollection.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_incidents_resolve_patch(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Resolve an incident or list of incidents

    The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: Ack/Resolve payload
    :type body: dict | bytes

    """
    body = AckOrResolveRequest.from_dict(body)
    return web.Response(status=200)
