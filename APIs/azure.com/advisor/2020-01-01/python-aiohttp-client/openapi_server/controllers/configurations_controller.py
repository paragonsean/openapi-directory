from typing import List, Dict
from aiohttp import web

from openapi_server.models.arm_error_response import ArmErrorResponse
from openapi_server.models.config_data import ConfigData
from openapi_server.models.configuration_list_result import ConfigurationListResult
from openapi_server import util


async def configurations_create_in_resource_group(request: web.Request, api_version, subscription_id, configuration_name, resource_group, config_contract) -> web.Response:
    """Create/Overwrite Azure Advisor configuration.

    

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param configuration_name: Advisor configuration name. Value must be &#39;default&#39;
    :type configuration_name: str
    :param resource_group: The name of the Azure resource group.
    :type resource_group: str
    :param config_contract: The Azure Advisor configuration data structure.
    :type config_contract: dict | bytes

    """
    config_contract = ConfigData.from_dict(config_contract)
    return web.Response(status=200)


async def configurations_create_in_subscription(request: web.Request, api_version, subscription_id, configuration_name, config_contract) -> web.Response:
    """Create/Overwrite Azure Advisor configuration.

    Create/Overwrite Azure Advisor configuration and also delete all configurations of contained resource groups.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param configuration_name: Advisor configuration name. Value must be &#39;default&#39;
    :type configuration_name: str
    :param config_contract: The Azure Advisor configuration data structure.
    :type config_contract: dict | bytes

    """
    config_contract = ConfigData.from_dict(config_contract)
    return web.Response(status=200)


async def configurations_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group) -> web.Response:
    """Retrieve Azure Advisor configurations.

    

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_group: The name of the Azure resource group.
    :type resource_group: str

    """
    return web.Response(status=200)


async def configurations_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """Retrieve Azure Advisor configurations.

    Retrieve Azure Advisor configurations and also retrieve configurations of contained resource groups.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)
