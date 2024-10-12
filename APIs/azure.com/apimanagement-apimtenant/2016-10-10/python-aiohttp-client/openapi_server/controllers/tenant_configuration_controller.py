from typing import List, Dict
from aiohttp import web

from openapi_server.models.deploy_configuration_parameters import DeployConfigurationParameters
from openapi_server.models.operation_result_contract import OperationResultContract
from openapi_server.models.save_configuration_parameter import SaveConfigurationParameter
from openapi_server.models.tenant_access_update_default_response import TenantAccessUpdateDefaultResponse
from openapi_server import util


async def tenant_configuration_deploy(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """tenant_configuration_deploy

    This operation applies changes from the specified Git branch to the configuration database. This is a long running operation and could take several minutes to complete.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Deploy Configuration parameters.
    :type parameters: dict | bytes

    """
    parameters = DeployConfigurationParameters.from_dict(parameters)
    return web.Response(status=200)


async def tenant_configuration_save(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """tenant_configuration_save

    This operation creates a commit with the current configuration snapshot to the specified branch in the repository. This is a long running operation and could take several minutes to complete.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Save Configuration parameters.
    :type parameters: dict | bytes

    """
    parameters = SaveConfigurationParameter.from_dict(parameters)
    return web.Response(status=200)


async def tenant_configuration_validate(request: web.Request, resource_group_name, service_name, api_version, subscription_id, parameters) -> web.Response:
    """tenant_configuration_validate

    This operation validates the changes in the specified Git branch. This is a long running operation and could take several minutes to complete.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Validate Configuration parameters.
    :type parameters: dict | bytes

    """
    parameters = DeployConfigurationParameters.from_dict(parameters)
    return web.Response(status=200)
