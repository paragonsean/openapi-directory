from typing import List, Dict
from aiohttp import web

from openapi_server.models.deployed_code_package_info import DeployedCodePackageInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.restart_deployed_code_package_description import RestartDeployedCodePackageDescription
from openapi_server import util


async def get_deployed_code_package_info_list(request: web.Request, api_version, node_name, application_id, service_manifest_name=None, code_package_name=None, timeout=None) -> web.Response:
    """Gets the list of code packages deployed on a Service Fabric node.

    Gets the list of code packages deployed on a Service Fabric node for the given application.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param service_manifest_name: The name of a service manifest registered as part of an application type in a Service Fabric cluster.
    :type service_manifest_name: str
    :param code_package_name: The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster.
    :type code_package_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def restart_deployed_code_package(request: web.Request, api_version, node_name, application_id, restart_deployed_code_package_description, timeout=None) -> web.Response:
    """Restarts a code package deployed on a Service Fabric node in a cluster.

    Restarts a code package deployed on a Service Fabric node in a cluster. This aborts the code package process, which will restart all the user service replicas hosted in that process.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param restart_deployed_code_package_description: Describes the deployed code package on Service Fabric node to restart.
    :type restart_deployed_code_package_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    restart_deployed_code_package_description = RestartDeployedCodePackageDescription.from_dict(restart_deployed_code_package_description)
    return web.Response(status=200)
