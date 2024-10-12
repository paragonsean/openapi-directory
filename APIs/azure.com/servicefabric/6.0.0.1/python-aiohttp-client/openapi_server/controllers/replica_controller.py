from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_health_policy import ApplicationHealthPolicy
from openapi_server.models.deployed_service_replica_detail_info import DeployedServiceReplicaDetailInfo
from openapi_server.models.deployed_service_replica_info import DeployedServiceReplicaInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.paged_replica_info_list import PagedReplicaInfoList
from openapi_server.models.replica_health import ReplicaHealth
from openapi_server.models.replica_info import ReplicaInfo
from openapi_server import util


async def get_deployed_service_replica_detail_info(request: web.Request, api_version, node_name, partition_id, replica_id, timeout=None) -> web.Response:
    """Gets the details of replica deployed on a Service Fabric node.

    Gets the details of the replica deployed on a Service Fabric node. The information include service kind, service name, current service operation, current service operation start date time, partition id, replica/instance id, reported load and other information.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param replica_id: The identifier of the replica.
    :type replica_id: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_deployed_service_replica_detail_info_by_partition_id(request: web.Request, api_version, node_name, partition_id, timeout=None) -> web.Response:
    """Gets the details of replica deployed on a Service Fabric node.

    Gets the details of the replica deployed on a Service Fabric node. The information include service kind, service name, current service operation, current service operation start date time, partition id, replica/instance id, reported load and other information.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_deployed_service_replica_info_list(request: web.Request, api_version, node_name, application_id, partition_id=None, service_manifest_name=None, timeout=None) -> web.Response:
    """Gets the list of replicas deployed on a Service Fabric node.

    Gets the list containing the information about replicas deployed on a Service Fabric node. The information include partition id, replica id, status of the replica, name of the service, name of the service type and other information. Use PartitionId or ServiceManifestName query parameters to return information about the deployed replicas matching the specified values for those parameters.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param service_manifest_name: The name of a service manifest registered as part of an application type in a Service Fabric cluster.
    :type service_manifest_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_replica_health(request: web.Request, api_version, partition_id, replica_id, events_health_state_filter=None, timeout=None) -> web.Response:
    """Gets the health of a Service Fabric stateful service replica or stateless service instance.

    Gets the health of a Service Fabric replica. Use EventsHealthStateFilter to filter the collection of health events reported on the replica based on the health state. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param replica_id: The identifier of the replica.
    :type replica_id: str
    :param events_health_state_filter: Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type events_health_state_filter: int
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_replica_health_using_policy(request: web.Request, api_version, partition_id, replica_id, events_health_state_filter=None, timeout=None, application_health_policy=None) -> web.Response:
    """Gets the health of a Service Fabric stateful service replica or stateless service instance using the specified policy.

    Gets the health of a Service Fabric stateful service replica or stateless service instance. Use EventsHealthStateFilter to filter the collection of health events reported on the cluster based on the health state. Use ApplicationHealthPolicy to optionally override the health policies used to evaluate the health. This API only uses &#39;ConsiderWarningAsError&#39; field of the ApplicationHealthPolicy. The rest of the fields are ignored while evaluating the health of the replica. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param replica_id: The identifier of the replica.
    :type replica_id: str
    :param events_health_state_filter: Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type events_health_state_filter: int
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param application_health_policy: Describes the health policies used to evaluate the health of an application or one of its children. If not present, the health evaluation uses the health policy from application manifest or the default health policy. 
    :type application_health_policy: dict | bytes

    """
    application_health_policy = ApplicationHealthPolicy.from_dict(application_health_policy)
    return web.Response(status=200)


async def get_replica_info(request: web.Request, api_version, partition_id, replica_id, continuation_token=None, timeout=None) -> web.Response:
    """Gets the information about a replica of a Service Fabric partition.

    The respons include the id, role, status, health, node name, uptime, and other details about the replica.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param replica_id: The identifier of the replica.
    :type replica_id: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_replica_info_list(request: web.Request, api_version, partition_id, continuation_token=None, timeout=None) -> web.Response:
    """Gets the information about replicas of a Service Fabric service partition.

    The GetReplicas endpoint returns information about the replicas of the specified partition. The respons include the id, role, status, health, node name, uptime, and other details about the replica.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def remove_replica(request: web.Request, api_version, node_name, partition_id, replica_id, force_remove=None, timeout=None) -> web.Response:
    """Removes a service replica running on a node.

    This API simulates a Service Fabric replica failure by removing a replica from a Service Fabric cluster. The removal closes the replica, transitions the replica to the role None, and then removes all of the state information of the replica from the cluster. This API tests the replica state removal path, and simulates the report fault permanent path through client APIs. Warning - There are no safety checks performed when this API is used. Incorrect use of this API can lead to data loss for stateful services.In addition, the forceRemove flag impacts all other replicas hosted in the same process.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param replica_id: The identifier of the replica.
    :type replica_id: str
    :param force_remove: Remove a Service Fabric application or service forcefully without going through the graceful shutdown sequence. This parameter can be used to forcefully delete an application or service for which delete is timing out due to issues in the service code that prevents graceful close of replicas.
    :type force_remove: bool
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def report_replica_health(request: web.Request, api_version, partition_id, replica_id, service_kind, health_information, immediate=None, timeout=None) -> web.Response:
    """Sends a health report on the Service Fabric replica.

    Reports health state of the specified Service Fabric replica. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway Replica, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, run GetReplicaHealth and check that the report appears in the HealthEvents section. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param replica_id: The identifier of the replica.
    :type replica_id: str
    :param service_kind: The kind of service replica (Stateless or Stateful) for which the health is being reported. Following are the possible values. - Stateless - Does not use Service Fabric to make its state highly available or reliable. The value is 1 - Stateful - Uses Service Fabric to make its state or part of its state highly available and reliable. The value is 2. 
    :type service_kind: str
    :param health_information: Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager.
    :type health_information: dict | bytes
    :param immediate: A flag which indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from Http Gateway to the health store, regardless of the fabric client settings that the Http Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the Http Gateway is closed or the message doesn&#39;t reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the Http Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately. 
    :type immediate: bool
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    health_information = HealthInformation.from_dict(health_information)
    return web.Response(status=200)


async def restart_replica(request: web.Request, api_version, node_name, partition_id, replica_id, timeout=None) -> web.Response:
    """Restarts a service replica of a persisted service running on a node.

    Restarts a service replica of a persisted service running on a node. Warning - There are no safety checks performed when this API is used. Incorrect use of this API can lead to availability loss for stateful services.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param replica_id: The identifier of the replica.
    :type replica_id: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)
