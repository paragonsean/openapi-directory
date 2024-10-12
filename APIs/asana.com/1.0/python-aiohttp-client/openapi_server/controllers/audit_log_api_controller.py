from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_audit_log_events200_response import GetAuditLogEvents200Response
from openapi_server import util


async def get_audit_log_events(request: web.Request, workspace_gid, start_at=None, end_at=None, event_type=None, actor_type=None, actor_gid=None, resource_gid=None, limit=None, offset=None) -> web.Response:
    """Get audit log events

    Retrieve the audit log events that have been captured in your domain.  This endpoint will return a list of [AuditLogEvent](/docs/audit-log-event) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.  There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/docs/audit-log-event) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.  The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the &#x60;offset&#x60; from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return &#x60;null&#x60; for the &#x60;next_page&#x60; field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a &#x60;next_page&#x60; with an &#x60;offset&#x60;, subsequent requests can be made with the latest &#x60;offset&#x60; to poll for new events that match the provided filters.  When no &#x60;offset&#x60; is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/docs/audit-log-event) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.

    :param workspace_gid: Globally unique identifier for the workspace or organization.
    :type workspace_gid: str
    :param start_at: Filter to events created after this time (inclusive).
    :type start_at: str
    :param end_at: Filter to events created before this time (exclusive).
    :type end_at: str
    :param event_type: Filter to events of this type. Refer to the [Supported AuditLogEvents](/docs/supported-auditlogevents) for a full list of values.
    :type event_type: str
    :param actor_type: Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If &#x60;actor_gid&#x60; is included, this should be excluded.
    :type actor_type: str
    :param actor_gid: Filter to events triggered by the actor with this ID.
    :type actor_gid: str
    :param resource_gid: Filter to events with this resource ID.
    :type resource_gid: str
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    start_at = util.deserialize_datetime(start_at)
    end_at = util.deserialize_datetime(end_at)
    return web.Response(status=200)
