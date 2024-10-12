from typing import List, Dict
from aiohttp import web

from openapi_server.models.compliance_summary_slav1 import ComplianceSummarySLAV1
from openapi_server.models.compliance_summary_v1 import ComplianceSummaryV1
from openapi_server.models.report_config_patch import ReportConfigPatch
from openapi_server.models.report_config_response import ReportConfigResponse
from openapi_server import util


async def get_compliance_summary_slav1(request: web.Request, snapshot_range) -> web.Response:
    """Get compliance summary information

    Returns the compliance summary information for all protected objects based on whether the last expected snapshot was successful. This requirement is based on the SLA Domain assigned to the objects.

    :param snapshot_range: An SLA Domain-based range of snapshots. Compliance is calculated for snapshots in the range.
    :type snapshot_range: str

    """
    return web.Response(status=200)


async def get_compliance_summary_v1(request: web.Request, ) -> web.Response:
    """Get compliance summary information

    Returns the compliance summary information for all protected objects based on a time-based requirement of at least one snapshot in each 24 hour report period. This view ignores the policies assigned to protected objects through SLA Domains.


    """
    return web.Response(status=200)


async def set_report_config(request: web.Request, body) -> web.Response:
    """Modify the report config

    Set the different report config parameters.

    :param body: Specifies the new report config parameters.
    :type body: dict | bytes

    """
    body = ReportConfigPatch.from_dict(body)
    return web.Response(status=200)
