from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.add_target_request import AddTargetRequest
from openapi_server.models.change_loadbalancer_dns_ptr_request import ChangeLoadbalancerDnsPtrRequest
from openapi_server.models.change_type_request import ChangeTypeRequest
from openapi_server.models.load_balancer_service import LoadBalancerService
from openapi_server.models.load_balancers_id_actions_attach_to_network_post_request import LoadBalancersIdActionsAttachToNetworkPostRequest
from openapi_server.models.load_balancers_id_actions_change_algorithm_post_request import LoadBalancersIdActionsChangeAlgorithmPostRequest
from openapi_server.models.load_balancers_id_actions_change_protection_post_request import LoadBalancersIdActionsChangeProtectionPostRequest
from openapi_server.models.load_balancers_id_actions_delete_service_post_request import LoadBalancersIdActionsDeleteServicePostRequest
from openapi_server.models.load_balancers_id_actions_detach_from_network_post_request import LoadBalancersIdActionsDetachFromNetworkPostRequest
from openapi_server.models.remove_target_request import RemoveTargetRequest
from openapi_server import util


async def load_balancers_id_actions_action_id_get(request: web.Request, id, action_id) -> web.Response:
    """Get an Action for a Load Balancer

    Returns a specific Action for a Load Balancer.

    :param id: ID of the Load Balancer
    :type id: int
    :param action_id: ID of the Action
    :type action_id: int

    """
    return web.Response(status=200)


async def load_balancers_id_actions_add_service_post(request: web.Request, id, body=None) -> web.Response:
    """Add Service

    Adds a service to a Load Balancer.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LoadBalancerService.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_add_target_post(request: web.Request, id, body=None) -> web.Response:
    """Add Target

    Adds a target to a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP you are trying to add as a target is not owned by the Project owner                            | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddTargetRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_attach_to_network_post(request: web.Request, id, body=None) -> web.Response:
    """Attach a Load Balancer to a Network

    Attach a Load Balancer to a Network.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;load_balancer_already_attached&#x60; | The Load Balancer is already attached to a network                    | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Load Balancer within the network | 

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LoadBalancersIdActionsAttachToNetworkPostRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_change_algorithm_post(request: web.Request, id, body=None) -> web.Response:
    """Change Algorithm

    Change the algorithm that determines to which target new requests are sent.

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LoadBalancersIdActionsChangeAlgorithmPostRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_change_dns_ptr_post(request: web.Request, id, body=None) -> web.Response:
    """Change reverse DNS entry for this Load Balancer

    Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.  Floating IPs assigned to the Server are not affected by this. 

    :param id: ID of the Load Balancer
    :type id: int
    :param body: Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;.
    :type body: dict | bytes

    """
    body = ChangeLoadbalancerDnsPtrRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_change_protection_post(request: web.Request, id, body=None) -> web.Response:
    """Change Load Balancer Protection

    Changes the protection configuration of a Load Balancer.

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LoadBalancersIdActionsChangeProtectionPostRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_change_type_post(request: web.Request, id, body=None) -> web.Response:
    """Change the Type of a Load Balancer

    Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.  **Call specific error codes**  | Code                         | Description                                                     | |------------------------------|-----------------------------------------------------------------| | &#x60;invalid_load_balancer_type&#x60; | The Load Balancer type does not fit for the given Load Balancer | 

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeTypeRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_delete_service_post(request: web.Request, id, body=None) -> web.Response:
    """Delete Service

    Delete a service of a Load Balancer.

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LoadBalancersIdActionsDeleteServicePostRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_detach_from_network_post(request: web.Request, id, body=None) -> web.Response:
    """Detach a Load Balancer from a Network

    Detaches a Load Balancer from a network.

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LoadBalancersIdActionsDetachFromNetworkPostRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_disable_public_interface_post(request: web.Request, id) -> web.Response:
    """Disable the public interface of a Load Balancer

    Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.  #### Call specific error codes  | Code                                      | Description                                                                    | |-------------------------------------------|--------------------------------------------------------------------------------| | &#x60;load_balancer_not_attached_to_network&#x60;   |  The Load Balancer is not attached to a network                                | | &#x60;targets_without_use_private_ip&#x60;          | The Load Balancer has targets that use the public IP instead of the private IP | 

    :param id: ID of the Load Balancer
    :type id: int

    """
    return web.Response(status=200)


async def load_balancers_id_actions_enable_public_interface_post(request: web.Request, id) -> web.Response:
    """Enable the public interface of a Load Balancer

    Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs.

    :param id: ID of the Load Balancer
    :type id: int

    """
    return web.Response(status=200)


async def load_balancers_id_actions_get(request: web.Request, id, sort=None, status=None) -> web.Response:
    """Get all Actions for a Load Balancer

    Returns all Action objects for a Load Balancer. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

    :param id: ID of the Load Balancer
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)


async def load_balancers_id_actions_remove_target_post(request: web.Request, id, body=None) -> web.Response:
    """Remove Target

    Removes a target from a Load Balancer.

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveTargetRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_id_actions_update_service_post(request: web.Request, id, body=None) -> web.Response:
    """Update Service

    Updates a Load Balancer Service.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LoadBalancerService.from_dict(body)
    return web.Response(status=200)
