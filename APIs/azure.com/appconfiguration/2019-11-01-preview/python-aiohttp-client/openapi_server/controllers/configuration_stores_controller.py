from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.api_key_list_result import ApiKeyListResult
from openapi_server.models.configuration_store import ConfigurationStore
from openapi_server.models.configuration_store_list_result import ConfigurationStoreListResult
from openapi_server.models.configuration_store_update_parameters import ConfigurationStoreUpdateParameters
from openapi_server.models.error import Error
from openapi_server.models.key_value import KeyValue
from openapi_server.models.list_key_value_parameters import ListKeyValueParameters
from openapi_server.models.regenerate_key_parameters import RegenerateKeyParameters
from openapi_server import util


async def configuration_stores_create(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, config_store_creation_parameters) -> web.Response:
    """configuration_stores_create

    Creates a configuration store with the specified parameters.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param config_store_creation_parameters: The parameters for creating a configuration store.
    :type config_store_creation_parameters: dict | bytes

    """
    config_store_creation_parameters = ConfigurationStore.from_dict(config_store_creation_parameters)
    return web.Response(status=200)


async def configuration_stores_delete(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version) -> web.Response:
    """configuration_stores_delete

    Deletes a configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def configuration_stores_get(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version) -> web.Response:
    """configuration_stores_get

    Gets the properties of the specified configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def configuration_stores_list(request: web.Request, subscription_id, api_version, skip_token=None) -> web.Response:
    """configuration_stores_list

    Lists the configuration stores for a given subscription.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param skip_token: A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    :type skip_token: str

    """
    return web.Response(status=200)


async def configuration_stores_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, skip_token=None) -> web.Response:
    """configuration_stores_list_by_resource_group

    Lists the configuration stores for a given resource group.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param skip_token: A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    :type skip_token: str

    """
    return web.Response(status=200)


async def configuration_stores_list_key_value(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, list_key_value_parameters) -> web.Response:
    """configuration_stores_list_key_value

    Lists a configuration store key-value.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param list_key_value_parameters: The parameters for retrieving a key-value.
    :type list_key_value_parameters: dict | bytes

    """
    list_key_value_parameters = ListKeyValueParameters.from_dict(list_key_value_parameters)
    return web.Response(status=200)


async def configuration_stores_list_keys(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, skip_token=None) -> web.Response:
    """configuration_stores_list_keys

    Lists the access key for the specified configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param skip_token: A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
    :type skip_token: str

    """
    return web.Response(status=200)


async def configuration_stores_regenerate_key(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, regenerate_key_parameters) -> web.Response:
    """configuration_stores_regenerate_key

    Regenerates an access key for the specified configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param regenerate_key_parameters: The parameters for regenerating an access key.
    :type regenerate_key_parameters: dict | bytes

    """
    regenerate_key_parameters = RegenerateKeyParameters.from_dict(regenerate_key_parameters)
    return web.Response(status=200)


async def configuration_stores_update(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, config_store_update_parameters) -> web.Response:
    """configuration_stores_update

    Updates a configuration store with the specified parameters.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param config_store_update_parameters: The parameters for updating a configuration store.
    :type config_store_update_parameters: dict | bytes

    """
    config_store_update_parameters = ConfigurationStoreUpdateParameters.from_dict(config_store_update_parameters)
    return web.Response(status=200)
