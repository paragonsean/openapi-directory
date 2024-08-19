from typing import List, Dict
from aiohttp import web

from openapi_server.models.incident_response import IncidentResponse
from openapi_server.models.list_incidents_response import ListIncidentsResponse
from openapi_server.models.list_related_incidents_response import ListRelatedIncidentsResponse
from openapi_server import util


async def get_incident(request: web.Request, incident_id) -> web.Response:
    """Get an Incident

    Returns the details of an incident.

    :param incident_id: ID of the Incident
    :type incident_id: str

    """
    return web.Response(status=200)


async def list_incidents(request: web.Request, limit=None, page=None, order_by=None, order_direction=None, status=None, severity=None) -> web.Response:
    """List Incidents

    Returns a list of incidents.

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param order_by: Value to order the results by
    :type order_by: str
    :param order_direction: Sort order.
    :type order_direction: str
    :param status: Status to filter incidents by
    :type status: str
    :param severity: Severity to filter incidents by
    :type severity: str

    """
    return web.Response(status=200)


async def list_related_incidents(request: web.Request, incident_id, limit=None, page=None, order_by=None, order_direction=None) -> web.Response:
    """List Related Incidents

    Returns all the incidents that seem related to a specific incident.

    :param incident_id: ID of the Incident
    :type incident_id: str
    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param order_by: Value to order the results by
    :type order_by: str
    :param order_direction: Sort order.
    :type order_direction: str

    """
    return web.Response(status=200)
