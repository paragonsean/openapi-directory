from typing import List, Dict
from aiohttp import web

from openapi_server.models.deployed_service_type_info import DeployedServiceTypeInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.service_type_info import ServiceTypeInfo
from openapi_server.models.service_type_manifest import ServiceTypeManifest
from openapi_server import util


async def get_deployed_service_type_info_by_name(request: web.Request, api_version, node_name, application_id, service_type_name, service_manifest_name=None, timeout=None) -> web.Response:
    """Gets the information about a specified service type of the application deployed on a node in a Service Fabric cluster.

    Gets the list containing the information about a specific service type from the applications deployed on a node in a Service Fabric cluster. The response includes the name of the service type, its registration status, the code package that registered it and activation id of the service package. Each entry represents one activation of a service type, differentiated by the activation id.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param service_type_name: Specifies the name of a Service Fabric service type.
    :type service_type_name: str
    :param service_manifest_name: The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest.
    :type service_manifest_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_deployed_service_type_info_list(request: web.Request, api_version, node_name, application_id, service_manifest_name=None, timeout=None) -> web.Response:
    """Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster.

    Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster. The response includes the name of the service type, its registration status, the code package that registered it and activation id of the service package.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param node_name: The name of the node.
    :type node_name: str
    :param application_id: The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.
    :type application_id: str
    :param service_manifest_name: The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest.
    :type service_manifest_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_service_manifest(request: web.Request, api_version, application_type_name, application_type_version, service_manifest_name, timeout=None) -> web.Response:
    """Gets the manifest describing a service type.

    Gets the manifest describing a service type. The response contains the service manifest XML as a string.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param application_type_name: The name of the application type.
    :type application_type_name: str
    :param application_type_version: The version of the application type.
    :type application_type_version: str
    :param service_manifest_name: The name of a service manifest registered as part of an application type in a Service Fabric cluster.
    :type service_manifest_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_service_type_info_list(request: web.Request, api_version, application_type_name, application_type_version, timeout=None) -> web.Response:
    """Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster.

    Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster. The response includes the name of the service type, the name and version of the service manifest the type is defined in, kind (stateless or stateless) of the service type and other information about it.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param application_type_name: The name of the application type.
    :type application_type_name: str
    :param application_type_version: The version of the application type.
    :type application_type_version: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)
