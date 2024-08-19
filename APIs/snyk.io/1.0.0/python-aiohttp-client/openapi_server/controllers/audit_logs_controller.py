from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_group_level_audit_logs_request import GetGroupLevelAuditLogsRequest
from openapi_server.models.get_organization_level_audit_logs_request import GetOrganizationLevelAuditLogsRequest
from openapi_server import util


async def get_group_level_audit_logs(request: web.Request, group_id, _from=None, to=None, page=None, sort_order=None, body=None) -> web.Response:
    """Get group level audit logs

    

    :param group_id: The group ID. The &#x60;API_KEY&#x60; must have access to this group.
    :type group_id: str
    :param _from: The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months.
    :type _from: str
    :param to: The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months.
    :type to: str
    :param page: The page of results to request. Audit logs are returned in page sizes of 100
    :type page: 
    :param sort_order: The sort order of the returned audit logs by date. Values: &#x60;ASC&#x60;, &#x60;DESC&#x60;. Default: &#x60;DESC&#x60;.
    :type sort_order: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetGroupLevelAuditLogsRequest.from_dict(body)
    return web.Response(status=200)


async def get_organization_level_audit_logs(request: web.Request, org_id, _from=None, to=None, page=None, sort_order=None, body=None) -> web.Response:
    """Get organization level audit logs

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param _from: The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months.
    :type _from: str
    :param to: The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months.
    :type to: str
    :param page: The page of results to request. Audit logs are returned in page sizes of 100.
    :type page: 
    :param sort_order: The sort order of the returned audit logs by date. Values: &#x60;ASC&#x60;, &#x60;DESC&#x60;. Default: &#x60;DESC&#x60;.
    :type sort_order: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetOrganizationLevelAuditLogsRequest.from_dict(body)
    return web.Response(status=200)
