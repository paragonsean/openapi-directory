from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server import util


async def invoke_infrastructure_command(request: web.Request, api_version, command, service_id=None, timeout=None) -> web.Response:
    """Invokes an administrative command on the given Infrastructure Service instance.

    For clusters that have one or more instances of the Infrastructure Service configured, this API provides a way to send infrastructure-specific commands to a particular instance of the Infrastructure Service.  Available commands and their corresponding response formats vary depending upon the infrastructure on which the cluster is running.  This API supports the Service Fabric platform; it is not meant to be used directly from your code. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param command: The text of the command to be invoked. The content of the command is infrastructure-specific.
    :type command: str
    :param service_id: The identity of the infrastructure service. This is  the full name of the infrastructure service without the &#39;fabric:&#39; URI scheme. This parameter required only for the cluster that have more than one instance of infrastructure service running.
    :type service_id: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def invoke_infrastructure_query(request: web.Request, api_version, command, service_id=None, timeout=None) -> web.Response:
    """Invokes a read-only query on the given infrastructure service instance.

    For clusters that have one or more instances of the Infrastructure Service configured, this API provides a way to send infrastructure-specific queries to a particular instance of the Infrastructure Service.  Available commands and their corresponding response formats vary depending upon the infrastructure on which the cluster is running.  This API supports the Service Fabric platform; it is not meant to be used directly from your code. 

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param command: The text of the command to be invoked. The content of the command is infrastructure-specific.
    :type command: str
    :param service_id: The identity of the infrastructure service. This is  the full name of the infrastructure service without the &#39;fabric:&#39; URI scheme. This parameter required only for the cluster that have more than one instance of infrastructure service running.
    :type service_id: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)
