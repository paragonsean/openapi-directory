from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_classification import StorageClassification
from openapi_server.models.storage_classification_collection import StorageClassificationCollection
from openapi_server import util


async def replication_storage_classifications_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, storage_classification_name) -> web.Response:
    """Gets the details of a storage classification.

    Gets the details of the specified storage classification.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param storage_classification_name: Storage classification name.
    :type storage_classification_name: str

    """
    return web.Response(status=200)


async def replication_storage_classifications_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of storage classification objects under a vault.

    Lists the storage classifications in the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def replication_storage_classifications_list_by_replication_fabrics(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Gets the list of storage classification objects under a fabric.

    Lists the storage classifications available in the specified fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Site name of interest.
    :type fabric_name: str

    """
    return web.Response(status=200)
