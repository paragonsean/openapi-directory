from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.volume_group_detail import VolumeGroupDetail
from openapi_server.models.volume_group_force_full_request import VolumeGroupForceFullRequest
from openapi_server.models.volume_group_force_full_response import VolumeGroupForceFullResponse
from openapi_server.models.volume_group_mount_summary import VolumeGroupMountSummary
from openapi_server.models.volume_group_mount_summary_list_response import VolumeGroupMountSummaryListResponse
from openapi_server.models.volume_group_on_demand_snapshot_config import VolumeGroupOnDemandSnapshotConfig
from openapi_server.models.volume_group_patch import VolumeGroupPatch
from openapi_server.models.volume_group_snapshot_detail import VolumeGroupSnapshotDetail
from openapi_server.models.volume_group_snapshot_summary import VolumeGroupSnapshotSummary
from openapi_server.models.volume_group_snapshot_summary_list_response import VolumeGroupSnapshotSummaryListResponse
from openapi_server.models.volume_group_summary_list_response import VolumeGroupSummaryListResponse
from openapi_server import util


async def create_on_demand_volume_group_backup(request: web.Request, id, body=None) -> web.Response:
    """Create on-demand snapshot for the Volume Group

    Create an on-demand snapshot for the given Volume Group ID.

    :param id: The ID of the Volume Group.
    :type id: str
    :param body: Configuration for the on-demand backup. Configuration values are &#x60;volumeIdsIncludedInSnapshot&#x60;, which specifies the unique ID of each volume that is part of this snapshot of the Volume Group, and &#x60;slaID&#x60;, the ID of the SLA Domain for the snapshot.
    :type body: dict | bytes

    """
    body = VolumeGroupOnDemandSnapshotConfig.from_dict(body)
    return web.Response(status=200)


async def get_volume_group(request: web.Request, id) -> web.Response:
    """Get Volume Group details

    Detailed view of a Volume Group.

    :param id: The ID of the Volume Group.
    :type id: str

    """
    return web.Response(status=200)


async def get_volume_group_force_full_spec(request: web.Request, id) -> web.Response:
    """Retrieve the configuration for forcing a full snapshot

    Retrieve the configuration for forcing a full snapshot for a Volume Group.

    :param id: The ID of the Volume Group.
    :type id: str

    """
    return web.Response(status=200)


async def get_volume_group_snapshot(request: web.Request, id) -> web.Response:
    """Get Volume Group snapshot details

    Retrieve detailed information about a snapshot.

    :param id: The ID of the Volume Group snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def get_volume_group_snapshot_mount(request: web.Request, id) -> web.Response:
    """Get summary information for a mount

    Retrieve information on a Volume Group mount. The information returned includes the following items, when available. id (the unique ID of the mount), name (the name of the Volume Group), snapshotDate (the snapshot date), sourceVolumeGroupId (The ID of the Volume Group from which this snapshot was created), sourceHostId (the ID of the source host), sourceHostName (the name of the source host), mountedDate (the date when the mount was created), mountedVolumes (the mounted volumes information), targetHostId (the ID of the mounted volumes host), targetHostName (the name of the mounted volumes host), mountRequestId (the ID of the job instance that initiated the mount), unmountRequestId (the ID of the job instance that intiated the request to remove the mount), isReady (whether the Volume Group mount is ready to use), and restoreScriptSmbPath (the link to the script that can perform bare-metal recovery).

    :param id: The ID of the Volume Group mount.
    :type id: str

    """
    return web.Response(status=200)


async def patch_volume_group(request: web.Request, id, body) -> web.Response:
    """Update Volume Group properties

    Patch Volume Group with specified properties.

    :param id: The ID of Volume Group.
    :type id: str
    :param body: Properties to update for this Volume Group.
    :type body: dict | bytes

    """
    body = VolumeGroupPatch.from_dict(body)
    return web.Response(status=200)


async def query_volume_group(request: web.Request, effective_sla_domain_id=None, primary_cluster_id=None, limit=None, offset=None, is_relic=None, name=None, sla_assignment=None, sort_by=None, sort_order=None) -> web.Response:
    """Get list of Volume Groups

    Get summary of all Volume Groups.

    :param effective_sla_domain_id: The ID of the SLA Domain that controls the protection of the Volume Group.
    :type effective_sla_domain_id: str
    :param primary_cluster_id: The ID of the Rubrik cluster that provides primary protection for the Volume Group.
    :type primary_cluster_id: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Ignore these many matches in the beginning.
    :type offset: int
    :param is_relic: Specifies whether the results should contain only Volume Groups that are accessible on the Rubrik cluster.
    :type is_relic: bool
    :param name: The name of the Volume Group.
    :type name: str
    :param sla_assignment: The type of SLA assigned to the Volume Group.
    :type sla_assignment: str
    :param sort_by: The Volume Group attribute to use in storing the responses. Valid attributes are &#x60;name&#x60; and &#x60;effectiveSlaDomainName&#x60;.
    :type sort_by: str
    :param sort_order: The order to sort the responses. Valid choices are asc (ascending) or desc (descending).
    :type sort_order: str

    """
    return web.Response(status=200)


async def query_volume_group_latest_snapshot(request: web.Request, id) -> web.Response:
    """Get the latest snapshot of the Volume Group

    Retrieve the latest snapshot summary of a Volume Group.

    :param id: ID of the Volume Group.
    :type id: str

    """
    return web.Response(status=200)


async def query_volume_group_snapshot(request: web.Request, id) -> web.Response:
    """Get list of snapshots of the Volume Group

    Retrieve snapshot details for a Volume Group.

    :param id: The ID of the Volume Group.
    :type id: str

    """
    return web.Response(status=200)


async def query_volume_group_snapshot_mount(request: web.Request, source_volume_group_id=None, source_host_name=None, sort_by=None, sort_order=None, offset=None, limit=None) -> web.Response:
    """Get summary information for all mounts

    Retrieves information for each Volume Group mount. The information returned includes the following items, when available. id (the unique ID of the mount), name (the name of the Volume Group), snapshotDate (the snapshot date), sourceVolumeGroupId (the ID of the Volume Group from which this snapshot was created), sourceHostId (the ID of the source host), sourceHostName (the name of the source host), mountedDate (the date when the mount was created), mountedVolumes (information on the mounted volumes), targetHostId (the ID of the mounted volumes host), targetHostName (the name of the mounted volumes host), mountRequestId (the ID of the job instance that initiated the mount), unmountRequestId (the ID of the job instance that initiated the request to remove the mount), isReady (whether the Volume Group mount is ready to use), and restoreScriptSmbPath (the link to the script that can perform bare-metal recovery).

    :param source_volume_group_id: The ID of the source Volume Group.
    :type source_volume_group_id: str
    :param source_host_name: A prefix of the source host name. The prefix is used as a response filter when available.
    :type source_host_name: str
    :param sort_by: The Volume Group mount attribute used in sorting the responses. Valid choices are name, sourceHostName, snapshotDate, and mountedDate.
    :type sort_by: str
    :param sort_order: The order to sort the responses. Valid choices are asc (ascending) or desc (descending).
    :type sort_order: str
    :param offset: Ignore these many matches in the beginning.
    :type offset: int
    :param limit: Limit the number of matches returned. The default value is 25.
    :type limit: int

    """
    return web.Response(status=200)


async def request_volume_group_force_full_snapshot(request: web.Request, id, body) -> web.Response:
    """Request a full snapshot on the next backup job of a Volume Group

    Request a full snapshot to be taken during the next backup job of a Volume Group.

    :param id: The ID of the Volume Group.
    :type id: str
    :param body: Configuration for forcing a full snapshot on the Volume Group.
    :type body: dict | bytes

    """
    body = VolumeGroupForceFullRequest.from_dict(body)
    return web.Response(status=200)
