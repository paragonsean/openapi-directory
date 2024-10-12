from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_async_request_status import BatchAsyncRequestStatus
from openapi_server.models.downloaded_snapshot_sla_assignment_info import DownloadedSnapshotSlaAssignmentInfo
from openapi_server.models.sla_domain_definition import SlaDomainDefinition
from openapi_server.models.sla_domain_patch_definition import SlaDomainPatchDefinition
from openapi_server.models.sla_domain_summary import SlaDomainSummary
from openapi_server.models.sla_domain_summary_list_response import SlaDomainSummaryListResponse
from openapi_server import util


async def assign_sla_to_downloaded_snapshots(request: web.Request, body) -> web.Response:
    """Assign retention SLA Domain to the downloaded snapshots of a single object

    Assigns an SLA Domain to a list of downloaded snapshots. The SLA Domain manages retention for the snapshots in the downloaded location. The assignment does not affect the retention of the snapshots in other locations.

    :param body: An object ID and a list of IDs for the downloaded snapshots. The specified SLA Domain manages retention for the downloaded copy of snapshots assigned to the specified IDs.
    :type body: dict | bytes

    """
    body = DownloadedSnapshotSlaAssignmentInfo.from_dict(body)
    return web.Response(status=200)


async def create_sla_domain(request: web.Request, body) -> web.Response:
    """Create SLA Domain

    Create a new SLA Domain on a Rubrik cluster by specifying Domain Rules and policies. Only Managed Volume objects support minute frequency to take transaction log backup. SLA assignment on other objects will be disallowed.

    :param body: SLA Domain definition. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using Rubrik cluster timezone.
    :type body: dict | bytes

    """
    body = SlaDomainDefinition.from_dict(body)
    return web.Response(status=200)


async def delete_sla_domain(request: web.Request, id) -> web.Response:
    """Remove SLA Domain

    Delete an SLA Domain from a Rubrik cluster. The SLA Domain must not be assigned to any VMs, filesets or databases.

    :param id: ID of the SLA Domain.
    :type id: str

    """
    return web.Response(status=200)


async def get_sla_domain(request: web.Request, id) -> web.Response:
    """Get SLA Domain details

    Retrieve summary information for a specified SLA Domain.

    :param id: ID of the SLA Domain.
    :type id: str

    """
    return web.Response(status=200)


async def patch_sla_domain(request: web.Request, id, body, should_apply_to_existing_snapshots=None) -> web.Response:
    """Patch SLA Domain

    (DEPRECATED) Patch the properties of an SLA Domain. The recommended endpoint is v3/sla_domain/{id}.

    :param id: ID of the SLA Domain.
    :type id: str
    :param body: Object containing the fields to be edited for SLA Domain. The SLA Domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using the Rubrik cluster timezone. Remote SLA Domain only supports edit to the archival specification.
    :type body: dict | bytes
    :param should_apply_to_existing_snapshots: A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is &#39;true&#39; by default.
    :type should_apply_to_existing_snapshots: bool

    """
    body = SlaDomainPatchDefinition.from_dict(body)
    return web.Response(status=200)


async def query_sla_domain(request: web.Request, primary_cluster_id=None, name=None, sort_by=None, sort_order=None, data_sources=None, snapshot_ids=None) -> web.Response:
    """Get list of SLA Domains

    Retrieve summary information for all SLA Domains.

    :param primary_cluster_id: Limits the information retrieved to those SLA Domains that are associated with the Rubrik cluster ID that is specified by primary_cluster_id. Use **local** for the Rubrik cluster that is hosting the current REST API session.
    :type primary_cluster_id: str
    :param name: Limit the list information to those SLA Domains which match the specified SLA Domain &#39;name&#39; value.
    :type name: str
    :param sort_by: Attribute to use to sort the SLA Domains summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending. If not specified, SLA Domain summary results will be sorted in ascending order.
    :type sort_order: str
    :param data_sources: Limit the list information to SLA Domains that can be assigned to specified data sources.
    :type data_sources: List[str]
    :param snapshot_ids: Limit the list information to SLA Domains that can be assigned to specified snapshots.
    :type snapshot_ids: List[str]

    """
    return web.Response(status=200)


async def update_sla_domain(request: web.Request, id, body, should_apply_to_existing_snapshots=None) -> web.Response:
    """Update SLA Domain

    Update the properties of an SLA Domain.

    :param id: ID of the SLA Domain.
    :type id: str
    :param body: Object containing the updated SLA Domain. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snpashot. Specify times using the Rubrik cluster time zone.
    :type body: dict | bytes
    :param should_apply_to_existing_snapshots: A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is &#39;true&#39; by default.
    :type should_apply_to_existing_snapshots: bool

    """
    body = SlaDomainDefinition.from_dict(body)
    return web.Response(status=200)
