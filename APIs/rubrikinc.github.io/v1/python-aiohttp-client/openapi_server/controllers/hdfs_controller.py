from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.browse_response_list_response import BrowseResponseListResponse
from openapi_server.models.hdfs_create import HdfsCreate
from openapi_server.models.hdfs_detail import HdfsDetail
from openapi_server.models.hdfs_export_file_job_config import HdfsExportFileJobConfig
from openapi_server.models.hdfs_restore_file_job_config import HdfsRestoreFileJobConfig
from openapi_server.models.hdfs_snapshot_detail import HdfsSnapshotDetail
from openapi_server.models.hdfs_summary_list_response import HdfsSummaryListResponse
from openapi_server.models.hdfs_update import HdfsUpdate
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.search_response_list_response import SearchResponseListResponse
from openapi_server import util


async def browse_hdfs_snapshot(request: web.Request, id, path, offset=None, limit=None) -> web.Response:
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


async def create_hdfs(request: web.Request, body) -> web.Response:
    """Create one HDFS directory for a host

    Create a HDFS directory for a network host. A HDFS directory is a HDFS directory template applied to a host.

    :param body: Specify a template ID and a host ID.
    :type body: dict | bytes

    """
    body = HdfsCreate.from_dict(body)
    return web.Response(status=200)


async def create_hdfs_backup_job(request: web.Request, id, body=None) -> web.Response:
    """Initiate an on-demand backup for a HDFS directory

    Create on-demand backup request for HDFS directory.

    :param id: ID of the HDFS directory.
    :type id: str
    :param body: Configuration for the on-demand backup.
    :type body: dict | bytes

    """
    body = BaseOnDemandSnapshotConfig.from_dict(body)
    return web.Response(status=200)


async def create_hdfs_export_file_job(request: web.Request, id, body) -> web.Response:
    """Create export job

    Initiate a job to copy a file or folder from a hdfs backup to a destination host other than the source host. Returns the job instance ID.

    :param id: ID of snapshot.
    :type id: str
    :param body: Configuration for job to export a file or folder from a hdfs backup.
    :type body: dict | bytes

    """
    body = HdfsExportFileJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_hdfs_restore_file_job(request: web.Request, id, body) -> web.Response:
    """Create restore job

    Initiate a job to copy a file or folder from a HDFS directory backup to the source host. Returns the job instance ID.

    :param id: ID of snapshot.
    :type id: str
    :param body: Configuration for job to restore a file or folder from a HDFS directory backup.
    :type body: dict | bytes

    """
    body = HdfsRestoreFileJobConfig.from_dict(body)
    return web.Response(status=200)


async def delete_hdfs(request: web.Request, id, preserve_snapshots=None) -> web.Response:
    """Delete a HDFS directory

    Delete a HDFS directory by specifying the HDFS directory ID.

    :param id: Provide a HDFS directory ID to delete.
    :type id: str
    :param preserve_snapshots: A flag that indicates whether the snapshots of the HDFS directory are preserved or deleted. By default, snapshots are preserved.
    :type preserve_snapshots: bool

    """
    return web.Response(status=200)


async def delete_hdfs_snapshot(request: web.Request, id) -> web.Response:
    """Delete a HDFS directory snapshot

    Delete a HDFS directory snapshot. A snapshot is deleted only if it is an on-demand snapshot, or a snapshot of an unprotected HDFS directory.

    :param id: ID of snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def delete_hdfs_snapshots(request: web.Request, id) -> web.Response:
    """Delete all snapshots of a HDFS directory

    Delete all snapshots that were created based on a hdfs by providing the HDFS directory ID. Requires an unprotected HDFS directory. Remove the HDFS directory from all SLA Domains.

    :param id: ID of the HDFS directory.
    :type id: str

    """
    return web.Response(status=200)


async def get_hdfs(request: web.Request, id) -> web.Response:
    """Get information for a single HDFS directory

    Retrieve summary information for a HDFS directory by specifying the HDFS directory ID.

    :param id: Specify the HDFS directory ID.
    :type id: str

    """
    return web.Response(status=200)


async def get_hdfs_async_request_status(request: web.Request, id) -> web.Response:
    """Get details about an asynchronous request

    Get details about a hdfs related asynchronous request.

    :param id: ID of the request.
    :type id: str

    """
    return web.Response(status=200)


async def get_hdfs_snapshot(request: web.Request, id) -> web.Response:
    """Get information for a HDFS directory snapshot

    Retrieve summary information for a HDFS directory snapshot by specifying the snapshot ID.

    :param id: ID of snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def get_missed_hdfs_snapshots(request: web.Request, id) -> web.Response:
    """Get missed snapshots for a HDFS directory

    Retrieve summary information about all missed snapshots for a HDFS directory.

    :param id: ID of the HDFS directory.
    :type id: str

    """
    return web.Response(status=200)


async def query_hdfs(request: web.Request, primary_cluster_id=None, host_id=None, is_relic=None, effective_sla_domain_id=None, template_id=None, limit=None, offset=None, name=None, host_name=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary information for all HDFS directories

    Retrieve summary information for each HDFS directory. Optionally, filter the retrieved information.

    :param primary_cluster_id: Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
    :type primary_cluster_id: str
    :param host_id: Filter the summary information based on the ID of the host referenced by the HDFS directory (name node).
    :type host_id: str
    :param is_relic: Filter the summary information based on the relic status of the HDFS directory. When this parameter is not set, the returned HDFS directory summary information is not filtered by relic status.
    :type is_relic: bool
    :param effective_sla_domain_id: Filter the summary information based on the ID of the effective SLA Domain inherited by a HDFS directory. Use **_UNPROTECTED_** to only return information for HDFS directories that do not have an effective SLA Domain. Use **_PROTECTED_** to only return information for HDFS directories that have an effective SLA Domain.
    :type effective_sla_domain_id: str
    :param template_id: Filter the summary information based on the ID of a HDFS directory template. Use **_NONE_** to only return information for HDFS directories that were not created from a HDFS directory template. Use **_ANY_** to only return information for HDFS directories that were created from a HDFS directory template.
    :type template_id: str
    :param limit: Limit the summary information to a specified maximum number of HDFS directories. Optionally, use with **_offset_** to start the count at a specified point. Optionally, use with **_sort_by_** to perform sort on given attributes. Include **_sort_order_** to determine the ascending or descending direction of sort.
    :type limit: int
    :param offset: Starting position in the list of HDFS directory entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as a collection of grouped entries for paging.
    :type offset: int
    :param name: Retrieve HDFS directories with a name matching the provided name. The search is performed as a case-insensitive infix search.
    :type name: str
    :param host_name: Retrieve HDFS directories with a host name (name node) matching the provided name. The search is performed as a case-insensitive infix search.
    :type host_name: str
    :param sort_by: Specifies a comma-separated list of HDFS directory attributes to use in sorting the HDFS directory summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified. Valid attributes are: **_name_**, **_hostName_**, **_templateType_**, **_slaName_**, **_includes_**, **_excludes_**, and **_exceptions_**. Requires **_sort_order_**.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def search_hdfs(request: web.Request, id, path, limit=None, cursor=None) -> web.Response:
    """Search for a file within the HDFS directory

    Search for a file within the HDFS directory. Search using full path prefix or filename prefix.

    :param id: HDFS directory ID to search.
    :type id: str
    :param path: The path query. The query can be a path refix or a filename prefix.
    :type path: str
    :param limit: Maximum number of entries in the response.
    :type limit: int
    :param cursor: Pagination cursor returned by the previous request.
    :type cursor: str

    """
    return web.Response(status=200)


async def update_hdfs(request: web.Request, id, body) -> web.Response:
    """Update a HDFS directory

    Update a HDFS directory with the specified properties.

    :param id: ID of the HDFS directory to update.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = HdfsUpdate.from_dict(body)
    return web.Response(status=200)
