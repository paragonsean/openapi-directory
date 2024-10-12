from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.bulk_oracle_db_details import BulkOracleDbDetails
from openapi_server.models.bulk_oracle_host_details import BulkOracleHostDetails
from openapi_server.models.bulk_oracle_rac_details import BulkOracleRacDetails
from openapi_server.models.oracle_aco_parameter_list import OracleAcoParameterList
from openapi_server.models.oracle_aco_validation_result import OracleAcoValidationResult
from openapi_server.models.oracle_bulk_update import OracleBulkUpdate
from openapi_server.models.oracle_data_guard_group_update import OracleDataGuardGroupUpdate
from openapi_server.models.oracle_db_detail import OracleDbDetail
from openapi_server.models.oracle_db_summary_list_response import OracleDbSummaryListResponse
from openapi_server.models.oracle_file_download_link import OracleFileDownloadLink
from openapi_server.models.oracle_restore_estimate_result import OracleRestoreEstimateResult
from openapi_server.models.oracle_update import OracleUpdate
from openapi_server.models.oracle_validate_config import OracleValidateConfig
from openapi_server import util


async def bulk_update_oracle_db(request: web.Request, body) -> web.Response:
    """Update Oracle Databases

    Update the properties of the objects that represent the specified Oracle Databases.

    :param body: Properties to use for the update of Oracle Database objects.
    :type body: dict | bytes

    """
    body = OracleBulkUpdate.from_dict(body)
    return web.Response(status=200)


async def bulk_update_oracle_host(request: web.Request, body) -> web.Response:
    """Update Oracle Hosts

    Update properties to Oracle Host objects.

    :param body: Properties to use for the update of Oracle Host objects.
    :type body: dict | bytes

    """
    body = OracleBulkUpdate.from_dict(body)
    return web.Response(status=200)


async def bulk_update_oracle_rac(request: web.Request, body) -> web.Response:
    """Update Oracle RACs

    Update the properties of the objects that represent the specified Oracle RAC.

    :param body: Properties to use for the update of Oracle RAC objects.
    :type body: dict | bytes

    """
    body = OracleBulkUpdate.from_dict(body)
    return web.Response(status=200)


async def create_oracle_validate_backup_job(request: web.Request, id, body) -> web.Response:
    """Validate Oracle database backups

    Queue a job to validate Oracle backups for a database snapshot or a specified timestamp.

    :param id: ID of the database to be validated.
    :type id: str
    :param body: Configuration parameters for a job to validate an Oracle backups.
    :type body: dict | bytes

    """
    body = OracleValidateConfig.from_dict(body)
    return web.Response(status=200)


async def delete_downloaded_snapshots(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Delete downloaded Oracle database snapshots and log snapshots

    Requests an asynchronous job to expire downloaded database snapshots taken during a specified time period as well as log snapshots that contain any logs with timestamps within that time period.

    :param id: ID of the Oracle database.
    :type id: str
    :param after_time: Uses the ISO 8601 format to specify the start of the time period used by the asynchronous snapshot expiration job, as in the example \&quot;2016-01-01T01:23:45.678\&quot;.
    :type after_time: str
    :param before_time: Uses the ISO 8601 format to specify the end of the time period used by the asynchronous snapshot expiration job, as in the example \&quot;2016-01-01T01:23:45.678\&quot;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_aco_parameter_list(request: web.Request, ) -> web.Response:
    """List of supported Advanced Cloning Options

    Get the list of supported Advanced Cloning Options (ACO) parameters.


    """
    return web.Response(status=200)


async def get_example_aco_download_link(request: web.Request, ) -> web.Response:
    """Link to download the Advanced Recovery Options example file

    Link to download the Advanced Recovery Options example file which can be used to customize Oracle recoveries.


    """
    return web.Response(status=200)


async def get_oracle_db_v1(request: web.Request, id) -> web.Response:
    """Get Oracle database information

    Retrieves detailed information for a specified Oracle database object.

    :param id: ID of an Oracle database object.
    :type id: str

    """
    return web.Response(status=200)


async def oracle_restore_estimate(request: web.Request, id, snapshot_id=None, recovery_time=None) -> web.Response:
    """Get a size estimate for a restore or export

    The estimated size of the data to download from an archival location in order to perform a specified restore or export operation.

    :param id: ID of the Oracle database.
    :type id: str
    :param snapshot_id: ID of the snapshot to recover to.
    :type snapshot_id: str
    :param recovery_time: The date and time for the recovery restore point, specified in the ISO 8601 format, as in the example \&quot;2016-01-01T01:23:45.678\&quot;.
    :type recovery_time: str

    """
    recovery_time = util.deserialize_datetime(recovery_time)
    return web.Response(status=200)


async def query_oracle_db_v1(request: web.Request, name=None, sla_assignment=None, effective_sla_domain_id=None, primary_cluster_id=None, is_relic=None, is_live_mount=None, limit=None, offset=None, sort_by=None, sort_order=None, include_backup_task_info=None, is_data_guard_group=None) -> web.Response:
    """Get summary information for Oracle databases

    Retrieves an array containing summary information about the Oracle database objects in the Rubrik cluster.

    :param name: Filters a response by making an infix comparison of the database name, SID, and tablespaces in the response with the specified value.
    :type name: str
    :param sla_assignment: Limits the response to Oracle databases that are protected by the specified type of SLA Domain assignment.
    :type sla_assignment: str
    :param effective_sla_domain_id: Filters by effective SLA Domain ID.
    :type effective_sla_domain_id: str
    :param primary_cluster_id: Limits the response to Oracle databases that have the specified primary cluster value.
    :type primary_cluster_id: str
    :param is_relic: Limits the response to Oracle databases that have the specified isRelic value.
    :type is_relic: bool
    :param is_live_mount: Limits the response to Oracle databases that have the specified isLiveMount value.
    :type is_live_mount: bool
    :param limit: Limits the summary information to the specified number of matches. Optionally, it can be used with offset to begin the count of matches at the number specified in the offset parameter, and with sort_by to sort the results by the specified attribute.
    :type limit: int
    :param offset: Determines the elements to include in the response starting with the element at the index number specified here. Optionally used with limit to enable paging of the results by retrieving a smaller number of elements in the response.
    :type offset: int
    :param sort_by: Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
    :type sort_by: str
    :param sort_order: Specifies the ascending or descending order to sort the elements in the response by the attributes specified in the sort_by parameter.
    :type sort_order: str
    :param include_backup_task_info: Specifies whether to include the backup task information in the response.
    :type include_backup_task_info: bool
    :param is_data_guard_group: Limits the response to Oracle databases that have the specified value for the isDataGuardGroup flag.
    :type is_data_guard_group: bool

    """
    return web.Response(status=200)


async def update_oracle_data_guard_group(request: web.Request, id, body) -> web.Response:
    """Update an Oracle Data Guard group

    Update properties of an Oracle Data Guard group object.

    :param id: ID assigned to an Oracle Data Guard group object.
    :type id: str
    :param body: Properties to use for the update of an Oracle Data Guard group object.
    :type body: dict | bytes

    """
    body = OracleDataGuardGroupUpdate.from_dict(body)
    return web.Response(status=200)


async def update_oracle_db_v1(request: web.Request, id, body) -> web.Response:
    """Update an Oracle database

    Updates the properties of a specified Oracle database object.

    :param id: ID of an Oracle database object.
    :type id: str
    :param body: Properties of the Oracle database object to be updated. object.
    :type body: dict | bytes

    """
    body = OracleUpdate.from_dict(body)
    return web.Response(status=200)


async def validate_oracle_aco_file(request: web.Request, is_live_mount, body) -> web.Response:
    """Validate Oracle ACO file

    Validate the provided Oracle ACO (Advanced Cloning Options) file.

    :param is_live_mount: Boolean that determines whether the ACO file is being used for a Live Mount.
    :type is_live_mount: bool
    :param body: Contents of the Advanced Cloning Options file in base64 encoded format.
    :type body: str

    """
    return web.Response(status=200)
