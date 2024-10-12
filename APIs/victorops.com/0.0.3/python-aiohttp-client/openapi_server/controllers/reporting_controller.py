from typing import List, Dict
from aiohttp import web

from openapi_server.models.active_incident_list import ActiveIncidentList
from openapi_server.models.incident_list import IncidentList
from openapi_server.models.on_call_log import OnCallLog
from openapi_server import util


async def api_reporting_v1_incidents_get(request: web.Request, x_vo_api_id, x_vo_api_key, offset=None, limit=None, entity_id=None, incident_number=None, started_after=None, started_before=None, host=None, service=None, current_phase=None) -> web.Response:
    """Get/search incident history

     __NOTE: This call is deprecated. Please use &#x60;GET /api-reporting/v2/incidents&#x60;.__  Retrieve incident history for your company, searching over date ranges and with filtering options.  This is historical data, and may be up to 15 minutes behind real-time incident data.  By default, only resolved incidents will be returned.  This API may be called a maximum of once a minute.  Incident requests are paginated with a offset and limit query string parameters.   The query for incidents is run and offset records are skipped, after which limit records will be returned.  The default offset is 0 and the default limit is 20. The maximum value allowed for limit is 100.  On return, the total number of records available for that query will be returned in the payload as &#39;total&#39;. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param offset: The offset within the set of matching incidents
    :type offset: 
    :param limit: The maximum number of matching incidents to return (100 max)
    :type limit: 
    :param entity_id: The entity ID involved  This is the unique identifier for the entity causing the incident.
    :type entity_id: str
    :param incident_number: The incident number as shown in VictorOps Multiple values and ranges are allowed: 4,5,20:50 
    :type incident_number: str
    :param started_after: Return incidents started after this timestamp Specify the timestamp in ISO8601 format
    :type started_after: str
    :param started_before: Find incidents started before this timestamp  Specify the timestamp in ISO8601 format
    :type started_before: str
    :param host: The host involved in the incident Multiple values can be separated with commas.
    :type host: str
    :param service: The service involved in the incident (if any) Multiple values can be separated with commas.
    :type service: str
    :param current_phase: The current phase of the incident \&quot;resolved\&quot;, \&quot;triggered\&quot; or \&quot;acknowledged\&quot;. Multiple values can be separated with commas.
    :type current_phase: str

    """
    return web.Response(status=200)


async def api_reporting_v1_team_team_oncall_log_get(request: web.Request, x_vo_api_id, x_vo_api_key, team, start=None, end=None, user_name=None) -> web.Response:
    """A list of shift changes for a team

    Returns a log of user shift changes for the specified team. This is historical data, and may be up to 15 minutes behind real-time log data.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team &#39;slug&#39;
    :type team: str
    :param start: Return shift changes occurring after this timestamp. The default is the start of the day at midnight. Specify the timestamp in ISO8601 format
    :type start: str
    :param end: Return shift changes occurring before this timestamp. The default is the end of the day at 11:59:59. Specify the timestamp in ISO8601 format
    :type end: str
    :param user_name: The VictorOps user ID. Return shift changes occurring during the interval specified for this user. Without this parameter, all relevant users (with respect to the specified interval) are returned
    :type user_name: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def api_reporting_v2_incidents_get(request: web.Request, x_vo_api_id, x_vo_api_key, offset=None, limit=None, entity_id=None, incident_number=None, started_after=None, started_before=None, host=None, service=None, current_phase=None, routing_key=None) -> web.Response:
    """Get/search incident history

    Retrieve incident history for your company, searching over date ranges and with filtering options.  This API may be called a maximum of once a minute.  Incident requests are paginated with a offset and limit query string parameters.   The query for incidents is run and offset records are skipped, after which limit records will be returned.  The default offset is 0 and the default limit is 20. The maximum value allowed for limit is 100.  Unless specified otherwise with the parameter currentPhase, the response will only contain resolved incidents.  On return, the total number of records available for that query will be returned in the payload as &#39;total&#39;. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param offset: The offset within the set of matching incidents
    :type offset: 
    :param limit: The maximum number of matching incidents to return (100 max)
    :type limit: 
    :param entity_id: The entity ID involved  This is the unique identifier for the entity causing the incident.
    :type entity_id: str
    :param incident_number: The incident number as shown in VictorOps Multiple values and ranges are allowed: 4,5,20:50 
    :type incident_number: str
    :param started_after: Return incidents started after this timestamp Specify the timestamp in ISO8601 format
    :type started_after: str
    :param started_before: Find incidents started before this timestamp  Specify the timestamp in ISO8601 format
    :type started_before: str
    :param host: The host involved in the incident Multiple values can be separated with commas.
    :type host: str
    :param service: The service involved in the incident (if any) Multiple values can be separated with commas.
    :type service: str
    :param current_phase: The current phase of the incident \&quot;resolved\&quot;, \&quot;triggered\&quot; or \&quot;acknowledged\&quot;. Multiple values can be separated with commas. By default, response contains only \&quot;resolved\&quot; incidents
    :type current_phase: str
    :param routing_key: The original routing of the incident
    :type routing_key: str

    """
    return web.Response(status=200)
