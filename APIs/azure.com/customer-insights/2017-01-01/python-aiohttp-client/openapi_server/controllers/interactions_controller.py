from typing import List, Dict
from aiohttp import web

from openapi_server.models.interaction_list_result import InteractionListResult
from openapi_server.models.interaction_resource_format import InteractionResourceFormat
from openapi_server.models.suggest_relationship_links_response import SuggestRelationshipLinksResponse
from openapi_server import util


async def interactions_create_or_update(request: web.Request, resource_group_name, hub_name, interaction_name, api_version, subscription_id, parameters) -> web.Response:
    """interactions_create_or_update

    Creates an interaction or updates an existing interaction within a hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param interaction_name: The name of the interaction.
    :type interaction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Interaction operation.
    :type parameters: dict | bytes

    """
    parameters = InteractionResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def interactions_get(request: web.Request, resource_group_name, hub_name, interaction_name, api_version, subscription_id, locale_code=None) -> web.Response:
    """interactions_get

    Gets information about the specified interaction.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param interaction_name: The name of the interaction.
    :type interaction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param locale_code: Locale of interaction to retrieve, default is en-us.
    :type locale_code: str

    """
    return web.Response(status=200)


async def interactions_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id, locale_code=None) -> web.Response:
    """interactions_list_by_hub

    Gets all interactions in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param locale_code: Locale of interaction to retrieve, default is en-us.
    :type locale_code: str

    """
    return web.Response(status=200)


async def interactions_suggest_relationship_links(request: web.Request, resource_group_name, hub_name, interaction_name, api_version, subscription_id) -> web.Response:
    """interactions_suggest_relationship_links

    Suggests relationships to create relationship links.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param interaction_name: The name of the interaction.
    :type interaction_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
