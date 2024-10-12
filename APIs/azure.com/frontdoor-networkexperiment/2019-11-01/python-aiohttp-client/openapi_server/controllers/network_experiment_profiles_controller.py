from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.profile import Profile
from openapi_server.models.profile_list import ProfileList
from openapi_server.models.profile_update_model import ProfileUpdateModel
from openapi_server import util


async def network_experiment_profiles_create_or_update(request: web.Request, profile_name, subscription_id, api_version, resource_group_name, parameters) -> web.Response:
    """Creates an NetworkExperiment Profile

    

    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param parameters: An Network Experiment Profile
    :type parameters: dict | bytes

    """
    parameters = Profile.from_dict(parameters)
    return web.Response(status=200)


async def network_experiment_profiles_delete(request: web.Request, subscription_id, api_version, resource_group_name, profile_name) -> web.Response:
    """Deletes an NetworkExperiment Profile by ProfileName

    

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


async def network_experiment_profiles_get(request: web.Request, subscription_id, api_version, resource_group_name, profile_name) -> web.Response:
    """Gets an NetworkExperiment Profile by ProfileName

    

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


async def network_experiment_profiles_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets a list of Network Experiment Profiles under a subscription

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def network_experiment_profiles_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Gets a list of Network Experiment Profiles within a resource group under a subscription

    

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def network_experiment_profiles_update(request: web.Request, subscription_id, api_version, resource_group_name, profile_name, parameters) -> web.Response:
    """Updates an NetworkExperimentProfiles by NetworkExperimentProfile name

    Updates an NetworkExperimentProfiles

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: The Profile identifier associated with the Tenant and Partner
    :type profile_name: str
    :param parameters: The Profile Update Model
    :type parameters: dict | bytes

    """
    parameters = ProfileUpdateModel.from_dict(parameters)
    return web.Response(status=200)
