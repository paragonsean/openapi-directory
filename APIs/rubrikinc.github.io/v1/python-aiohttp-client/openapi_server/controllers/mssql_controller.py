from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.count_response import CountResponse
from openapi_server.models.download_mssql_backup_files_by_id_job_config import DownloadMssqlBackupFilesByIdJobConfig
from openapi_server.models.export_mssql_db_job_config import ExportMssqlDbJobConfig
from openapi_server.models.internal_job_instance_detail import InternalJobInstanceDetail
from openapi_server.models.job_scheduled_response import JobScheduledResponse
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.mount_mssql_db_config import MountMssqlDbConfig
from openapi_server.models.mssql_availability_group_detail import MssqlAvailabilityGroupDetail
from openapi_server.models.mssql_availability_group_summary_list_response import MssqlAvailabilityGroupSummaryListResponse
from openapi_server.models.mssql_availability_group_update import MssqlAvailabilityGroupUpdate
from openapi_server.models.mssql_backup_job_config import MssqlBackupJobConfig
from openapi_server.models.mssql_backup_selection import MssqlBackupSelection
from openapi_server.models.mssql_backups import MssqlBackups
from openapi_server.models.mssql_batch_backup_job_config import MssqlBatchBackupJobConfig
from openapi_server.models.mssql_batch_backup_summary import MssqlBatchBackupSummary
from openapi_server.models.mssql_db_defaults import MssqlDbDefaults
from openapi_server.models.mssql_db_defaults_update import MssqlDbDefaultsUpdate
from openapi_server.models.mssql_db_detail import MssqlDbDetail
from openapi_server.models.mssql_db_snapshot_detail import MssqlDbSnapshotDetail
from openapi_server.models.mssql_db_snapshot_summary_list_response import MssqlDbSnapshotSummaryListResponse
from openapi_server.models.mssql_db_summary_list_response import MssqlDbSummaryListResponse
from openapi_server.models.mssql_db_update import MssqlDbUpdate
from openapi_server.models.mssql_db_update_id import MssqlDbUpdateId
from openapi_server.models.mssql_download_from_archive_config import MssqlDownloadFromArchiveConfig
from openapi_server.models.mssql_hierarchy_object_summary import MssqlHierarchyObjectSummary
from openapi_server.models.mssql_hierarchy_object_summary_list_response import MssqlHierarchyObjectSummaryListResponse
from openapi_server.models.mssql_host_configuration import MssqlHostConfiguration
from openapi_server.models.mssql_host_configuration_with_host_id import MssqlHostConfigurationWithHostId
from openapi_server.models.mssql_host_configuration_with_host_id_list_response import MssqlHostConfigurationWithHostIdListResponse
from openapi_server.models.mssql_instance_detail import MssqlInstanceDetail
from openapi_server.models.mssql_instance_summary_list_response import MssqlInstanceSummaryListResponse
from openapi_server.models.mssql_instance_update import MssqlInstanceUpdate
from openapi_server.models.mssql_log_shipping_create_config import MssqlLogShippingCreateConfig
from openapi_server.models.mssql_log_shipping_detail import MssqlLogShippingDetail
from openapi_server.models.mssql_log_shipping_reseed_config import MssqlLogShippingReseedConfig
from openapi_server.models.mssql_log_shipping_summary_list_response import MssqlLogShippingSummaryListResponse
from openapi_server.models.mssql_log_shipping_update import MssqlLogShippingUpdate
from openapi_server.models.mssql_missed_recoverable_range_list_response import MssqlMissedRecoverableRangeListResponse
from openapi_server.models.mssql_mount_detail import MssqlMountDetail
from openapi_server.models.mssql_mount_summary_list_response import MssqlMountSummaryListResponse
from openapi_server.models.mssql_recoverable_range_list_response import MssqlRecoverableRangeListResponse
from openapi_server.models.mssql_restore_estimate_result import MssqlRestoreEstimateResult
from openapi_server.models.mssql_restore_file import MssqlRestoreFile
from openapi_server.models.mssql_sla_domain_assign_info import MssqlSlaDomainAssignInfo
from openapi_server.models.mssql_snappable_id import MssqlSnappableId
from openapi_server.models.protected_objects_count import ProtectedObjectsCount
from openapi_server.models.restore_mssql_db_job_config import RestoreMssqlDbJobConfig
from openapi_server import util


async def assign_mssql_sla_properties(request: web.Request, body) -> web.Response:
    """Assign SLA properties to SQL Server objects

    Assigns SLA Domain properties to SQL Server objects. Hosts and Windows clusters cannot be assigned SLA Domains directly. The SLA Domains are instead applied to the SQL Server child objects within the Host or Windows Cluster object. Newly discovered SQL Server objects within a given Host or Windows Cluster object do not inherit SLA Domain properties from other child SQL Server objects with the same parent object. 

    :param body: Update information.
    :type body: dict | bytes

    """
    body = MssqlSlaDomainAssignInfo.from_dict(body)
    return web.Response(status=200)


async def browse_mssql_backup_files(request: web.Request, id, body) -> web.Response:
    """List snapshots and logs from a Microsoft SQL database

    When a recovery point is set, this API endpoint returns the snapshot and list of logs needed to restore the database to the recovery point. When a time range or LSN range is specified, this API endpoint returns the snapshots and logs that overlap the specified range. Specify only a recovery point or a range. Specify only LSNs or times. This endpoint is only used to fetch data, but uses POST instead of GET due to limitations on parameters used in the body of a GET request. The parameter set for this endpoint is shared with the download_file endpoint. 

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param body: Configuration for the browse request.
    :type body: dict | bytes

    """
    body = MssqlBackupSelection.from_dict(body)
    return web.Response(status=200)


async def bulk_update_mssql_db_v1(request: web.Request, body) -> web.Response:
    """Update multiple Microsoft SQL databases

    Update multiple Microsoft SQL databases with the specified properties.

    :param body: Properties to update for each database.
    :type body: list | bytes

    """
    body = [MssqlDbUpdateId.from_dict(d) for d in body]
    return web.Response(status=200)


async def count_mssql_db_v1(request: web.Request, root_id=None) -> web.Response:
    """Returns a count of Microsoft SQL databases

    Returns a count of Microsoft SQL databases.

    :param root_id: Include only instances that belong to this root.
    :type root_id: str

    """
    return web.Response(status=200)


async def count_mssql_instance_v1(request: web.Request, ) -> web.Response:
    """Returns a count of Microsoft SQL instances

    Returns a count of all Microsoft SQL instances.


    """
    return web.Response(status=200)


async def create_download_mssql_backup_files(request: web.Request, id, body) -> web.Response:
    """Download snapshots and logs backups from a Microsoft SQL Database

    Starts an asynchronous request to download a set of backup files as a single compressed zipfile. When a recovery point is set, this API endpoint returns the snapshot and list of logs that Rubrik CDM would use to restore the database to the recovery point. When a time range or LSN range is specified, this API endpoint returns the snapshots and logs that overlap the specified range. Specify only a point in time or a range. Specify only LSNs or times. 

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param body: Configuration for a download files job.
    :type body: dict | bytes

    """
    body = MssqlBackupSelection.from_dict(body)
    return web.Response(status=200)


async def create_download_mssql_backup_files_by_id(request: web.Request, id, body) -> web.Response:
    """Downloads a list of snapshot and log backups from a Microsoft SQL database

    Downloads a list of snapshot and log backups from a Microsoft SQL database.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param body: Configuration for a download files by id job.
    :type body: dict | bytes

    """
    body = DownloadMssqlBackupFilesByIdJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_export_mssql_db(request: web.Request, id, body) -> web.Response:
    """Export a Microsoft SQL database to a new location

    Create a request to export a Microsoft SQL database. To check the result of the request, poll /mssql/request/{id}.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param body: Configuration for the export.
    :type body: dict | bytes

    """
    body = ExportMssqlDbJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_log_shipping_configuration(request: web.Request, id, body) -> web.Response:
    """Create a log shipping configuration

    Create a log shipping configuration between a specified primary database and a specified secondary database. The transaction logs from the primary database are regularly restored to the secondary database in order to maintain the secondary database as a point-in-time copy of the primary database. The primary database must have log backups configured, and it must be in the full or bulk-logged recovery model.

    :param id: ID of the primary database object.
    :type id: str
    :param body: Object containing the values of a log shipping configuration.
    :type body: dict | bytes

    """
    body = MssqlLogShippingCreateConfig.from_dict(body)
    return web.Response(status=200)


async def create_mssql_host_config(request: web.Request, body) -> web.Response:
    """Create a SQL Server host configuration

    Creates a SQL Server host configuration.

    :param body: Parameters for creating a SQL Server host configuration.
    :type body: dict | bytes

    """
    body = MssqlHostConfigurationWithHostId.from_dict(body)
    return web.Response(status=200)


async def create_mssql_mount(request: web.Request, id, body) -> web.Response:
    """Live Mount SQL Server database from a point in time copy

    Create an asynchronous request to create a Live Mount SQL Server database. Poll the task status by using /mssql/request/{id}.

    :param id: ID of the SQL Server database.
    :type id: str
    :param body: Configuration for the Live Mount.
    :type body: dict | bytes

    """
    body = MountMssqlDbConfig.from_dict(body)
    return web.Response(status=200)


async def create_mssql_unmount(request: web.Request, id, force=None) -> web.Response:
    """Delete a Live Mount of a SQL Server database

    Create an async request to delete a Live Mount of a SQL Server database. Poll the task status by using /mssql/request/{id}.

    :param id: ID of the Live Mount to delete.
    :type id: str
    :param force: Remove all data within the Rubrik cluster related to the Live Mount, even if the SQL Server database cannot be contacted. Default value is false.
    :type force: bool

    """
    return web.Response(status=200)


async def create_on_demand_mssql_backup(request: web.Request, id, body) -> web.Response:
    """Take an on-demand backup of a Microsoft SQL database

    Take an on-demand backup of a Microsoft SQL database. The forceFullSnapshot property can be set to true to force a full snapshot. To check the result of the request, poll /mssql/request/{id}.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param body: Configuration for the on-demand backup.
    :type body: dict | bytes

    """
    body = MssqlBackupJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_on_demand_mssql_batch_backup_v1(request: web.Request, body) -> web.Response:
    """Take an on-demand backup of multiple Microsoft SQL databases

    Take an on-demand backup of one or more Microsoft SQL databases. Set the forceFullSnapshot property to true to force a full snapshot for every database that is specified. Only one snapshot will be taken for each database, even if a database is included multiple times in the fields of the request body. To check the result of the request, poll /mssql/request/{id}.

    :param body: Configuration for the on-demand backups.
    :type body: dict | bytes

    """
    body = MssqlBatchBackupJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_on_demand_mssql_log_backup(request: web.Request, id) -> web.Response:
    """Take an on-demand log backup for a Microsoft SQL database

    Take an on-demand log backup for a Microsoft SQL database.

    :param id: ID of the Microsoft SQL database.
    :type id: str

    """
    return web.Response(status=200)


async def create_restore_mssql_db(request: web.Request, id, body) -> web.Response:
    """Restore a Microsoft SQL database

    Create a request to restore a SQL Server database. To check the result of the request, poll /mssql/request/{id}.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param body: Restore configuration.
    :type body: dict | bytes

    """
    body = RestoreMssqlDbJobConfig.from_dict(body)
    return web.Response(status=200)


async def delete_downloaded_mssql_db_recoverable_ranges_v1(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Delete downloaded recoverable ranges of a Microsoft SQL database

    Deletes all local snapshots and logs that have previously been downloaded. Provide a begin or end time to delete only the downloaded snapshots and logs that fall within this time frame. The time is relative to when the snapshot or log backup was originally taken, not downloaded. Parts of the window may not be deleted if certain log files must be kept to preserve times outside the window. Data is deleted in the background. To check the status of the deletion, poll /mssql/db/recoverable_range/download/{id}.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param after_time: Delete only the downloaded snapshots and logs taken after this time. The date-time string should be in ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678\&quot;.
    :type after_time: str
    :param before_time: Delete only the downloaded snapshots and logs taken before this time. The date-time string should be in ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def delete_log_shipping_configuration(request: web.Request, id, delete_secondary_database=None) -> web.Response:
    """Delete a specified log shipping configuration

    Deletes the specified log shipping configuration.

    :param id: ID of a log shipping configuration object.
    :type id: str
    :param delete_secondary_database: Boolean value that determines whether to attempt to delete the secondary database associated with the specified log shipping configuration. The default value is false. When set to false, no attempt is made to delete the secondary database. When set to true, starts an asynchronous job to delete the secondary database.
    :type delete_secondary_database: bool

    """
    return web.Response(status=200)


async def delete_mssql_db_snapshots(request: web.Request, id) -> web.Response:
    """Delete all snapshots of a Microsoft SQL database

    Deletes all snapshots of a Microsoft SQL database. The database must be unprotected for the operation to succeed.

    :param id: ID of the Microsoft SQL database.
    :type id: str

    """
    return web.Response(status=200)


async def delete_mssql_host_config(request: web.Request, host_id) -> web.Response:
    """Delete the SQL Server host configuration

    Deletes the SQL Server host configuration. The host falls back to use values from the global configuration.

    :param host_id: ID of the host.
    :type host_id: str

    """
    return web.Response(status=200)


async def download_from_archive(request: web.Request, id, body) -> web.Response:
    """Download snapshots and log backups from archival

    Starts an asynchronous request to download snapshots and logs from archival for a given database and recovery point. If the specified point in time is already available locally, this endpoint throws an error. 

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param body: Configuration for the archive download request.
    :type body: dict | bytes

    """
    body = MssqlDownloadFromArchiveConfig.from_dict(body)
    return web.Response(status=200)


async def get_compatible_mssql_instances_v1(request: web.Request, id, recovery_type, recovery_time=None) -> web.Response:
    """Get compatible instances for the recovery of a Microsoft SQL database

    Returns all compatible instances for export for the specified recovery time.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param recovery_type: Recovery type.
    :type recovery_type: str
    :param recovery_time: Time, in ISO8601 format, to recover to. For example \&quot;2016-01-01T01:23:45.678Z\&quot;. If this is not specified, the latest recoverable time is used.
    :type recovery_time: str

    """
    recovery_time = util.deserialize_datetime(recovery_time)
    return web.Response(status=200)


async def get_default_db_properties_v1(request: web.Request, ) -> web.Response:
    """Returns the current default properties for Microsoft SQL databases

    The default properties are Log Backup Frequency (in seconds), Log Retention Time (in hours) and CBT status. New databases added to the Rubrik cluster are provided the log backup frequency value and log backup retention value by default. New hosts added to the Rubrik cluster are provided the CBT status by default.


    """
    return web.Response(status=200)


async def get_delete_mssql_db_recoverable_ranges_status_v1(request: web.Request, id) -> web.Response:
    """Get the deletion status of downloaded recoverable ranges

    Get the details of the progress made in deleting recoverable ranges. The recoverable ranges to delete are those specified by the DELETE request to /mssql/db/{id}/recoverable_range/download which yielded the response with the job id.

    :param id: Job ID of the deletion for which to check progress.
    :type id: str

    """
    return web.Response(status=200)


async def get_log_shipping_configuration(request: web.Request, id) -> web.Response:
    """Get a log shipping configuration

    Retrieves a particular log shipping configuration with all the details of the configuration.

    :param id: ID of a log shipping configuration.
    :type id: str

    """
    return web.Response(status=200)


async def get_missed_mssql_db_snapshots(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Get summary information for missed snapshots of a SQL database

    Returns a list of summary information for the missed snapshots of a Microsoft SQL database, including the time of day and the locations where the snapshot was missed.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param after_time: Filter snapshots to those missed on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type after_time: str
    :param before_time: Filter snapshots to those missed on or before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_mssql_async_request_status(request: web.Request, id) -> web.Response:
    """Get details for an async request

    Returns the task object for an async request related to SQL Server databases.

    :param id: ID of the async request.
    :type id: str

    """
    return web.Response(status=200)


async def get_mssql_availability_group_v1(request: web.Request, id) -> web.Response:
    """Returns detailed information for a Microsoft SQL availability group

    Returns a detailed view of a Microsoft SQL availability group.

    :param id: ID of the Microsoft SQL availability group to fetch.
    :type id: str

    """
    return web.Response(status=200)


async def get_mssql_db(request: web.Request, id) -> web.Response:
    """Get detailed information for a Microsoft SQL database

    Returns a detailed view of a Microsoft SQL database.

    :param id: ID of the Microsoft SQL database to fetch.
    :type id: str

    """
    return web.Response(status=200)


async def get_mssql_db_missed_recoverable_ranges(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Get missed recoverable ranges of a Microsoft SQL database

    Retrieve a list of missed recoverable ranges for a Microsoft SQL database. For each run of one type of error, the first and last occurrence of the error are given.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param after_time: Filter the missed ranges to end after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type after_time: str
    :param before_time: Filter the missed ranges to start before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_mssql_db_recoverable_ranges(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Get recoverable ranges of a Microsoft SQL database

    Retrieve the recoverable ranges for a specified Microsoft SQL database. A begin and/or end timestamp can be provided to retrieve only the ranges that fall within the window.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param after_time: Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678Z\&quot;.
    :type after_time: str
    :param before_time: Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_mssql_db_snapshot(request: web.Request, id) -> web.Response:
    """Get details information about a Microsoft SQL database snapshot

    Returns detailed information about a Microsoft SQL database snapshot.

    :param id: ID of the snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def get_mssql_hierarchy_children(request: web.Request, id, effective_sla_domain_id=None, object_type=None, primary_cluster_id=None, limit=None, offset=None, name=None, is_relic=None, is_live_mount=None, is_log_shipping_secondary=None, is_clustered=None, has_instances=None, sla_assignment=None, sort_by=None, sort_order=None, snappable_status=None) -> web.Response:
    """Get list of immediate descendant objects

    Retrieve the list of immediate descendant objects for the specified parent.

    :param id: ID of the parent SQL Server hierarchy object. To get top-level nodes, use **root** as the ID. 
    :type id: str
    :param effective_sla_domain_id: Filter by the ID of the effective SLA Domain.
    :type effective_sla_domain_id: str
    :param object_type: Filter by a comma-separated list of node object types. 
    :type object_type: List[str]
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: An integer that specifies the number of initial matches to ignore. 
    :type offset: int
    :param name: Filter children by provided name.
    :type name: str
    :param is_relic: Filter by the value of the &#x60;isRelic&#x60; field for nodes with object type MssqlDatabase.
    :type is_relic: bool
    :param is_live_mount: Filter database by the value of the &#x60;isLiveMount&#x60; field for nodes with object type MssqlDatabase.
    :type is_live_mount: bool
    :param is_log_shipping_secondary: Filter by the value of the &#x60;isLogShippingSecondary&#x60; field for nodes with object type MssqlDatabase.
    :type is_log_shipping_secondary: bool
    :param is_clustered: Filter by the value of the &#x60;isClustered&#x60; field for nodes with object type MssqlDatabase or MssqlInstance.
    :type is_clustered: bool
    :param has_instances: Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is &#39;true,&#39; the filter shows only nodes with children MssqlInstance nodes. When this value is &#39;false,&#39; the filter shows only nodes without children MssqlInstance nodes.
    :type has_instances: bool
    :param sla_assignment: Filter by SLA assignment type.
    :type sla_assignment: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str
    :param snappable_status: Determines whether SQL Server instances are fetched with additional privilege checks.
    :type snappable_status: str

    """
    return web.Response(status=200)


async def get_mssql_hierarchy_descendants(request: web.Request, id, effective_sla_domain_id=None, object_type=None, primary_cluster_id=None, limit=None, offset=None, name=None, is_relic=None, is_live_mount=None, is_log_shipping_secondary=None, is_clustered=None, has_instances=None, sla_assignment=None, sort_by=None, sort_order=None, snappable_status=None) -> web.Response:
    """Get list of descendant objects

    Retrieve the list of descendant objects for the specified parent.

    :param id: ID of the parent SQL server hierarchy object. To get top-level nodes, use **root** as the ID. 
    :type id: str
    :param effective_sla_domain_id: Filter by the ID of the effective SLA Domain.
    :type effective_sla_domain_id: str
    :param object_type: Filter by a comma-separated list of node object types. 
    :type object_type: List[str]
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: An integer that specifies the number of initial matches to ignore. 
    :type offset: int
    :param name: Filter descendants by provided name.
    :type name: str
    :param is_relic: Filter by the value of the &#x60;isRelic&#x60; field for nodes with MssqlDatabase as the value of the object type field.
    :type is_relic: bool
    :param is_live_mount: Filter database by the value of the &#x60;isLiveMount&#x60; field for nodes with MssqlDatabase as the value of the object type field.
    :type is_live_mount: bool
    :param is_log_shipping_secondary: Filter by the value of the &#x60;isLogShippingSecondary&#x60; field for nodes with MssqlDatabase as the value of the object type field.
    :type is_log_shipping_secondary: bool
    :param is_clustered: Filter by the value of the &#x60;isClustered&#x60; field for nodes with object type MssqlDatabase or MssqlInstance.
    :type is_clustered: bool
    :param has_instances: Boolean that filters top-level nodes with the Host or WindowsCluster object type by whether or not the nodes have children MssqlInstance nodes. When this value is &#39;true,&#39; the filter shows only nodes with children MssqlInstance nodes. When this value is &#39;false,&#39; the filter shows only nodes without children MssqlInstance nodes.
    :type has_instances: bool
    :param sla_assignment: Filter by SLA Domain assignment type.
    :type sla_assignment: str
    :param sort_by: Attribute to sort the results on.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str
    :param snappable_status: Determines whether SQL Server instances are fetched with additional privilege checks.
    :type snappable_status: str

    """
    return web.Response(status=200)


async def get_mssql_hierarchy_object(request: web.Request, id) -> web.Response:
    """Get summary of a SQL Server hierarchy object

    Retrieve details for the specified object in the SQL Server hierarchy. 

    :param id: ID of the SQL Server hierarchy object.
    :type id: str

    """
    return web.Response(status=200)


async def get_mssql_host_config(request: web.Request, host_id) -> web.Response:
    """Get the configuration for a specific host

    Returns the configuration for the specified SQL Server host.

    :param host_id: ID of the host.
    :type host_id: str

    """
    return web.Response(status=200)


async def get_mssql_instance(request: web.Request, id) -> web.Response:
    """Get detailed information for a Microsoft SQL instance

    Returns a detailed view of a Microsoft SQL instance.

    :param id: ID of the Microsoft SQL instance.
    :type id: str

    """
    return web.Response(status=200)


async def get_mssql_mount(request: web.Request, id) -> web.Response:
    """Get detailed information for a Live Mount of a SQL Server database

    Returns detailed information for the specified Live Mount of a SQL Server database.

    :param id: ID of the Live Mount to fetch.
    :type id: str

    """
    return web.Response(status=200)


async def get_on_demand_mssql_batch_backup_result_v1(request: web.Request, id) -> web.Response:
    """Returns details for an on-demand backup of multiple Microsoft SQL databases

    Returns the details for an on-demand backup of multiple Microsoft SQL databases. This only returns details for requests that have finished successfully. To check the status of the request, poll /mssql/request/{id}.

    :param id: ID of the on-demand backup request.
    :type id: str

    """
    return web.Response(status=200)


async def mssql_get_restore_files_v1(request: web.Request, id, time=None, lsn=None, recovery_fork_guid=None) -> web.Response:
    """Returns a list all database files to be restored

    Provides a list of database files to be restored for the specified restore or export operation.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param time: Time, in ISO8601 date-time format, to recover to. For example, \&quot;2016-01-01T01:23:45.678\&quot;. This value or the LSN are required.
    :type time: str
    :param lsn: LSN to recover to. This value or the time are required.
    :type lsn: str
    :param recovery_fork_guid: Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified.
    :type recovery_fork_guid: str

    """
    time = util.deserialize_datetime(time)
    return web.Response(status=200)


async def mssql_get_snappable_id_v1(request: web.Request, id) -> web.Response:
    """Returns the snappableId for a Microsoft SQL database

    Returns the snappableId for a Microsoft SQL database.

    :param id: ID of the Microsoft SQL database.
    :type id: str

    """
    return web.Response(status=200)


async def mssql_restore_estimate_v1(request: web.Request, id, time=None, lsn=None, recovery_fork_guid=None) -> web.Response:
    """Returns a size estimate for a restore or export

    Provides an estimate of resources needed for the specified restore or export operation.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param time: Time, in ISO8601 date-time format, to recover to. For example, \&quot;2016-01-01T01:23:45.678\&quot;. This value or the LSN are required.
    :type time: str
    :param lsn: LSN to recover to. This value or the LSN are required.
    :type lsn: str
    :param recovery_fork_guid: Recovery fork GUID of LSN to recover to. Meaningful only when lsn is specified.
    :type recovery_fork_guid: str

    """
    time = util.deserialize_datetime(time)
    return web.Response(status=200)


async def query_log_shipping_configurations(request: web.Request, primary_database_id=None, primary_database_name=None, secondary_database_name=None, location=None, status=None, limit=None, offset=None, sort_by=None, sort_order=None) -> web.Response:
    """Get log shipping configurations

    Retrieves all log shipping configuration objects. Results can be filtered and sorted.

    :param primary_database_id: ID of a primary database object.
    :type primary_database_id: str
    :param primary_database_name: Filter log shipping configuration objects by performing an infix search using the name of a primary database.
    :type primary_database_name: str
    :param secondary_database_name: Filter log shipping configuration objects by performing an infix search using the name of a secondary database.
    :type secondary_database_name: str
    :param location: Filter log shipping configuration objects by performing an infix search using the location string value (host/instance) for a secondary database.
    :type location: str
    :param status: Filter log shipping configuration objects based on the status value for the secondary database.
    :type status: str
    :param limit: Limit the summary information to a specified maximum number of results.
    :type limit: int
    :param offset: Starting position in the list of results contained in the response. The summary information includes the specified numbered result and all higher numbered results.
    :type offset: int
    :param sort_by: Specifies an attribute used to ASCII-sort the results. Sorting by the last_applied attribute represents the timestamp as an ISO 8601-encoded string.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def query_mssql_availability_group_v1(request: web.Request, primary_cluster_id=None) -> web.Response:
    """Returns summary information for Microsoft SQL availability groups

    Returns a list of summary information for Microsoft SQL availability groups.

    :param primary_cluster_id: Filter by primary cluster.
    :type primary_cluster_id: str

    """
    return web.Response(status=200)


async def query_mssql_db(request: web.Request, instance_id=None, availability_group_id=None, effective_sla_domain_id=None, primary_cluster_id=None, name=None, sla_assignment=None, limit=None, offset=None, is_relic=None, is_live_mount=None, is_log_shipping_secondary=None, sort_by=None, sort_order=None, include_backup_task_info=None) -> web.Response:
    """Get summary information for SQL Server databases

    Returns a list of summary information for Microsoft SQL databases.

    :param instance_id: Filter by Microsoft SQL instance.
    :type instance_id: str
    :param availability_group_id: Filter by the &#x60;id&#x60; of an Always On Availability Group.
    :type availability_group_id: str
    :param effective_sla_domain_id: Filter by effective SLA domain.
    :type effective_sla_domain_id: str
    :param primary_cluster_id: Filter by primary cluster.
    :type primary_cluster_id: str
    :param name: Filter by a substring of the database name.
    :type name: str
    :param sla_assignment: SLA Assignment of the database.
    :type sla_assignment: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: An integer that specifies a number of initial matches to ignore.
    :type offset: int
    :param is_relic: Filter database summary information by the value of the &#x60;isRelic&#x60; field.
    :type is_relic: bool
    :param is_live_mount: Filter database summary information by the value of the &#x60;isLiveMount&#x60; field.
    :type is_live_mount: bool
    :param is_log_shipping_secondary: Filter database summary information by the value of the &#x60;isLogShippingSecondary&#x60; field.
    :type is_log_shipping_secondary: bool
    :param sort_by: Specifies the SQL Server Database attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str
    :param include_backup_task_info: Include backup task information in response.
    :type include_backup_task_info: bool

    """
    return web.Response(status=200)


async def query_mssql_db_snapshot(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Get summary information for snapshots of a Microsoft SQL database

    Returns a list of summary information for snapshots of a Microsoft SQL database.

    :param id: ID of the Microsoft SQL database.
    :type id: str
    :param after_time: Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type after_time: str
    :param before_time: Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def query_mssql_host_config(request: web.Request, host_id=None) -> web.Response:
    """Get the summary of SQL Server host configurations

    Returns a list of customized SQL Server host configurations.

    :param host_id: IDs of the hosts.
    :type host_id: List[str]

    """
    return web.Response(status=200)


async def query_mssql_instance(request: web.Request, root_id=None, primary_cluster_id=None, snappable_status=None) -> web.Response:
    """Get summary information for Microsoft SQL instances

    Returns a list of summary information for Microsoft SQL instances.

    :param root_id: Include only instances that belong to this root.
    :type root_id: str
    :param primary_cluster_id: Limits the instances returned within one cluster specified by primary_cluster_id.
    :type primary_cluster_id: str
    :param snappable_status: Determines whether SQL Server instances are fetched with additional privilege checks.
    :type snappable_status: str

    """
    return web.Response(status=200)


async def query_mssql_mount(request: web.Request, source_database_id=None, source_database_name=None, target_instance_id=None, mounted_database_name=None, sort_by=None, sort_order=None, offset=None, limit=None) -> web.Response:
    """Get summary information for all Live Mounts SQL Server databases

    Returns a list with summary information for all Live Mount SQL Server databases.

    :param source_database_id: Filters by the ID of the source SQL Server database.
    :type source_database_id: str
    :param source_database_name: Filters by the name of the source SQL Server database using infix search.
    :type source_database_name: str
    :param target_instance_id: Filters by the ID of the target SQL Server instance.
    :type target_instance_id: str
    :param mounted_database_name: Filters by the name of the mounted SQL Server database using infix search.
    :type mounted_database_name: str
    :param sort_by: Specifies the SQL Server Live Mount attribute to use in sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
    :type sort_by: str
    :param sort_order: Specifies the sort order, either ascending or descending. Default order is ascending.
    :type sort_order: str
    :param offset: Returns the portion of the ordered list that starts after the element specified by the offset number.
    :type offset: int
    :param limit: Sets the maximum number of a elements to include in the data array of the response.
    :type limit: int

    """
    return web.Response(status=200)


async def reseed_secondary(request: web.Request, id, body) -> web.Response:
    """Reseed a secondary database

    Starts an asynchronous job to reseed a secondary database. Reseeding restores the data in the secondary database based on a log shipping configuration.

    :param id: ID of the log shipping configuration object for the specified secondary database.
    :type id: str
    :param body: Configuration parameters for the reseed operation.
    :type body: dict | bytes

    """
    body = MssqlLogShippingReseedConfig.from_dict(body)
    return web.Response(status=200)


async def update_default_db_properties_v1(request: web.Request, body) -> web.Response:
    """Update the default properties for Microsoft SQL databases

    The default properties are Log Backup Frequency (in seconds), Log Retention Time (in hours) and CBT status. New databases added to the Rubrik cluster are provided the log backup frequency value and log backup retention value by default. New hosts added to the Rubrik cluster are provided the CBT status by default.

    :param body: Updated default properties.
    :type body: dict | bytes

    """
    body = MssqlDbDefaultsUpdate.from_dict(body)
    return web.Response(status=200)


async def update_log_shipping_configuration(request: web.Request, id, body) -> web.Response:
    """Update a specified log shipping configuration

    Updates a specified log shipping configuration.

    :param id: ID of a log shipping configuration object.
    :type id: str
    :param body: Configuration parameters for the update operation.
    :type body: dict | bytes

    """
    body = MssqlLogShippingUpdate.from_dict(body)
    return web.Response(status=200)


async def update_mssql_availability_group_v1(request: web.Request, id, body) -> web.Response:
    """Update a Microsoft SQL availability group

    Update a Microsoft SQL availability group with the specified properties.

    :param id: ID of the Microsoft SQL availability group to update.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = MssqlAvailabilityGroupUpdate.from_dict(body)
    return web.Response(status=200)


async def update_mssql_db(request: web.Request, id, body) -> web.Response:
    """Update a Microsoft SQL database

    Update a Microsoft SQL database with the specified properties.

    :param id: ID of the Microsoft SQL database to update.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = MssqlDbUpdate.from_dict(body)
    return web.Response(status=200)


async def update_mssql_host_config(request: web.Request, host_id, body) -> web.Response:
    """Update host configuration

    Updates the configuration for a specified host.

    :param host_id: ID of the SQL Server host to update the host configuration.
    :type host_id: str
    :param body: SQL Server host configuration properties to update.
    :type body: dict | bytes

    """
    body = MssqlHostConfiguration.from_dict(body)
    return web.Response(status=200)


async def update_mssql_instance(request: web.Request, id, body) -> web.Response:
    """Update a Microsoft SQL instance

    Update a Microsoft SQL instance with specified properties.

    :param id: ID of the Microsoft SQL instance.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = MssqlInstanceUpdate.from_dict(body)
    return web.Response(status=200)
