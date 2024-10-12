from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.browse_response_list_response import BrowseResponseListResponse
from openapi_server.models.fileset_create import FilesetCreate
from openapi_server.models.fileset_detail import FilesetDetail
from openapi_server.models.fileset_download_file_job_config import FilesetDownloadFileJobConfig
from openapi_server.models.fileset_export_file_job_config import FilesetExportFileJobConfig
from openapi_server.models.fileset_restore_file_job_config import FilesetRestoreFileJobConfig
from openapi_server.models.fileset_snapshot_detail import FilesetSnapshotDetail
from openapi_server.models.fileset_summary_list_response import FilesetSummaryListResponse
from openapi_server.models.fileset_update import FilesetUpdate
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.search_response_list_response import SearchResponseListResponse
from openapi_server import util


async def browse_fileset_snapshot(request: web.Request, id, path, offset=None, limit=None) -> web.Response:
    """Lists all files and directories in a given path

    Lists all files and directories in a given path.

    :param id: ID of snapshot.
    :type id: str
    :param path: The absolute path of the starting point for the directory listing.
    :type path: str
    :param offset: Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries.
    :type offset: int
    :param limit: Maximum number of entries in the response.
    :type limit: int

    """
    return web.Response(status=200)


async def create_download_fileset_snapshot_from_cloud(request: web.Request, id) -> web.Response:
    """Create a download fileset snapshot from archival request

    Create a download fileset snapshot from archival request.

    :param id: ID of snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def create_fileset(request: web.Request, body) -> web.Response:
    """Create one fileset for a host

    Create a fileset for a network host. A fileset is a fileset template applied to a host.

    :param body: Specify a template ID and either a host ID or a share ID. When a share ID is provided, the host ID is derived from the host share. Also specify whether or not this backup is a direct archive backup.
    :type body: dict | bytes

    """
    body = FilesetCreate.from_dict(body)
    return web.Response(status=200)


async def create_fileset_backup_job(request: web.Request, id, body=None) -> web.Response:
    """Initiate an on-demand backup for a fileset

    Create an on-demand backup request for the given fileset.

    :param id: ID of the Fileset.
    :type id: str
    :param body: Configuration for the on-demand backup.
    :type body: dict | bytes

    """
    body = BaseOnDemandSnapshotConfig.from_dict(body)
    return web.Response(status=200)


async def create_fileset_download_file_job(request: web.Request, id, body) -> web.Response:
    """Create a file download job from a fileset backup

    Initiate a job to download a file from a backup of a fileset. Returns a job instance ID. An email notification will be sent out when the download is ready. When the download is ready, the file can be downloaded from the corresponding event which includes the job instance ID as the value of **jobInstanceId**.

    :param id: ID of snapshot.
    :type id: str
    :param body: Configuration for a download job.
    :type body: dict | bytes

    """
    body = FilesetDownloadFileJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_fileset_export_file_job(request: web.Request, id, body) -> web.Response:
    """Create export job

    Initiate a job to copy a file or folder from a fileset backup to a destination host other than the source host. Returns the job instance ID.

    :param id: ID of snapshot.
    :type id: str
    :param body: Configuration for job to export a file or folder from a fileset backup.
    :type body: dict | bytes

    """
    body = FilesetExportFileJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_fileset_restore_file_job(request: web.Request, id, body) -> web.Response:
    """Create restore job

    Initiate a job to copy a file or folder from a fileset backup to the source host. Returns the job instance ID.

    :param id: ID of snapshot.
    :type id: str
    :param body: Configuration for job to restore a file or folder from a fileset backup.
    :type body: dict | bytes

    """
    body = FilesetRestoreFileJobConfig.from_dict(body)
    return web.Response(status=200)


async def delete_fileset(request: web.Request, id, preserve_snapshots=None) -> web.Response:
    """Delete a fileset

    Delete a fileset by specifying the fileset ID.

    :param id: Provide a fileset ID to delete.
    :type id: str
    :param preserve_snapshots: Flag to indicate whether to preserve snapshots of the fileset or to delete them. Default behavior is to preserve them.
    :type preserve_snapshots: bool

    """
    return web.Response(status=200)


async def delete_fileset_snapshot(request: web.Request, id, location) -> web.Response:
    """Delete a fileset snapshot

    Delete a fileset snapshot. A snapshot is deleted only if it is an on-demand snapshot, a snapshot of an unprotected fileset or a local snapshot that was downloaded from an archive location.

    :param id: ID of snapshot.
    :type id: str
    :param location: Snapshot location to delete. Use **_local_** to delete all local snapshots and **_all_** to delete the snapshot in all locations.
    :type location: str

    """
    return web.Response(status=200)


async def delete_fileset_snapshots(request: web.Request, id) -> web.Response:
    """Delete all snapshots of a fileset

    Delete all snapshots that were created based on a fileset by providing the fileset ID. Requires an unprotected fileset. Remove the fileset from all SLA Domains.

    :param id: ID of the fileset.
    :type id: str

    """
    return web.Response(status=200)


async def get_fileset(request: web.Request, id) -> web.Response:
    """Get information for a single fileset

    Retrieve summary information for a fileset by specifying the fileset ID.

    :param id: Specify the fileset ID.
    :type id: str

    """
    return web.Response(status=200)


async def get_fileset_async_request_status(request: web.Request, id) -> web.Response:
    """Get details about an async request

    Get details about a fileset related async request.

    :param id: ID of the request.
    :type id: str

    """
    return web.Response(status=200)


async def get_fileset_snapshot(request: web.Request, id, verbose=None) -> web.Response:
    """Get information for a fileset snapshot

    Retrieve summary information for a fileset snapshot by specifying the snapshot ID.

    :param id: ID of snapshot.
    :type id: str
    :param verbose: Whether or not to fetch verbose fileset snapshot information. The performance of this endpoint will decrease if set to true.
    :type verbose: bool

    """
    return web.Response(status=200)


async def get_missed_fileset_snapshots(request: web.Request, id) -> web.Response:
    """Get missed snapshots for a fileset

    Retrieve summary information about all missed snapshots for a fileset.

    :param id: ID of the fileset.
    :type id: str

    """
    return web.Response(status=200)


async def query_fileset(request: web.Request, primary_cluster_id=None, host_id=None, share_id=None, is_relic=None, effective_sla_domain_id=None, template_id=None, limit=None, offset=None, name=None, host_name=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary information for all filesets

    Retrieve summary information for each fileset. Optionally, filter the retrieved information.

    :param primary_cluster_id: Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
    :type primary_cluster_id: str
    :param host_id: Filter the summary information based on the ID of the host referenced by the fileset.
    :type host_id: str
    :param share_id: Filter the summary information based on the ID of the host share referenced by the fileset. Use **_NONE_** to only return information for filesets that were not created based on a host share. Use **_ANY_** to only return information for filesets that were created based on a host share.
    :type share_id: str
    :param is_relic: Filter the summary information based on the relic status of the fileset. Returns both relic and non relic if the parameter is not set.
    :type is_relic: bool
    :param effective_sla_domain_id: Filter the summary information based on the ID of the effective SLA Domain inherited by a fileset. Use **_UNPROTECTED_** to only return information for filesets that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for filesets that do have an effective SLA Domain.
    :type effective_sla_domain_id: str
    :param template_id: Filter the summary information based on the ID of a fileset template.  Use **_NONE_** to only return information for filesets that were not created from a fileset template.  Use **_ANY_** to only return information for filesets that were created from a fileset template.
    :type template_id: str
    :param limit: Limit the summary information to a specified maximum number of filesets.  Optionally, use with **_offset_** to start the count at a specified point.  Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort.
    :type limit: int
    :param offset: Starting position in the list of fileset entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of results.
    :type offset: int
    :param name: Retrieve filesets with a name matching the provided name. The search is performed as a case-insensitive infix search.
    :type name: str
    :param host_name: Retrieve filesets with a host name matching the provided name. The search is performed as a case-insensitive infix search.
    :type host_name: str
    :param sort_by: Specifies a comma-separated list of fileset attributes to use in sorting the fileset summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified.  Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def search_fileset(request: web.Request, id, path, limit=None, cursor=None) -> web.Response:
    """Search for a file within the fileset

    Search for a file within the fileset. Search via full path prefix or filename prefix.

    :param id: Fileset ID to search.
    :type id: str
    :param path: The path query. Either path prefix or filename prefix.
    :type path: str
    :param limit: Maximum number of entries in the response.
    :type limit: int
    :param cursor: Pagination cursor returned by the previous request.
    :type cursor: str

    """
    return web.Response(status=200)


async def update_fileset(request: web.Request, id, body) -> web.Response:
    """Update a Fileset

    Update a Fileset with the specified properties.

    :param id: ID of the Fileset. to update.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = FilesetUpdate.from_dict(body)
    return web.Response(status=200)
