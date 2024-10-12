from typing import List, Dict
from aiohttp import web

from openapi_server.models.workload_classifier import WorkloadClassifier
from openapi_server.models.workload_classifier_list_result import WorkloadClassifierListResult
from openapi_server import util


async def workload_classifiers_create_or_update(request: web.Request, resource_group_name, server_name, database_name, workload_group_name, workload_classifier_name, subscription_id, api_version, parameters) -> web.Response:
    """workload_classifiers_create_or_update

    Creates or updates a workload classifier.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param workload_group_name: The name of the workload group from which to receive the classifier from.
    :type workload_group_name: str
    :param workload_classifier_name: The name of the workload classifier to create/update.
    :type workload_classifier_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The properties of the workload classifier.
    :type parameters: dict | bytes

    """
    parameters = WorkloadClassifier.from_dict(parameters)
    return web.Response(status=200)


async def workload_classifiers_delete(request: web.Request, resource_group_name, server_name, database_name, workload_group_name, workload_classifier_name, subscription_id, api_version) -> web.Response:
    """workload_classifiers_delete

    Deletes a workload classifier.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param workload_group_name: The name of the workload group from which to receive the classifier from.
    :type workload_group_name: str
    :param workload_classifier_name: The name of the workload classifier to delete.
    :type workload_classifier_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def workload_classifiers_get(request: web.Request, resource_group_name, server_name, database_name, workload_group_name, workload_classifier_name, subscription_id, api_version) -> web.Response:
    """workload_classifiers_get

    Gets a workload classifier

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param workload_group_name: The name of the workload group from which to receive the classifier from.
    :type workload_group_name: str
    :param workload_classifier_name: The name of the workload classifier.
    :type workload_classifier_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def workload_classifiers_list_by_workload_group(request: web.Request, resource_group_name, server_name, database_name, workload_group_name, subscription_id, api_version) -> web.Response:
    """workload_classifiers_list_by_workload_group

    Gets the list of workload classifiers for a workload group

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param workload_group_name: The name of the workload group from which to receive the classifiers from.
    :type workload_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
