from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_partition_description import BackupPartitionDescription
from openapi_server.models.backup_policy_description import BackupPolicyDescription
from openapi_server.models.backup_progress_info import BackupProgressInfo
from openapi_server.models.disable_backup_description import DisableBackupDescription
from openapi_server.models.enable_backup_description import EnableBackupDescription
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.get_backup_by_storage_query_description import GetBackupByStorageQueryDescription
from openapi_server.models.paged_backup_configuration_info_list import PagedBackupConfigurationInfoList
from openapi_server.models.paged_backup_entity_list import PagedBackupEntityList
from openapi_server.models.paged_backup_info_list import PagedBackupInfoList
from openapi_server.models.paged_backup_policy_description_list import PagedBackupPolicyDescriptionList
from openapi_server.models.partition_backup_configuration_info import PartitionBackupConfigurationInfo
from openapi_server.models.restore_partition_description import RestorePartitionDescription
from openapi_server.models.restore_progress_info import RestoreProgressInfo
from openapi_server import util


async def backup_partition(request: web.Request, partition_id, api_version, backup_timeout=None, timeout=None, backup_partition_description=None) -> web.Response:
    """Triggers backup of the partition&#39;s state.

    Creates a backup of the stateful persisted partition&#39;s state. In case the partition is already being periodically backed up, then by default the new backup is created at the same backup storage. One can also override the same by specifying the backup storage details as part of the request body. Once the backup is initiated, its progress can be tracked using the GetBackupProgress operation.  In case, the operation times out, specify a greater backup timeout value in the query parameter.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param backup_timeout: Specifies the maximum amount of time, in minutes, to wait for the backup operation to complete. Post that, the operation completes with timeout error. However, in certain corner cases it could be that though the operation returns back timeout, the backup actually goes through. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. The default value for the same is 10 minutes.
    :type backup_timeout: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param backup_partition_description: Describes the parameters to backup the partition now. If not present, backup operation uses default parameters from the backup policy current associated with this partition.
    :type backup_partition_description: dict | bytes

    """
    backup_partition_description = BackupPartitionDescription.from_dict(backup_partition_description)
    return web.Response(status=200)


async def create_backup_policy(request: web.Request, api_version, backup_policy_description, timeout=None) -> web.Response:
    """Creates a backup policy.

    Creates a backup policy which can be associated later with a Service Fabric application, service or a partition for periodic backup.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param backup_policy_description: Describes the backup policy.
    :type backup_policy_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    backup_policy_description = BackupPolicyDescription.from_dict(backup_policy_description)
    return web.Response(status=200)


async def delete_backup_policy(request: web.Request, backup_policy_name, api_version, timeout=None) -> web.Response:
    """Deletes the backup policy.

    Deletes an existing backup policy. A backup policy must be created before it can be deleted. A currently active backup policy, associated with any Service Fabric application, service or partition, cannot be deleted without first deleting the mapping.

    :param backup_policy_name: The name of the backup policy.
    :type backup_policy_name: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def disable_application_backup(request: web.Request, application_id, api_version, timeout=None, disable_backup_description=None) -> web.Response:
    """Disables periodic backup of Service Fabric application.

    Disables periodic backup of Service Fabric application which was previously enabled.

    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param disable_backup_description: Specifies the parameters to disable backup for any backup entity.
    :type disable_backup_description: dict | bytes

    """
    disable_backup_description = DisableBackupDescription.from_dict(disable_backup_description)
    return web.Response(status=200)


async def disable_partition_backup(request: web.Request, partition_id, api_version, timeout=None, disable_backup_description=None) -> web.Response:
    """Disables periodic backup of Service Fabric partition which was previously enabled.

    Disables periodic backup of partition which was previously enabled. Backup must be explicitly enabled before it can be disabled.  In case the backup is enabled for the Service Fabric application or service, which this partition is part of, this partition would continue to be periodically backed up as per the policy mapped at the higher level entity.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param disable_backup_description: Specifies the parameters to disable backup for any backup entity.
    :type disable_backup_description: dict | bytes

    """
    disable_backup_description = DisableBackupDescription.from_dict(disable_backup_description)
    return web.Response(status=200)


async def disable_service_backup(request: web.Request, service_id, api_version, timeout=None, disable_backup_description=None) -> web.Response:
    """Disables periodic backup of Service Fabric service which was previously enabled.

    Disables periodic backup of Service Fabric service which was previously enabled. Backup must be explicitly enabled before it can be disabled. In case the backup is enabled for the Service Fabric application, which this service is part of, this service would continue to be periodically backed up as per the policy mapped at the application level.

    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param disable_backup_description: Specifies the parameters to disable backup for any backup entity.
    :type disable_backup_description: dict | bytes

    """
    disable_backup_description = DisableBackupDescription.from_dict(disable_backup_description)
    return web.Response(status=200)


async def enable_application_backup(request: web.Request, application_id, api_version, enable_backup_description, timeout=None) -> web.Response:
    """Enables periodic backup of stateful partitions under this Service Fabric application.

    Enables periodic backup of stateful partitions which are part of this Service Fabric application. Each partition is backed up individually as per the specified backup policy description.  Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param enable_backup_description: Specifies the parameters for enabling backup.
    :type enable_backup_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    enable_backup_description = EnableBackupDescription.from_dict(enable_backup_description)
    return web.Response(status=200)


async def enable_partition_backup(request: web.Request, partition_id, api_version, enable_backup_description, timeout=None) -> web.Response:
    """Enables periodic backup of the stateful persisted partition.

    Enables periodic backup of stateful persisted partition. Each partition is backed up as per the specified backup policy description. In case the application or service, which is partition is part of, is already enabled for backup then this operation would override the policy being used to take the periodic backup of this partition. Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param enable_backup_description: Specifies the parameters for enabling backup.
    :type enable_backup_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    enable_backup_description = EnableBackupDescription.from_dict(enable_backup_description)
    return web.Response(status=200)


async def enable_service_backup(request: web.Request, service_id, api_version, enable_backup_description, timeout=None) -> web.Response:
    """Enables periodic backup of stateful partitions under this Service Fabric service.

    Enables periodic backup of stateful partitions which are part of this Service Fabric service. Each partition is backed up individually as per the specified backup policy description. In case the application, which the service is part of, is already enabled for backup then this operation would override the policy being used to take the periodic backup for this service and its partitions (unless explicitly overridden at the partition level). Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param enable_backup_description: Specifies the parameters for enabling backup.
    :type enable_backup_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    enable_backup_description = EnableBackupDescription.from_dict(enable_backup_description)
    return web.Response(status=200)


async def get_all_entities_backed_up_by_policy(request: web.Request, backup_policy_name, api_version, continuation_token=None, max_results=None, timeout=None) -> web.Response:
    """Gets the list of backup entities that are associated with this policy.

    Returns a list of Service Fabric application, service or partition which are associated with this backup policy.

    :param backup_policy_name: The name of the backup policy.
    :type backup_policy_name: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    :type max_results: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_application_backup_configuration_info(request: web.Request, application_id, api_version, continuation_token=None, max_results=None, timeout=None) -> web.Response:
    """Gets the Service Fabric application backup configuration information.

    Gets the Service Fabric backup configuration information for the application and the services and partitions under this application.

    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    :type max_results: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_application_backup_list(request: web.Request, application_id, api_version, timeout=None, latest=None, start_date_time_filter=None, end_date_time_filter=None, continuation_token=None, max_results=None) -> web.Response:
    """Gets the list of backups available for every partition in this application.

    Returns a list of backups available for every partition in this Service Fabric application. The server enumerates all the backups available at the backup location configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for every partition.

    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param latest: Specifies whether to get only the most recent backup available for a partition for the specified time range.
    :type latest: bool
    :param start_date_time_filter: Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
    :type start_date_time_filter: str
    :param end_date_time_filter: Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
    :type end_date_time_filter: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    :type max_results: int

    """
    start_date_time_filter = util.deserialize_datetime(start_date_time_filter)
    end_date_time_filter = util.deserialize_datetime(end_date_time_filter)
    return web.Response(status=200)


async def get_backup_policy_by_name(request: web.Request, backup_policy_name, api_version, timeout=None) -> web.Response:
    """Gets a particular backup policy by name.

    Gets a particular backup policy identified by {backupPolicyName}

    :param backup_policy_name: The name of the backup policy.
    :type backup_policy_name: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_backup_policy_list(request: web.Request, api_version, continuation_token=None, max_results=None, timeout=None) -> web.Response:
    """Gets all the backup policies configured.

    Get a list of all the backup policies configured.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    :type max_results: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_backups_from_backup_location(request: web.Request, api_version, get_backup_by_storage_query_description, timeout=None, continuation_token=None, max_results=None) -> web.Response:
    """Gets the list of backups available for the specified backed up entity at the specified backup location.

    Gets the list of backups available for the specified backed up entity (Application, Service or Partition) at the specified backup location (FileShare or Azure Blob Storage).

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param get_backup_by_storage_query_description: Describes the filters and backup storage details to be used for enumerating backups.
    :type get_backup_by_storage_query_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    :type max_results: int

    """
    get_backup_by_storage_query_description = GetBackupByStorageQueryDescription.from_dict(get_backup_by_storage_query_description)
    return web.Response(status=200)


async def get_partition_backup_configuration_info(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """Gets the partition backup configuration information

    Gets the Service Fabric Backup configuration information for the specified partition.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_partition_backup_list(request: web.Request, partition_id, api_version, timeout=None, latest=None, start_date_time_filter=None, end_date_time_filter=None) -> web.Response:
    """Gets the list of backups available for the specified partition.

    Returns a list of backups available for the specified partition. The server enumerates all the backups available in the backup store configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for the partition.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param latest: Specifies whether to get only the most recent backup available for a partition for the specified time range.
    :type latest: bool
    :param start_date_time_filter: Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
    :type start_date_time_filter: str
    :param end_date_time_filter: Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
    :type end_date_time_filter: str

    """
    start_date_time_filter = util.deserialize_datetime(start_date_time_filter)
    end_date_time_filter = util.deserialize_datetime(end_date_time_filter)
    return web.Response(status=200)


async def get_partition_backup_progress(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """Gets details for the latest backup triggered for this partition.

    Returns information about the state of the latest backup along with details or failure reason in case of completion.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_partition_restore_progress(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """Gets details for the latest restore operation triggered for this partition.

    Returns information about the state of the latest restore operation along with details or failure reason in case of completion.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_service_backup_configuration_info(request: web.Request, service_id, api_version, continuation_token=None, max_results=None, timeout=None) -> web.Response:
    """Gets the Service Fabric service backup configuration information.

    Gets the Service Fabric backup configuration information for the service and the partitions under this service.

    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    :type max_results: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_service_backup_list(request: web.Request, service_id, api_version, timeout=None, latest=None, start_date_time_filter=None, end_date_time_filter=None, continuation_token=None, max_results=None) -> web.Response:
    """Gets the list of backups available for every partition in this service.

    Returns a list of backups available for every partition in this Service Fabric service. The server enumerates all the backups available in the backup store configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for every partition.

    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param latest: Specifies whether to get only the most recent backup available for a partition for the specified time range.
    :type latest: bool
    :param start_date_time_filter: Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
    :type start_date_time_filter: str
    :param end_date_time_filter: Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
    :type end_date_time_filter: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    :type max_results: int

    """
    start_date_time_filter = util.deserialize_datetime(start_date_time_filter)
    end_date_time_filter = util.deserialize_datetime(end_date_time_filter)
    return web.Response(status=200)


async def restore_partition(request: web.Request, partition_id, api_version, restore_partition_description, restore_timeout=None, timeout=None) -> web.Response:
    """Triggers restore of the state of the partition using the specified restore partition description.

    Restores the state of a of the stateful persisted partition using the specified backup point. In case the partition is already being periodically backed up, then by default the backup point is looked for in the storage specified in backup policy. One can also override the same by specifying the backup storage details as part of the restore partition description in body. Once the restore is initiated, its progress can be tracked using the GetRestoreProgress operation.  In case, the operation times out, specify a greater restore timeout value in the query parameter.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param restore_partition_description: Describes the parameters to restore the partition.
    :type restore_partition_description: dict | bytes
    :param restore_timeout: Specifies the maximum amount of time to wait, in minutes, for the restore operation to complete. Post that, the operation returns back with timeout error. However, in certain corner cases it could be that the restore operation goes through even though it completes with timeout. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. the default value for the same is 10 minutes.
    :type restore_timeout: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    restore_partition_description = RestorePartitionDescription.from_dict(restore_partition_description)
    return web.Response(status=200)


async def resume_application_backup(request: web.Request, application_id, api_version, timeout=None) -> web.Response:
    """Resumes periodic backup of a Service Fabric application which was previously suspended.

    The previously suspended Service Fabric application resumes taking periodic backup as per the backup policy currently configured for the same.

    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def resume_partition_backup(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """Resumes periodic backup of partition which was previously suspended.

    The previously suspended partition resumes taking periodic backup as per the backup policy currently configured for the same.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def resume_service_backup(request: web.Request, service_id, api_version, timeout=None) -> web.Response:
    """Resumes periodic backup of a Service Fabric service which was previously suspended.

    The previously suspended Service Fabric service resumes taking periodic backup as per the backup policy currently configured for the same.

    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def suspend_application_backup(request: web.Request, application_id, api_version, timeout=None) -> web.Response:
    """Suspends periodic backup for the specified Service Fabric application.

    The application which is configured to take periodic backups, is suspended for taking further backups till it is resumed again. This operation applies to the entire application&#39;s hierarchy. It means all the services and partitions under this application are now suspended for backup.

    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def suspend_partition_backup(request: web.Request, partition_id, api_version, timeout=None) -> web.Response:
    """Suspends periodic backup for the specified partition.

    The partition which is configured to take periodic backups, is suspended for taking further backups till it is resumed again.

    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def suspend_service_backup(request: web.Request, service_id, api_version, timeout=None) -> web.Response:
    """Suspends periodic backup for the specified Service Fabric service.

    The service which is configured to take periodic backups, is suspended for taking further backups till it is resumed again. This operation applies to the entire service&#39;s hierarchy. It means all the partitions under this service are now suspended for backup.

    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def update_backup_policy(request: web.Request, backup_policy_name, api_version, backup_policy_description, timeout=None) -> web.Response:
    """Updates the backup policy.

    Updates the backup policy identified by {backupPolicyName}

    :param backup_policy_name: The name of the backup policy.
    :type backup_policy_name: str
    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param backup_policy_description: Describes the backup policy.
    :type backup_policy_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    backup_policy_description = BackupPolicyDescription.from_dict(backup_policy_description)
    return web.Response(status=200)
