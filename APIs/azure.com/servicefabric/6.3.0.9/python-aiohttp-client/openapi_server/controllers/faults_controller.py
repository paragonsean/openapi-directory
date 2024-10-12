from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.node_transition_progress import NodeTransitionProgress
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.partition_data_loss_progress import PartitionDataLossProgress
from openapi_server.models.partition_quorum_loss_progress import PartitionQuorumLossProgress
from openapi_server.models.partition_restart_progress import PartitionRestartProgress
from openapi_server import util


async def cancel_operation(request: web.Request, api_version, operation_id, force, timeout=None) -> web.Response:
    """Cancels a user-induced fault operation.

    The following APIs start fault operations that may be cancelled by using CancelOperation: StartDataLoss, StartQuorumLoss, StartPartitionRestart, StartNodeTransition.  If force is false, then the specified user-induced operation will be gracefully stopped and cleaned up.  If force is true, the command will be aborted, and some internal state may be left behind.  Specifying force as true should be used with care.  Calling this API with force set to true is not allowed until this API has already been called on the same test command with force set to false first, or unless the test command already has an OperationState of OperationState.RollingBack. Clarification: OperationState.RollingBack means that the system will be/is cleaning up internal system state caused by executing the command.  It will not restore data if the test command was to cause data loss.  For example, if you call StartDataLoss then call this API, the system will only clean up internal state from running the command. It will not restore the target partition&#39;s data, if the command progressed far enough to cause data loss.  Important note:  if this API is invoked with force&#x3D;&#x3D;true, internal state may be left behind.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param force: Indicates whether to gracefully rollback and clean up internal system state modified by executing the user-induced operation.
    :type force: bool
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_data_loss_progress(request: web.Request, api_version, service_id, partition_id, operation_id, timeout=None) -> web.Response:
    """Gets the progress of a partition data loss operation started using the StartDataLoss API.

    Gets the progress of a data loss operation started with StartDataLoss, using the OperationId.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_fault_operation_list(request: web.Request, api_version, type_filter, state_filter, timeout=None) -> web.Response:
    """Gets a list of user-induced fault operations filtered by provided input.

    Gets the a list of user-induced fault operations filtered by provided input.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param type_filter: Used to filter on OperationType for user-induced operations.  - 65535 - select all - 1 - select PartitionDataLoss. - 2 - select PartitionQuorumLoss. - 4 - select PartitionRestart. - 8 - select NodeTransition.
    :type type_filter: int
    :param state_filter: Used to filter on OperationState&#39;s for user-induced operations.  - 65535 - select All - 1 - select Running - 2 - select RollingBack - 8 - select Completed - 16 - select Faulted - 32 - select Cancelled - 64 - select ForceCancelled
    :type state_filter: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_node_transition_progress(request: web.Request, api_version, node_name, operation_id, timeout=None) -> web.Response:
    """Gets the progress of an operation started using StartNodeTransition.

    Gets the progress of an operation started with StartNodeTransition using the provided OperationId.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_partition_restart_progress(request: web.Request, api_version, service_id, partition_id, operation_id, timeout=None) -> web.Response:
    """Gets the progress of a PartitionRestart operation started using StartPartitionRestart.

    Gets the progress of a PartitionRestart started with StartPartitionRestart using the provided OperationId.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_quorum_loss_progress(request: web.Request, api_version, service_id, partition_id, operation_id, timeout=None) -> web.Response:
    """Gets the progress of a quorum loss operation on a partition started using the StartQuorumLoss API.

    Gets the progress of a quorum loss operation started with StartQuorumLoss, using the provided OperationId.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def start_data_loss(request: web.Request, api_version, service_id, partition_id, operation_id, data_loss_mode, timeout=None) -> web.Response:
    """This API will induce data loss for the specified partition. It will trigger a call to the OnDataLossAsync API of the partition.

    This API will induce data loss for the specified partition. It will trigger a call to the OnDataLoss API of the partition. Actual data loss will depend on the specified DataLossMode.  - PartialDataLoss - Only a quorum of replicas are removed and OnDataLoss is triggered for the partition but actual data loss depends on the presence of in-flight replication. - FullDataLoss - All replicas are removed hence all data is lost and OnDataLoss is triggered.  This API should only be called with a stateful service as the target.  Calling this API with a system service as the target is not advised.  Note:  Once this API has been called, it cannot be reversed. Calling CancelOperation will only stop execution and clean up internal system state. It will not restore data if the command has progressed far enough to cause data loss.  Call the GetDataLossProgress API with the same OperationId to return information on the operation started with this API.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param data_loss_mode: This enum is passed to the StartDataLoss API to indicate what type of data loss to induce.
    :type data_loss_mode: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def start_node_transition(request: web.Request, api_version, node_name, operation_id, node_transition_type, node_instance_id, stop_duration_in_seconds, timeout=None) -> web.Response:
    """Starts or stops a cluster node.

    Starts or stops a cluster node.  A cluster node is a process, not the OS instance itself.  To start a node, pass in \&quot;Start\&quot; for the NodeTransitionType parameter. To stop a node, pass in \&quot;Stop\&quot; for the NodeTransitionType parameter.  This API starts the operation - when the API returns the node may not have finished transitioning yet. Call GetNodeTransitionProgress with the same OperationId to get the progress of the operation.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param node_transition_type: Indicates the type of transition to perform.  NodeTransitionType.Start will start a stopped node.  NodeTransitionType.Stop will stop a node that is up.
    :type node_transition_type: str
    :param node_instance_id: The node instance ID of the target node.  This can be determined through GetNodeInfo API.
    :type node_instance_id: str
    :param stop_duration_in_seconds: The duration, in seconds, to keep the node stopped.  The minimum value is 600, the maximum is 14400.  After this time expires, the node will automatically come back up.
    :type stop_duration_in_seconds: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def start_partition_restart(request: web.Request, api_version, service_id, partition_id, operation_id, restart_partition_mode, timeout=None) -> web.Response:
    """This API will restart some or all replicas or instances of the specified partition.

    This API is useful for testing failover.  If used to target a stateless service partition, RestartPartitionMode must be AllReplicasOrInstances.  Call the GetPartitionRestartProgress API using the same OperationId to get the progress.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param restart_partition_mode: Describe which partitions to restart.
    :type restart_partition_mode: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def start_quorum_loss(request: web.Request, api_version, service_id, partition_id, operation_id, quorum_loss_mode, quorum_loss_duration, timeout=None) -> web.Response:
    """Induces quorum loss for a given stateful service partition.

    This API is useful for a temporary quorum loss situation on your service.  Call the GetQuorumLossProgress API with the same OperationId to return information on the operation started with this API.  This can only be called on stateful persisted (HasPersistedState&#x3D;&#x3D;true) services.  Do not use this API on stateless services or stateful in-memory only services.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param operation_id: A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    :type operation_id: str
    :type operation_id: str
    :param quorum_loss_mode: This enum is passed to the StartQuorumLoss API to indicate what type of quorum loss to induce.
    :type quorum_loss_mode: str
    :param quorum_loss_duration: The amount of time for which the partition will be kept in quorum loss.  This must be specified in seconds.
    :type quorum_loss_duration: int
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)
