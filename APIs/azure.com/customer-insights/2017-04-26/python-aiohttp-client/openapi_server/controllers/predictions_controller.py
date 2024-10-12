from typing import List, Dict
from aiohttp import web

from openapi_server.models.prediction_list_result import PredictionListResult
from openapi_server.models.prediction_model_status import PredictionModelStatus
from openapi_server.models.prediction_resource_format import PredictionResourceFormat
from openapi_server.models.prediction_training_results import PredictionTrainingResults
from openapi_server import util


async def predictions_create_or_update(request: web.Request, resource_group_name, hub_name, prediction_name, api_version, subscription_id, parameters) -> web.Response:
    """predictions_create_or_update

    Creates a Prediction or updates an existing Prediction in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param prediction_name: The name of the Prediction.
    :type prediction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update Prediction operation.
    :type parameters: dict | bytes

    """
    parameters = PredictionResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def predictions_delete(request: web.Request, resource_group_name, hub_name, prediction_name, api_version, subscription_id) -> web.Response:
    """predictions_delete

    Deletes a Prediction in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param prediction_name: The name of the Prediction.
    :type prediction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def predictions_get(request: web.Request, resource_group_name, hub_name, prediction_name, api_version, subscription_id) -> web.Response:
    """predictions_get

    Gets a Prediction in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param prediction_name: The name of the Prediction.
    :type prediction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def predictions_get_model_status(request: web.Request, resource_group_name, hub_name, prediction_name, api_version, subscription_id) -> web.Response:
    """predictions_get_model_status

    Gets model status of the prediction.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param prediction_name: The name of the Prediction.
    :type prediction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def predictions_get_training_results(request: web.Request, resource_group_name, hub_name, prediction_name, api_version, subscription_id) -> web.Response:
    """predictions_get_training_results

    Gets training results.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param prediction_name: The name of the Prediction.
    :type prediction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def predictions_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """predictions_list_by_hub

    Gets all the predictions in the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def predictions_model_status(request: web.Request, resource_group_name, hub_name, prediction_name, api_version, subscription_id, parameters) -> web.Response:
    """predictions_model_status

    Creates or updates the model status of prediction.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param prediction_name: The name of the Prediction.
    :type prediction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update prediction model status operation.
    :type parameters: dict | bytes

    """
    parameters = PredictionModelStatus.from_dict(parameters)
    return web.Response(status=200)
