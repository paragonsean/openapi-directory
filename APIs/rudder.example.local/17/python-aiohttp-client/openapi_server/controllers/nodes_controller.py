from typing import List, Dict
from aiohttp import web

from openapi_server.models.apply_policy_all_nodes200_response import ApplyPolicyAllNodes200Response
from openapi_server.models.change_pending_node_status200_response import ChangePendingNodeStatus200Response
from openapi_server.models.change_pending_node_status_request import ChangePendingNodeStatusRequest
from openapi_server.models.create_nodes200_response import CreateNodes200Response
from openapi_server.models.delete_node200_response import DeleteNode200Response
from openapi_server.models.get_nodes_status200_response import GetNodesStatus200Response
from openapi_server.models.list_accepted_nodes200_response import ListAcceptedNodes200Response
from openapi_server.models.list_pending_nodes200_response import ListPendingNodes200Response
from openapi_server.models.node_add_inner import NodeAddInner
from openapi_server.models.node_details200_response import NodeDetails200Response
from openapi_server.models.node_inherited_properties200_response import NodeInheritedProperties200Response
from openapi_server.models.node_settings import NodeSettings
from openapi_server.models.update_node200_response import UpdateNode200Response
from openapi_server import util


async def apply_policy(request: web.Request, node_id) -> web.Response:
    """Trigger an agent run

    This API allows to trigger an agent run on the target node. Response is a stream of the actual agent run on the node.

    :param node_id: Id of the target node
    :type node_id: str

    """
    return web.Response(status=200)


async def apply_policy_all_nodes(request: web.Request, ) -> web.Response:
    """Trigger an agent run on all nodes

    This API allows to trigger an agent run on all nodes. Response contains a json stating if agent could be started on each node, but not if the run went fine and do not display any output from it. You can see the result of the run in Rudder web interface or in the each agent logs.


    """
    return web.Response(status=200)


async def change_pending_node_status(request: web.Request, node_id, body=None) -> web.Response:
    """Update pending Node status

    Accept or refuse a pending node

    :param node_id: Id of the target node
    :type node_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangePendingNodeStatusRequest.from_dict(body)
    return web.Response(status=200)


async def create_nodes(request: web.Request, body) -> web.Response:
    """Create one or several new nodes

    Use the provided array of node information to create new nodes

    :param body: 
    :type body: list | bytes

    """
    body = [NodeAddInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_node(request: web.Request, node_id, mode=None) -> web.Response:
    """Delete a node

    Remove a node from the Rudder server. It won&#39;t be managed anymore.

    :param node_id: Id of the target node
    :type node_id: str
    :param mode: Deletion mode to use, either move to trash (&#39;move&#39;, default) or erase (&#39;erase&#39;)
    :type mode: str

    """
    return web.Response(status=200)


async def get_nodes_status(request: web.Request, ids) -> web.Response:
    """Get nodes acceptation status

    Get acceptation status (pending, accepted, deleted, unknown) of a list of nodes

    :param ids: Comma separated list of node Ids
    :type ids: str

    """
    return web.Response(status=200)


async def list_accepted_nodes(request: web.Request, include=None, query=None, where=None, composition=None, select=None) -> web.Response:
    """List managed nodes

    Get information about the nodes managed by the target server

    :param include: Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60;
    :type include: str
    :param query: The criterion you want to find for your nodes. Replaces the &#x60;where&#x60;, &#x60;composition&#x60; and &#x60;select&#x60; parameters in a single parameter.
    :type query: dict | bytes
    :param where: The criterion you want to find for your nodes
    :type where: List[]
    :param composition: Boolean operator to use between each  &#x60;where&#x60; criteria.
    :type composition: str
    :param select: What kind of data we want to include. Here we can get policy servers/relay by setting &#x60;nodeAndPolicyServer&#x60;. Only used if &#x60;where&#x60; is defined.
    :type select: str

    """
    query = .from_dict(query)
    return web.Response(status=200)


async def list_pending_nodes(request: web.Request, include=None, query=None, where=None, composition=None, select=None) -> web.Response:
    """List pending nodes

    Get information about the nodes pending acceptation

    :param include: Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60;
    :type include: str
    :param query: The criterion you want to find for your nodes. Replaces the &#x60;where&#x60;, &#x60;composition&#x60; and &#x60;select&#x60; parameters in a single parameter.
    :type query: dict | bytes
    :param where: The criterion you want to find for your nodes
    :type where: List[]
    :param composition: Boolean operator to use between each  &#x60;where&#x60; criteria.
    :type composition: str
    :param select: What kind of data we want to include. Here we can get policy servers/relay by setting &#x60;nodeAndPolicyServer&#x60;. Only used if &#x60;where&#x60; is defined.
    :type select: str

    """
    query = .from_dict(query)
    return web.Response(status=200)


async def node_details(request: web.Request, node_id, include=None) -> web.Response:
    """Get information about a node

    Get details about a given node

    :param node_id: Id of the target node
    :type node_id: str
    :param include: Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60;
    :type include: str

    """
    return web.Response(status=200)


async def node_inherited_properties(request: web.Request, node_id) -> web.Response:
    """Get inherited node properties for a node

    This API returns all node properties for a node, including group inherited ones.

    :param node_id: Id of the target node
    :type node_id: str

    """
    return web.Response(status=200)


async def update_node(request: web.Request, node_id, body=None) -> web.Response:
    """Update node settings and properties

    Update node settings and properties

    :param node_id: Id of the target node
    :type node_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NodeSettings.from_dict(body)
    return web.Response(status=200)
