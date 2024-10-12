from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.sap_hana_add_system_response import SapHanaAddSystemResponse
from openapi_server.models.sap_hana_database_detail import SapHanaDatabaseDetail
from openapi_server.models.sap_hana_database_patch import SapHanaDatabasePatch
from openapi_server.models.sap_hana_database_snapshot_detail import SapHanaDatabaseSnapshotDetail
from openapi_server.models.sap_hana_database_snapshot_summary_list_response import SapHanaDatabaseSnapshotSummaryListResponse
from openapi_server.models.sap_hana_database_summary_list_response import SapHanaDatabaseSummaryListResponse
from openapi_server.models.sap_hana_patch_system_response import SapHanaPatchSystemResponse
from openapi_server.models.sap_hana_recoverable_range_list_response import SapHanaRecoverableRangeListResponse
from openapi_server.models.sap_hana_restore_source_config import SapHanaRestoreSourceConfig
from openapi_server.models.sap_hana_system_config import SapHanaSystemConfig
from openapi_server.models.sap_hana_system_patch import SapHanaSystemPatch
from openapi_server.models.sap_hana_system_summary import SapHanaSystemSummary
from openapi_server.models.sap_hana_system_summary_list_response import SapHanaSystemSummaryListResponse
from openapi_server import util


async def add_sap_hana_system(request: web.Request, body) -> web.Response:
    """Add a SAP HANA system

    Add a SAP HANA system to the Rubrik cluster.

    :param body: Add a SAP HANA system to the Rubrik cluster. Contains parameters like username, list of hosts, password required while adding a SAP HANA system.
    :type body: dict | bytes

    """
    body = SapHanaSystemConfig.from_dict(body)
    return web.Response(status=200)


async def configure_sap_hana_restore(request: web.Request, id, body) -> web.Response:
    """Configure the target database for system copy restore

    Initiates a job to configure the specified target database for a system copy restore by sending metadata about the source database. System copy restore in SAP HANA is done across different databases.

    :param id: ID of the target SAP HANA database to be configured.
    :type id: str
    :param body: The object containing configuration related metadata for the source SAP HANA database.
    :type body: dict | bytes

    """
    body = SapHanaRestoreSourceConfig.from_dict(body)
    return web.Response(status=200)


async def create_on_demand_sap_hana_backup(request: web.Request, id, body=None) -> web.Response:
    """Create on demand database snapshot

    Initiates a job to take an on demand full snapshot of a specified SAP HANA database object. The GET /sap_hana/db/request/{id} endpoint can be used to monitor the progress of the job.

    :param id: ID assigned to a SAP HANA database object.
    :type id: str
    :param body: Configuration for the on demand backup.
    :type body: dict | bytes

    """
    body = BaseOnDemandSnapshotConfig.from_dict(body)
    return web.Response(status=200)


async def create_sap_hana_system_refresh(request: web.Request, id) -> web.Response:
    """Refresh SAP HANA system metadata

    Initiates a job to refresh metadata of a SAP HANA system object. The GET /sap_hana/system/request/{id} endpoint can be used to monitor the progress of the job.

    :param id: The ID of the SAP HANA system.
    :type id: str

    """
    return web.Response(status=200)


async def delete_sap_hana_db_snapshot(request: web.Request, id) -> web.Response:
    """Delete a particular full snapshot of a SAP HANA database

    Initiates a request to delete a particular full snapshot of a SAP HANA database. If the log retention period for the database is still in effect, the snapshot will be deleted when the log retention period ends.

    :param id: ID assigned to a SAP HANA database full snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def delete_sap_hana_system(request: web.Request, id) -> web.Response:
    """Delete a SAP HANA system

    Initiates a job to delete a SAP HANA system object. GET /sap_hana/system/request/{id} endpoint can be used to monitor the progress of the job.

    :param id: The ID of the SAP HANA system.
    :type id: str

    """
    return web.Response(status=200)


async def get_missed_sap_hana_db_snapshots(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Retrieve summary information for missed snapshots of a SAP HANA database

    Returns a summary of information for the missed snapshots of a SAP HANA database. Retrieve only the missed snapshots that occur between the beginning and ending timestamps.

    :param id: ID of the SAP HANA database.
    :type id: str
    :param after_time: Filter for snapshots that are missed on or after this time. The date-time string must be in ISO8601 format, for example, \&quot;2016-01-01T01:23:45.678\&quot;.
    :type after_time: str
    :param before_time: Filter for snapshots that are missed on or before this time. The date-time string must be in ISO8601 format, for example, \&quot;2016-01-01T01:23:45.678\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_sap_hana_database(request: web.Request, id) -> web.Response:
    """Get detailed information for an SAP HANA database

    Returns a detailed view of the SAP HANA database.

    :param id: The ID of the SAP HANA database.
    :type id: str

    """
    return web.Response(status=200)


async def get_sap_hana_db_async_request_status(request: web.Request, id) -> web.Response:
    """Get the status of a SAP HANA database request

    Get details about a SAP HANA database related request which includes the status of data backup job.

    :param id: ID of the request.
    :type id: str

    """
    return web.Response(status=200)


async def get_sap_hana_db_recoverable_ranges(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Get recoverable ranges of a SAP HANA database

    Retrieve the recoverable ranges for a specified SAP HANA database. Provide a beginning and/or ending timestamp to retrieve only the recoverable ranges that fall within this period of time.

    :param id: ID of the SAP HANA database.
    :type id: str
    :param after_time: Filter ranges to end after this time. The date-time string should be in an ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678Z\&quot;.
    :type after_time: str
    :param before_time: Filter ranges to start before this time. The date-time string should be in an ISO8601 format. For example, \&quot;2016-01-01T01:23:45.678Z\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_sap_hana_db_snapshot(request: web.Request, id) -> web.Response:
    """Get SAP HANA database snapshot details

    Retrieve detailed information about a full or an incremental snapshot of a SAP HANA database.

    :param id: ID of snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def get_sap_hana_system(request: web.Request, id) -> web.Response:
    """Get summary information for a SAP HANA system

    Returns a summary view of a SAP HANA system.

    :param id: The ID of the SAP HANA system.
    :type id: str

    """
    return web.Response(status=200)


async def get_sap_hana_system_async_request_status(request: web.Request, id) -> web.Response:
    """Get the status of a SAP HANA system request

    Get details about a SAP HANA system related request which includes the status of delete or refresh system job.

    :param id: The ID of the request object used to poll the status.
    :type id: str

    """
    return web.Response(status=200)


async def patch_sap_hana_database(request: web.Request, id, body) -> web.Response:
    """Update the SLA Domain for an SAP HANA database

    Update the SLA Domain that is configured for an SAP HANA database.

    :param id: The ID of the SAP HANA database.
    :type id: str
    :param body: Object containing updated SAP HANA database SLA Domain ID.
    :type body: dict | bytes

    """
    body = SapHanaDatabasePatch.from_dict(body)
    return web.Response(status=200)


async def patch_sap_hana_system(request: web.Request, id, body) -> web.Response:
    """Update the SLA Domain for a SAP HANA system

    Update the SLA Domain that is configured for a SAP HANA system.

    :param id: The ID of the SAP HANA system.
    :type id: str
    :param body: An object that contains the updated SLA Domain ID for the SAP HANA system.
    :type body: dict | bytes

    """
    body = SapHanaSystemPatch.from_dict(body)
    return web.Response(status=200)


async def query_sap_hana_databases(request: web.Request, effective_sla_domain_id=None, primary_cluster_id=None, name=None, sla_assignment=None, limit=None, offset=None, is_relic=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary information for discovered SAP HANA databases

    Returns summary information for SAP HANA databases connected to the CDM cluster.

    :param effective_sla_domain_id: The ID of the SLA Domain that controls the protection of the host.
    :type effective_sla_domain_id: str
    :param primary_cluster_id: The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases.
    :type primary_cluster_id: str
    :param name: The name of the SAP HANA database.
    :type name: str
    :param sla_assignment: The name of the SLA Domain that controls the protection of the SAP HANA database.
    :type sla_assignment: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: An integer that specifies a number of initial matches to ignore.
    :type offset: int
    :param is_relic: Specify whether the SAP HANA database is accessible on the Rubrik cluster.
    :type is_relic: bool
    :param sort_by: Specifies the SAP HANA Database attribute to use in sorting the summary information.
    :type sort_by: str
    :param sort_order: The order to sort the responses by. Valid choices are asc (ascending) and desc (descending).
    :type sort_order: str

    """
    return web.Response(status=200)


async def query_sap_hana_db_snapshot(request: web.Request, id, backup_type=None, after_time=None, before_time=None) -> web.Response:
    """Get a summary list of snapshots for a SAP HANA database

    Retrieve summary information about the full and incremental snapshots of a specified SAP HANA database.

    :param id: ID assigned to a SAP HANA database object.
    :type id: str
    :param backup_type: Filter snapshots to those of a particular backup type.
    :type backup_type: str
    :param after_time: Filter snapshots to those taken on or after this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type after_time: str
    :param before_time: Filter snapshots to those taken before or on this time. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def query_sap_hana_systems(request: web.Request, primary_cluster_id=None, sid=None, limit=None, offset=None, sort_by=None, sort_order=None) -> web.Response:
    """Get summary information for added SAP HANA systems

    Returns summary information for SAP HANA systems.

    :param primary_cluster_id: The ID of the Rubrik cluster that provides primary protection for the SAP HANA databases.
    :type primary_cluster_id: str
    :param sid: The SAP System Identification (SID) code for the SAP HANA system.
    :type sid: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: An integer that specifies a number of initial matches to ignore.
    :type offset: int
    :param sort_by: The SAP HANA system attribute to use in sorting the responses.
    :type sort_by: str
    :param sort_order: The order to sort the responses by. Valid choices are asc (ascending) and desc (descending).
    :type sort_order: str

    """
    return web.Response(status=200)


async def unconfigure_sap_hana_restore(request: web.Request, id) -> web.Response:
    """Reset the configuration for system copy restore on target database

    Initiates a job to reset the configuration for the system copy restore on the specified target database. System copy restore in SAP HANA is done across different databases.

    :param id: ID assigned to target SAP HANA database object.
    :type id: str

    """
    return web.Response(status=200)
