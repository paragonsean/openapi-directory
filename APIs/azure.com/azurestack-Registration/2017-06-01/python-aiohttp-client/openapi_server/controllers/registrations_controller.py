from typing import List, Dict
from aiohttp import web

from openapi_server.models.activation_key_result import ActivationKeyResult
from openapi_server.models.registration import Registration
from openapi_server.models.registration_list import RegistrationList
from openapi_server.models.registration_parameter import RegistrationParameter
from openapi_server.models.registrations_list_default_response import RegistrationsListDefaultResponse
from openapi_server import util


async def registrations_create_or_update(request: web.Request, subscription_id, resource_group, registration_name, api_version, token) -> web.Response:
    """registrations_create_or_update

    Create or update an Azure Stack registration.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param token: Registration token
    :type token: dict | bytes

    """
    token = RegistrationParameter.from_dict(token)
    return web.Response(status=200)


async def registrations_delete(request: web.Request, subscription_id, resource_group, registration_name, api_version) -> web.Response:
    """registrations_delete

    Delete the requested Azure Stack registration.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registrations_get(request: web.Request, subscription_id, resource_group, registration_name, api_version) -> web.Response:
    """registrations_get

    Returns the properties of an Azure Stack registration.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registrations_get_activation_key(request: web.Request, subscription_id, resource_group, registration_name, api_version) -> web.Response:
    """registrations_get_activation_key

    Returns Azure Stack Activation Key.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registrations_list(request: web.Request, subscription_id, resource_group, api_version) -> web.Response:
    """registrations_list

    Returns a list of all registrations.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def registrations_update(request: web.Request, subscription_id, resource_group, registration_name, api_version, token) -> web.Response:
    """registrations_update

    Patch an Azure Stack registration.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param token: Registration token
    :type token: dict | bytes

    """
    token = RegistrationParameter.from_dict(token)
    return web.Response(status=200)
