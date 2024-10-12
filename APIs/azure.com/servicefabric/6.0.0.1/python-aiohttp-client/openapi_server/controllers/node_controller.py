from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster_health_policy import ClusterHealthPolicy
from openapi_server.models.deactivation_intent_description import DeactivationIntentDescription
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.node_health import NodeHealth
from openapi_server.models.node_info import NodeInfo
from openapi_server.models.node_load_info import NodeLoadInfo
from openapi_server.models.paged_node_info_list import PagedNodeInfoList
from openapi_server.models.restart_node_description import RestartNodeDescription
from openapi_server import util


async def disable_node(request: web.Request, api_version, node_name, deactivation_intent_description, timeout=None) -> web.Response:
    """Deactivate a Service Fabric cluster node with the specified deactivation intent.

    Deactivate a Service Fabric cluster node with the specified deactivation intent. Once the deactivation is in progress, the deactivation intent can be increased, but not decreased (for example, a node which is was deactivated with the Pause intent can be deactivated further with Restart, but not the other way around. Nodes may be reactivated using the Activate a node operation any time after they are deactivated. If the deactivation is not complete this will cancel the deactivation. A node which goes down and comes back up while deactivated will still need to be reactivated before services will be placed on that node.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param deactivation_intent_description: Describes the intent or reason for deactivating the node.
    :type deactivation_intent_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    deactivation_intent_description = DeactivationIntentDescription.from_dict(deactivation_intent_description)
    return web.Response(status=200)


async def enable_node(request: web.Request, api_version, node_name, timeout=None) -> web.Response:
    """Activate a Service Fabric cluster node which is currently deactivated.

    Activates a Service Fabric cluster node which is currently deactivated. Once activated, the node will again become a viable target for placing new replicas, and any deactivated replicas remaining on the node will be reactivated.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_node_health(request: web.Request, api_version, node_name, events_health_state_filter=None, timeout=None) -> web.Response:
    """Gets the health of a Service Fabric node.

    Gets the health of a Service Fabric node. Use EventsHealthStateFilter to filter the collection of health events reported on the node based on the health state. If the node that you specify by name does not exist in the health store, this returns an error.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param events_health_state_filter: Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type events_health_state_filter: int
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_node_health_using_policy(request: web.Request, api_version, node_name, events_health_state_filter=None, timeout=None, cluster_health_policy=None) -> web.Response:
    """Gets the health of a Service Fabric node, by using the specified health policy.

    Gets the health of a Service Fabric node. Use EventsHealthStateFilter to filter the collection of health events reported on the node based on the health state. Use ClusterHealthPolicy in the POST body to override the health policies used to evaluate the health. If the node that you specify by name does not exist in the health store, this returns an error.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param events_health_state_filter: Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    :type events_health_state_filter: int
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int
    :param cluster_health_policy: Describes the health policies used to evaluate the health of a cluster or node. If not present, the health evaluation uses the health policy from cluster manifest or the default health policy.
    :type cluster_health_policy: dict | bytes

    """
    cluster_health_policy = ClusterHealthPolicy.from_dict(cluster_health_policy)
    return web.Response(status=200)


async def get_node_info(request: web.Request, api_version, node_name, timeout=None) -> web.Response:
    """Gets the list of nodes in the Service Fabric cluster.

    Gets the information about a specific node in the Service Fabric Cluster.The respons include the name, status, id, health, uptime and other details about the node.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_node_info_list(request: web.Request, api_version, continuation_token=None, node_status_filter=None, timeout=None) -> web.Response:
    """Gets the list of nodes in the Service Fabric cluster.

    The Nodes endpoint returns information about the nodes in the Service Fabric Cluster. The respons include the name, status, id, health, uptime and other details about the node.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param node_status_filter: Allows filtering the nodes based on the NodeStatus. Only the nodes that are matching the specified filter value will be returned. The filter value can be one of the following.    - default - This filter value will match all of the nodes excepts the ones with with status as Unknown or Removed.   - all - This filter value will match all of the nodes.   - up - This filter value will match nodes that are Up.   - down - This filter value will match nodes that are Down.   - enabling - This filter value will match nodes that are in the process of being enabled with status as Enabling.   - disabling - This filter value will match nodes that are in the process of being disabled with status as Disabling.   - disabled - This filter value will match nodes that are Disabled.   - unknown - This filter value will match nodes whose status is Unknown. A node would be in Unknown state if Service Fabric does not have authoritative information about that node. This can happen if the system learns about a node at runtime.   - removed - This filter value will match nodes whose status is Removed. These are the nodes that are removed from the cluster using the RemoveNodeState API. 
    :type node_status_filter: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_node_load_info(request: web.Request, api_version, node_name, timeout=None) -> web.Response:
    """Gets the load information of a Service Fabric node.

    Gets the load information of a Service Fabric node.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def remove_node_state(request: web.Request, api_version, node_name, timeout=None) -> web.Response:
    """Notifies Service Fabric that the persisted state on a node has been permanently removed or lost.

    Notifies Service Fabric that the persisted state on a node has been permanently removed or lost.  This implies that it is not possible to recover the persisted state of that node. This generally happens if a hard disk has been wiped clean, or if a hard disk crashes. The node has to be down for this operation to be successful. This operation lets Service Fabric know that the replicas on that node no longer exist, and that Service Fabric should stop waiting for those replicas to come back up. Do not run this cmdlet if the state on the node has not been removed and the node can comes back up with its state intact.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def report_node_health(request: web.Request, api_version, node_name, health_information, immediate=None, timeout=None) -> web.Response:
    """Sends a health report on the Service Fabric node.

    Reports health state of the specified Service Fabric node. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway node, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, run GetNodeHealth and check that the report appears in the HealthEvents section. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param health_information: Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager.
    :type health_information: dict | bytes
    :param immediate: A flag which indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from Http Gateway to the health store, regardless of the fabric client settings that the Http Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the Http Gateway is closed or the message doesn&#39;t reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the Http Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately. 
    :type immediate: bool
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    health_information = HealthInformation.from_dict(health_information)
    return web.Response(status=200)


async def restart_node(request: web.Request, api_version, node_name, restart_node_description, timeout=None) -> web.Response:
    """Restarts a Service Fabric cluster node.

    Restarts a Service Fabric cluster node that is already started.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param restart_node_description: The instance of the node to be restarted and a flag indicating the need to take dump of the fabric process.
    :type restart_node_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    restart_node_description = RestartNodeDescription.from_dict(restart_node_description)
    return web.Response(status=200)
