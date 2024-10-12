from typing import List, Dict
from aiohttp import web

from openapi_server.models.kpi_definition import KpiDefinition
from openapi_server.models.profile_list_result import ProfileListResult
from openapi_server.models.profile_resource_format import ProfileResourceFormat
from openapi_server import util


async def profiles_create_or_update(request: web.Request, resource_group_name, hub_name, profile_name, api_version, subscription_id, parameters) -> web.Response:
    """profiles_create_or_update

    Creates a profile within a Hub, or updates an existing profile.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param profile_name: The name of the profile.
    :type profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/delete Profile type operation
    :type parameters: dict | bytes

    """
    parameters = ProfileResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def profiles_delete(request: web.Request, resource_group_name, hub_name, profile_name, api_version, subscription_id, locale_code=None) -> web.Response:
    """profiles_delete

    Deletes a profile within a hub

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param profile_name: The name of the profile.
    :type profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param locale_code: Locale of profile to retrieve, default is en-us.
    :type locale_code: str

    """
    return web.Response(status=200)


async def profiles_get(request: web.Request, resource_group_name, hub_name, profile_name, api_version, subscription_id, locale_code=None) -> web.Response:
    """profiles_get

    Gets information about the specified profile.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param profile_name: The name of the profile.
    :type profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param locale_code: Locale of profile to retrieve, default is en-us.
    :type locale_code: str

    """
    return web.Response(status=200)


async def profiles_get_enriching_kpis(request: web.Request, resource_group_name, hub_name, profile_name, api_version, subscription_id) -> web.Response:
    """profiles_get_enriching_kpis

    Gets the KPIs that enrich the profile Type identified by the supplied name. Enrichment happens through participants of the Interaction on an Interaction KPI and through Relationships for Profile KPIs.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param profile_name: The name of the profile.
    :type profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def profiles_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id, locale_code=None) -> web.Response:
    """profiles_list_by_hub

    Gets all profile in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param locale_code: Locale of profile to retrieve, default is en-us.
    :type locale_code: str

    """
    return web.Response(status=200)
