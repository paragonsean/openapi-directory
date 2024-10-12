from typing import List, Dict
from aiohttp import web

from openapi_server.models.db_log_report_properties import DbLogReportProperties
from openapi_server.models.db_log_report_properties_update import DbLogReportPropertiesUpdate
from openapi_server.models.db_log_report_summary_list_response import DbLogReportSummaryListResponse
from openapi_server import util


async def query_log_report(request: web.Request, effective_sla_domain_id=None, name=None, database_type=None, location=None, log_backup_delay=None, limit=None, offset=None, sort_by=None, sort_order=None) -> web.Response:
    """Get the database log backup delay information

    Get the database log backup delay information.

    :param effective_sla_domain_id: Filter by effective SLA domain.
    :type effective_sla_domain_id: str
    :param name: Filter by the database name substring.
    :type name: str
    :param database_type: Filter by the database type.
    :type database_type: str
    :param location: Filter by the database location.
    :type location: str
    :param log_backup_delay: Filter by the database log backup delay in seconds, greater than this value.
    :type log_backup_delay: int
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Integer specifying the number of initial matches to ignore.
    :type offset: int
    :param sort_by: Specifies the attribute to use while sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def query_report_properties(request: web.Request, ) -> web.Response:
    """Get the database log backup report properties

    Get the properties for the database (SQL and Oracle) log backup delay email notification creation. The properties are logDelayThresholdInMin and logDelayNotificationFrequencyInMin.


    """
    return web.Response(status=200)


async def update_report_properties(request: web.Request, body) -> web.Response:
    """Update the database log backup report properties

    Update the properties for the database (SQL and Oracle) log backup delay email notification creation. The properties are logDelayThresholdInMin and logDelayNotificationFrequencyInMin.

    :param body: Updated report properties.
    :type body: dict | bytes

    """
    body = DbLogReportPropertiesUpdate.from_dict(body)
    return web.Response(status=200)
