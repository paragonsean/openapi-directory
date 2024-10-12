from typing import List, Dict
from aiohttp import web

from openapi_server.models.compose_deployment_status_info import ComposeDeploymentStatusInfo
from openapi_server.models.compose_deployment_upgrade_description import ComposeDeploymentUpgradeDescription
from openapi_server.models.compose_deployment_upgrade_progress_info import ComposeDeploymentUpgradeProgressInfo
from openapi_server.models.create_compose_deployment_description import CreateComposeDeploymentDescription
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_compose_deployment_status_info_list import PagedComposeDeploymentStatusInfoList
from openapi_server import util


async def create_compose_deployment(request: web.Request, api_version, create_compose_deployment_description, timeout=None) -> web.Response:
    """Creates a Service Fabric compose deployment.

    Compose is a file format that describes multi-container applications. This API allows deploying container based applications defined in compose format in a Service Fabric cluster. Once the deployment is created it&#39;s status can be tracked via &#x60;GetComposeDeploymentStatus&#x60; API.

    :param api_version: The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;.
    :type api_version: str
    :param create_compose_deployment_description: Describes the compose deployment that needs to be created.
    :type create_compose_deployment_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    create_compose_deployment_description = CreateComposeDeploymentDescription.from_dict(create_compose_deployment_description)
    return web.Response(status=200)


async def get_compose_deployment_status(request: web.Request, api_version, deployment_name, timeout=None) -> web.Response:
    """Gets information about a Service Fabric compose deployment.

    Returns the status of the compose deployment that was created or in the process of being created in the Service Fabric cluster and whose name matches the one specified as the parameter. The response includes the name, status and other details about the deployment.

    :param api_version: The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;.
    :type api_version: str
    :param deployment_name: The identity of the deployment.
    :type deployment_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_compose_deployment_status_list(request: web.Request, api_version, continuation_token=None, max_results=None, timeout=None) -> web.Response:
    """Gets the list of compose deployments created in the Service Fabric cluster.

    Gets the status about the compose deployments that were created or in the process of being created in the Service Fabric cluster. The response includes the name, status and other details about the compose deployments. If the list of deployments do not fit in a page, one page of results is returned as well as a continuation token which can be used to get the next page.

    :param api_version: The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;.
    :type api_version: str
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param max_results: The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message.
    :type max_results: int
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_compose_deployment_upgrade_progress(request: web.Request, api_version, deployment_name, timeout=None) -> web.Response:
    """Gets details for the latest upgrade performed on this Service Fabric compose deployment.

    Returns the information about the state of the compose deployment upgrade along with details to aid debugging application health issues.

    :param api_version: The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;.
    :type api_version: str
    :param deployment_name: The identity of the deployment.
    :type deployment_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def remove_compose_deployment(request: web.Request, api_version, deployment_name, timeout=None) -> web.Response:
    """Deletes an existing Service Fabric compose deployment from cluster.

    Deletes an existing Service Fabric compose deployment.

    :param api_version: The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;.
    :type api_version: str
    :param deployment_name: The identity of the deployment.
    :type deployment_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def start_compose_deployment_upgrade(request: web.Request, api_version, deployment_name, compose_deployment_upgrade_description, timeout=None) -> web.Response:
    """Starts upgrading a compose deployment in the Service Fabric cluster.

    Validates the supplied upgrade parameters and starts upgrading the deployment if the parameters are valid.

    :param api_version: The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;.
    :type api_version: str
    :param deployment_name: The identity of the deployment.
    :type deployment_name: str
    :param compose_deployment_upgrade_description: Parameters for upgrading compose deployment.
    :type compose_deployment_upgrade_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    compose_deployment_upgrade_description = ComposeDeploymentUpgradeDescription.from_dict(compose_deployment_upgrade_description)
    return web.Response(status=200)
