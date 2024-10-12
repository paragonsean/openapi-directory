from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_server_request import CreateServerRequest
from openapi_server.models.create_server_response import CreateServerResponse
from openapi_server.models.load_balancers_id_metrics_get200_response import LoadBalancersIdMetricsGet200Response
from openapi_server.models.servers_get200_response import ServersGet200Response
from openapi_server.models.servers_id_delete200_response import ServersIdDelete200Response
from openapi_server.models.servers_id_get200_response import ServersIdGet200Response
from openapi_server.models.update_server_request import UpdateServerRequest
from openapi_server import util


async def servers_get(request: web.Request, name=None, label_selector=None, sort=None, status=None) -> web.Response:
    """Get all Servers

    Returns all existing Server objects

    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times. The response will only contain Server matching the status
    :type status: str

    """
    return web.Response(status=200)


async def servers_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Server

    Deletes a Server. This immediately removes the Server from your account, and it is no longer accessible.

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_get(request: web.Request, id) -> web.Response:
    """Get a Server

    Returns a specific Server object. The Server must exist inside the Project

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_metrics_get(request: web.Request, id, type, start, end, step=None) -> web.Response:
    """Get Metrics for a Server

    Get Metrics for specified Server.  You must specify the type of metric to get: cpu, disk or network. You can also specify more than one type by comma separation, e.g. cpu,disk.  Depending on the type you will get different time series data  | Type    | Timeseries              | Unit      | Description                                          | |---------|-------------------------|-----------|------------------------------------------------------| | cpu     | cpu                     | percent   | Percent CPU usage                                    | | disk    | disk.0.iops.read        | iop/s     | Number of read IO operations per second              | |         | disk.0.iops.write       | iop/s     | Number of write IO operations per second             | |         | disk.0.bandwidth.read   | bytes/s   | Bytes read per second                                | |         | disk.0.bandwidth.write  | bytes/s   | Bytes written per second                             | | network | network.0.pps.in        | packets/s | Public Network interface packets per second received | |         | network.0.pps.out       | packets/s | Public Network interface packets per second sent     | |         | network.0.bandwidth.in  | bytes/s   | Public Network interface bytes/s received            | |         | network.0.bandwidth.out | bytes/s   | Public Network interface bytes/s sent                |  Metrics are available for the last 30 days only.  If you do not provide the step argument we will automatically adjust it so that a maximum of 200 samples are returned.  We limit the number of samples returned to a maximum of 500 and will adjust the step parameter accordingly. 

    :param id: ID of the Server
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


async def servers_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a Server

    Updates a Server. You can update a Server’s name and a Server’s labels. Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes). Also note that when updating labels, the Server’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateServerRequest.from_dict(body)
    return web.Response(status=200)


async def servers_post(request: web.Request, body=None) -> web.Response:
    """Create a Server

    Creates a new Server. Returns preliminary information about the Server as well as an Action that covers progress of creation.

    :param body: Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).  For &#x60;server_type&#x60; you can either use the ID as listed in &#x60;/server_types&#x60; or its name.  For &#x60;image&#x60; you can either use the ID as listed in &#x60;/images&#x60; or its name.  If you want to create the Server in a Location, you must set &#x60;location&#x60; to the ID or name as listed in &#x60;/locations&#x60;. This is the recommended way. You can be even more specific by setting &#x60;datacenter&#x60; to the ID or name as listed in &#x60;/datacenters&#x60;. However we only recommend this if you want to assign a specific Primary IP to the Server which is located in the specified Datacenter.  Some properties like &#x60;start_after_create&#x60; or &#x60;automount&#x60; will trigger Actions after the Server is created. Those Actions are listed in the &#x60;next_actions&#x60; field in the response.  For accessing your Server we strongly recommend to use SSH keys by passing the respective key IDs in &#x60;ssh_keys&#x60;. If you do not specify any &#x60;ssh_keys&#x60; we will generate a root password for you and return it in the response.  Please note that provided user-data is stored in our systems. While we take measures to protect it we highly recommend that you don’t use it to store passwords or other sensitive information.  #### Call specific error codes  | Code                             | Description                                                | |----------------------------------|------------------------------------------------------------| | &#x60;placement_error&#x60;                | An error during the placement occurred                     | | &#x60;primary_ip_assigned&#x60;            | The specified Primary IP is already assigned to a server   | | &#x60;primary_ip_datacenter_mismatch&#x60; | The specified Primary IP is in a different datacenter      | | &#x60;primary_ip_version_mismatch&#x60;    | The specified Primary IP has the wrong IP Version          | 
    :type body: dict | bytes

    """
    body = CreateServerRequest.from_dict(body)
    return web.Response(status=200)
