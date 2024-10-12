from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_api_request_body import ContainerApiRequestBody
from openapi_server.models.container_api_response import ContainerApiResponse
from openapi_server.models.container_logs import ContainerLogs
from openapi_server.models.deployed_code_package_info import DeployedCodePackageInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.restart_deployed_code_package_description import RestartDeployedCodePackageDescription
from openapi_server import util


async def get_container_logs_deployed_on_node(request: web.Request, api_version, node_name, application_id, service_manifest_name, code_package_name, tail=None, previous=None, timeout=None) -> web.Response:
    """Gets the container logs for container deployed on a Service Fabric node.

    Gets the container logs for container deployed on a Service Fabric node for the given code package.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param service_manifest_name: The name of a service manifest registered as part of an application type in a Service Fabric cluster.
    :type service_manifest_name: str
    :param code_package_name: The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster.
    :type code_package_name: str
    :param tail: Number of lines to show from the end of the logs. Default is 100. &#39;all&#39; to show the complete logs.
    :type tail: str
    :param previous: Specifies whether to get container logs from exited/dead containers of the code package instance.
    :type previous: bool
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_deployed_code_package_info_list(request: web.Request, api_version, node_name, application_id, service_manifest_name=None, code_package_name=None, timeout=None) -> web.Response:
    """Gets the list of code packages deployed on a Service Fabric node.

    Gets the list of code packages deployed on a Service Fabric node for the given application.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param service_manifest_name: The name of a service manifest registered as part of an application type in a Service Fabric cluster.
    :type service_manifest_name: str
    :param code_package_name: The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster.
    :type code_package_name: str
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def invoke_container_api(request: web.Request, api_version, node_name, application_id, service_manifest_name, code_package_name, code_package_instance_id, container_api_request_body, timeout=None) -> web.Response:
    """Invoke container API on a container deployed on a Service Fabric node.

    Invoke container API on a container deployed on a Service Fabric node for the given code package.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.2&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param service_manifest_name: The name of a service manifest registered as part of an application type in a Service Fabric cluster.
    :type service_manifest_name: str
    :param code_package_name: The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster.
    :type code_package_name: str
    :param code_package_instance_id: ID that uniquely identifies a code package instance deployed on a service fabric node.
    :type code_package_instance_id: str
    :param container_api_request_body: Parameters for making container API call
    :type container_api_request_body: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    container_api_request_body = ContainerApiRequestBody.from_dict(container_api_request_body)
    return web.Response(status=200)


async def restart_deployed_code_package(request: web.Request, api_version, node_name, application_id, restart_deployed_code_package_description, timeout=None) -> web.Response:
    """Restarts a code package deployed on a Service Fabric node in a cluster.

    Restarts a code package deployed on a Service Fabric node in a cluster. This aborts the code package process, which will restart all the user service replicas hosted in that process.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param restart_deployed_code_package_description: Describes the deployed code package on Service Fabric node to restart.
    :type restart_deployed_code_package_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    restart_deployed_code_package_description = RestartDeployedCodePackageDescription.from_dict(restart_deployed_code_package_description)
    return web.Response(status=200)
