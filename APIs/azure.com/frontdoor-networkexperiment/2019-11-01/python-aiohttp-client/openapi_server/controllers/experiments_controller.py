from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.experiment import Experiment
from openapi_server.models.experiment_list import ExperimentList
from openapi_server.models.experiment_update_model import ExperimentUpdateModel
from openapi_server import util


async def experiments_create_or_update(request: web.Request, subscription_id, api_version, resource_group_name, profile_name, experiment_name, parameters) -> web.Response:
    """Creates or updates an Experiment

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str
    :param experiment_name: The Experiment identifier associated with the Experiment
    :type experiment_name: str
    :param parameters: The Experiment resource
    :type parameters: dict | bytes

    """
    parameters = Experiment.from_dict(parameters)
    return web.Response(status=200)


async def experiments_delete(request: web.Request, subscription_id, api_version, resource_group_name, profile_name, experiment_name) -> web.Response:
    """Deletes an Experiment

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str
    :param experiment_name: The Experiment identifier associated with the Experiment
    :type experiment_name: str

    """
    return web.Response(status=200)


async def experiments_get(request: web.Request, subscription_id, api_version, resource_group_name, profile_name, experiment_name) -> web.Response:
    """Gets an Experiment by ExperimentName

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str
    :param experiment_name: The Experiment identifier associated with the Experiment
    :type experiment_name: str

    """
    return web.Response(status=200)


async def experiments_list_by_profile(request: web.Request, subscription_id, api_version, resource_group_name, profile_name) -> web.Response:
    """Gets a list of Experiments

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str

    """
    return web.Response(status=200)


async def experiments_update(request: web.Request, subscription_id, api_version, resource_group_name, profile_name, experiment_name, parameters) -> web.Response:
    """Updates an Experiment by Experiment id

    Updates an Experiment

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str
    :param experiment_name: The Experiment identifier associated with the Experiment
    :type experiment_name: str
    :param parameters: The Experiment Update Model
    :type parameters: dict | bytes

    """
    parameters = ExperimentUpdateModel.from_dict(parameters)
    return web.Response(status=200)
