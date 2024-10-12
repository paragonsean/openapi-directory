from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_audit_actions_response import GetAuditActionsResponse
from openapi_server.models.get_audit_logs_response import GetAuditLogsResponse
from openapi_server.models.rpc_status import RpcStatus
from openapi_server import util


async def audit_logs_get_audit_actions(request: web.Request, account) -> web.Response:
    """Returns list of audit log actions.

    Get audit log actions for a namespace to be used as a filter for querying audit events.

    :param account: Namespace to query audit log actions for.
    :type account: str

    """
    return web.Response(status=200)


async def audit_logs_get_audit_logs(request: web.Request, account, action=None, name=None, actor=None, _from=None, to=None, page=None, page_size=None) -> web.Response:
    """Returns list of audit log  events.

    Get audit log events for a given namespace.

    :param account: Namespace to query audit logs for.
    :type account: str
    :param action: action name one of [\&quot;repo.tag.push\&quot;, ...]. Optional parameter to filter specific audit log actions.
    :type action: str
    :param name: name. Optional parameter to filter audit log events to a specific name. For repository events, this is the name of the repository. For organization events, this is the name of the organization. For team member events, this is the username of the team member.
    :type name: str
    :param actor: actor name. Optional parameter to filter audit log events to the specific user who triggered the event.
    :type actor: str
    :param _from: Start of the time window you wish to query audit events for.
    :type _from: str
    :param to: End of the time window you wish to query audit events for.
    :type to: str
    :param page: page - specify page number. Page number to get.
    :type page: int
    :param page_size: page_size - specify page size. Number of events to return per page.
    :type page_size: int

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
