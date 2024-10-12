from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_search_response_list_response import AppSearchResponseListResponse
from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.vapp_export_options import VappExportOptions
from openapi_server.models.vapp_export_snapshot_job_config import VappExportSnapshotJobConfig
from openapi_server.models.vapp_instant_recovery_job_config import VappInstantRecoveryJobConfig
from openapi_server.models.vapp_instant_recovery_options import VappInstantRecoveryOptions
from openapi_server.models.vapp_template_export_job_config import VappTemplateExportJobConfig
from openapi_server.models.vapp_template_export_options_union import VappTemplateExportOptionsUnion
from openapi_server.models.vcd_vapp_detail import VcdVappDetail
from openapi_server.models.vcd_vapp_patch import VcdVappPatch
from openapi_server.models.vcd_vapp_snapshot_detail import VcdVappSnapshotDetail
from openapi_server.models.vcd_vapp_snapshot_summary_list_response import VcdVappSnapshotSummaryListResponse
from openapi_server.models.vcd_vapp_summary_list_response import VcdVappSummaryListResponse
from openapi_server import util


async def create_on_demand_snapshot_v1(request: web.Request, id, body=None) -> web.Response:
    """Create an on-demand snapshot for a vApp

    Start an asynchronous job to create an on-demand snapshot for a specified vApp object.

    :param id: ID assigned to a vApp object.
    :type id: str
    :param body: Configuration for the on-demand backup of a specified vApp object.
    :type body: dict | bytes

    """
    body = BaseOnDemandSnapshotConfig.from_dict(body)
    return web.Response(status=200)


async def create_vapp_export_v1(request: web.Request, snapshot_id, body) -> web.Response:
    """Export vApp snapshot

    Export the specified vApp snapshot into a new vApp or an existing vApp.

    :param snapshot_id: ID assigned to the vApp snapshot object.
    :type snapshot_id: str
    :param body: Configuration for the request to export the specified vApp snapshot.
    :type body: dict | bytes

    """
    body = VappExportSnapshotJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_vapp_instant_recovery_v1(request: web.Request, snapshot_id, body) -> web.Response:
    """Instant Recovery of vApp virtual machines

    Use Instant Recovery to recover specified vApp virtual machines.

    :param snapshot_id: ID assigned to the vApp snapshot object.
    :type snapshot_id: str
    :param body: Configuration for a request to recover specified virtual machines from a vApp snapshot.
    :type body: dict | bytes

    """
    body = VappInstantRecoveryJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_vapp_template_snapshot_export(request: web.Request, snapshot_id, body) -> web.Response:
    """Export of a vApp template snapshot

    Export a vApp template snapashot to a catalog. Use the options endpoint to confirm that exporting to the catalog defaults or the original organization vDC storage profile is possible.

    :param snapshot_id: ID assigned to a vApp snapshot object.
    :type snapshot_id: str
    :param body: Configuration for a request to export a vApp template snapshot to a specific catalog.
    :type body: dict | bytes

    """
    body = VappTemplateExportJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_vcd_vapp_download_snapshot_from_cloud_v1(request: web.Request, id) -> web.Response:
    """Download snapshot from archive

    Provides a method for retrieving a snapshot that is not available locally, from an archival location.

    :param id: ID of snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def delete_vapp_snapshot_v1(request: web.Request, id, location) -> web.Response:
    """Delete a vApp snapshot

    Designate a vApp snapshot as expired and available for garbage collection. The snapshot must be an on-demand snapshot or a snapshot from a vApp that is not assigned to an SLA Domain.

    :param id: ID assigned to a snapshot object.
    :type id: str
    :param location: Location of the snapshot to delete. Use _local_ to delete only the local copy of the snapshot. Use _all_ to delete the snapshot locally, on a replication target, and at an archival location.
    :type location: str

    """
    return web.Response(status=200)


async def delete_vapp_snapshots_v1(request: web.Request, id) -> web.Response:
    """Delete all snapshots of vApp

    Delete all snapshots for a specified vApp object.

    :param id: ID assigned to a vApp object.
    :type id: str

    """
    return web.Response(status=200)


async def get_vapp_async_request_status_v1(request: web.Request, id) -> web.Response:
    """Get vApp job status

    Retrieve the details of a specified asynchronous job for a vApp.

    :param id: ID assigned to an asynchronous job.
    :type id: str

    """
    return web.Response(status=200)


async def get_vapp_snapshot_export_options_v1(request: web.Request, snapshot_id, export_mode, target_vapp_id=None, target_org_vdc_id=None) -> web.Response:
    """Get exportable network configurations

    Retrieve summary information for the vApp networks that are available for network connections from the virtual machines in the exported vApp snapshot. The summary also specifies the default vApp network for each virtual machine network connection.

    :param snapshot_id: ID assigned to the vApp snapshot object to export.
    :type snapshot_id: str
    :param export_mode: Target type for the specified vApp export.
    :type export_mode: str
    :param target_vapp_id: ID assigned to the target vApp object, when the export is into an existing vApp. When the export is not into a target vApp, remove the &#39;target_vapp_id&#39; member.
    :type target_vapp_id: str
    :param target_org_vdc_id: ID assigned to a target organization VDC object. Use the ID when exporting a vApp snapshot to create a new vApp on the specified target organization VDC. When the exported vApp snapshot is not used to create a new vApp on a target organization VDC, remove the &#39;target_org_vdc_id&#39; member.
    :type target_org_vdc_id: str

    """
    return web.Response(status=200)


async def get_vapp_snapshot_instant_recovery_options_v1(request: web.Request, snapshot_id) -> web.Response:
    """Get Instant Recovery information

    Retrieve the available vApp network connections and the default vApp network connection for the virtual machines in a vApp snapshot. Use this information to configure an Instant Recovery of specified virtual machines in the vApp snapshot.

    :param snapshot_id: ID assigned to a vApp snapshot object.
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def get_vapp_snapshot_v1(request: web.Request, id) -> web.Response:
    """Get vApp snapshot details

    Retrieve detailed information about a specified snapshot for a vApp object.

    :param id: ID assigned to a snapshot object.
    :type id: str

    """
    return web.Response(status=200)


async def get_vapp_template_snapshot_export_options(request: web.Request, snapshot_id, catalog_id, name, org_vdc_id=None) -> web.Response:
    """Get Export information for a vApp template snapshot

    Retrieve the available choices vApp template storage profile and organization vDC choices in case of exporting to either original organization vDC defaults of the target catalog. In case advanced option of manually deciding org vdc is preferred, this also provides available storage profile choices.

    :param snapshot_id: ID assigned to a vApp snapshot object.
    :type snapshot_id: str
    :param catalog_id: ID of the target catalog object.
    :type catalog_id: str
    :param name: Name of template object to create. This is used to verify the existence of a template with the given name. Templates must have unique names.
    :type name: str
    :param org_vdc_id: ID assigned to a target organization vDC object. Use the ID when exporting a vApp template snapshot to a specified organization VDC. This ID is used to fetch the avaiable choices to pick the storage profile of the template. Leave this field empty to use the options from the original organization vDC or the target catalog defaults.
    :type org_vdc_id: str

    """
    return web.Response(status=200)


async def get_vcd_vapp_v1(request: web.Request, id) -> web.Response:
    """Get details of a specific vApp

    Retrieve detailed information for a specified vApp.

    :param id: ID assigned to a vApp object.
    :type id: str

    """
    return web.Response(status=200)


async def query_vapp_snapshot_v1(request: web.Request, id) -> web.Response:
    """Get list of snapshots of vApp

    Retrieve summary information for each of the snapshot objects of a specified vApp object.

    :param id: ID assigned to a vApp object.
    :type id: str

    """
    return web.Response(status=200)


async def query_vcd_vapps_v1(request: web.Request, sort_by=None, sort_order=None, limit=None, offset=None, name=None, is_relic=None, effective_sla_domain_id=None, primary_cluster_id=None, sla_assignment=None, include_backup_task_info=None) -> web.Response:
    """Get summary for vApps

    Retrieve summary information for all vCD vApp objects.

    :param sort_by: Attribute to sort the vCD vApp list on.
    :type sort_by: str
    :param sort_order: Order for sorting the results, either ascending or descending.
    :type sort_order: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Number of matches to ignore from the beginning of the results.
    :type offset: int
    :param name: Search for a vCD vApp object by name.
    :type name: str
    :param is_relic: Filter by isRelic field of vCD vApp object. Return both relic and non-relic vApps when this value is not specified.
    :type is_relic: bool
    :param effective_sla_domain_id: Filter by ID of the effective SLA domain.
    :type effective_sla_domain_id: str
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param sla_assignment: Filter by SLA assignment type.
    :type sla_assignment: str
    :param include_backup_task_info: Include backup task information in response.
    :type include_backup_task_info: bool

    """
    return web.Response(status=200)


async def search_vapp_v1(request: web.Request, id, path) -> web.Response:
    """Search for a file in a vApp

    Aggregated search for a file through snapshots of all virtual machines that are presently part of the vApp. Specify the file using a full path prefix or a filename prefix.

    :param id: ID of the vApp.
    :type id: str
    :param path: The path query. Use either a path prefix or a filename prefix.
    :type path: str

    """
    return web.Response(status=200)


async def update_vcd_vapp_v1(request: web.Request, id, body) -> web.Response:
    """Update vApp

    Make changes to the parameters of a specified vApp object.

    :param id: ID assigned to a vApp object.
    :type id: str
    :param body: Parameters to use to update the specified vApp object.
    :type body: dict | bytes

    """
    body = VcdVappPatch.from_dict(body)
    return web.Response(status=200)


async def vcd_missed_snapshots_v1(request: web.Request, id) -> web.Response:
    """Get details about missed snapshots for a vApp

    Retrieve the timestamp for each missed snapshot for a specified vApp.

    :param id: ID of the vApp.
    :type id: str

    """
    return web.Response(status=200)
