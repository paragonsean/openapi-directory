from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_event import ApplicationEvent
from openapi_server.models.cluster_event import ClusterEvent
from openapi_server.models.container_instance_event import ContainerInstanceEvent
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.fabric_event import FabricEvent
from openapi_server.models.node_event import NodeEvent
from openapi_server.models.partition_event import PartitionEvent
from openapi_server.models.replica_event import ReplicaEvent
from openapi_server.models.service_event import ServiceEvent
from openapi_server import util


async def get_application_event_list(request: web.Request, api_version, application_id, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets an Application-related events.

    The response is list of ApplicationEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_applications_event_list(request: web.Request, api_version, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets all Applications-related events.

    The response is list of ApplicationEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_cluster_event_list(request: web.Request, api_version, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets all Cluster-related events.

    The response is list of ClusterEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_containers_event_list(request: web.Request, api_version, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets all Containers-related events.

    The response is list of ContainerInstanceEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_correlated_event_list(request: web.Request, api_version, event_instance_id, timeout=None) -> web.Response:
    """Gets all correlated events for a given event.

    The response is list of FabricEvents.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param event_instance_id: The EventInstanceId.
    :type event_instance_id: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_node_event_list(request: web.Request, api_version, node_name, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets a Node-related events.

    The response is list of NodeEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_nodes_event_list(request: web.Request, api_version, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets all Nodes-related Events.

    The response is list of NodeEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_partition_event_list(request: web.Request, api_version, partition_id, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets a Partition-related events.

    The response is list of PartitionEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_partition_replica_event_list(request: web.Request, api_version, partition_id, replica_id, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets a Partition Replica-related events.

    The response is list of ReplicaEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param replica_id: The identifier of the replica.
    :type replica_id: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_partition_replicas_event_list(request: web.Request, api_version, partition_id, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets all Replicas-related events for a Partition.

    The response is list of ReplicaEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param partition_id: The identity of the partition.
    :type partition_id: str
    :type partition_id: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_partitions_event_list(request: web.Request, api_version, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets all Partitions-related events.

    The response is list of PartitionEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_service_event_list(request: web.Request, api_version, service_id, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets a Service-related events.

    The response is list of ServiceEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param service_id: The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.
    :type service_id: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)


async def get_services_event_list(request: web.Request, api_version, start_time_utc, end_time_utc, timeout=None, events_types_filter=None, exclude_analysis_events=None, skip_correlation_lookup=None) -> web.Response:
    """Gets all Services-related events.

    The response is list of ServiceEvent objects.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;.
    :type api_version: str
    :param start_time_utc: The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type start_time_utc: str
    :param end_time_utc: The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    :type end_time_utc: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param events_types_filter: This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    :type events_types_filter: str
    :param exclude_analysis_events: This param disables the retrieval of AnalysisEvents if true is passed.
    :type exclude_analysis_events: bool
    :param skip_correlation_lookup: This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    :type skip_correlation_lookup: bool

    """
    return web.Response(status=200)
