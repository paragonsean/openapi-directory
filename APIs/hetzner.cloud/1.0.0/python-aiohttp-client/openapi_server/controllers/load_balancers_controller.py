from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_load_balancer_request import CreateLoadBalancerRequest
from openapi_server.models.load_balancers_get200_response import LoadBalancersGet200Response
from openapi_server.models.load_balancers_id_get200_response import LoadBalancersIdGet200Response
from openapi_server.models.load_balancers_id_metrics_get200_response import LoadBalancersIdMetricsGet200Response
from openapi_server.models.load_balancers_id_put_request import LoadBalancersIdPutRequest
from openapi_server.models.load_balancers_post201_response import LoadBalancersPost201Response
from openapi_server import util


async def load_balancers_get(request: web.Request, sort=None, name=None, label_selector=None) -> web.Response:
    """Get all Load Balancers

    Gets all existing Load Balancers that you have available.

    :param sort: Can be used multiple times.
    :type sort: str
    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str

    """
    return web.Response(status=200)


async def load_balancers_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Load Balancer

    Deletes a Load Balancer.

    :param id: ID of the Load Balancer
    :type id: int

    """
    return web.Response(status=200)


async def load_balancers_id_get(request: web.Request, id) -> web.Response:
    """Get a Load Balancer

    Gets a specific Load Balancer object.

    :param id: ID of the Load Balancer
    :type id: int

    """
    return web.Response(status=200)


async def load_balancers_id_metrics_get(request: web.Request, id, type, start, end, step=None) -> web.Response:
    """Get Metrics for a LoadBalancer

    You must specify the type of metric to get: &#x60;open_connections&#x60;, &#x60;connections_per_second&#x60;, &#x60;requests_per_second&#x60; or &#x60;bandwidth&#x60;. You can also specify more than one type by comma separation, e.g. &#x60;requests_per_second,bandwidth&#x60;.  Depending on the type you will get different time series data:  |Type | Timeseries | Unit | Description | |---- |------------|------|-------------| | open_connections | open_connections | number | Open connections | | connections_per_second | connections_per_second | connections/s | Connections per second | | requests_per_second | requests_per_second | requests/s | Requests per second | | bandwidth | bandwidth.in | bytes/s | Ingress bandwidth | || bandwidth.out | bytes/s | Egress bandwidth |  Metrics are available for the last 30 days only.  If you do not provide the step argument we will automatically adjust it so that 200 samples are returned.  We limit the number of samples to a maximum of 500 and will adjust the step parameter accordingly. 

    :param id: ID of the Load Balancer
    :type id: int
    :param type: Type of metrics to get
    :type type: str
    :param start: Start of period to get Metrics for (in ISO-8601 format)
    :type start: str
    :param end: End of period to get Metrics for (in ISO-8601 format)
    :type end: str
    :param step: Resolution of results in seconds
    :type step: str

    """
    return web.Response(status=200)


async def load_balancers_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a Load Balancer

    Updates a Load Balancer. You can update a Load Balancer’s name and a Load Balancer’s labels.  Note that when updating labels, the Load Balancer’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Load Balancer object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the Load Balancer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LoadBalancersIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def load_balancers_post(request: web.Request, body=None) -> web.Response:
    """Create a Load Balancer

    Creates a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP is not owned by the owner of the project of the Load Balancer                                  | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;source_port_already_used&#x60;              | The source port you are trying to add is already in use                                               | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateLoadBalancerRequest.from_dict(body)
    return web.Response(status=200)
