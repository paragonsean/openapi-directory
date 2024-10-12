from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_from_json_scale_unit_parameters_list import CreateFromJsonScaleUnitParametersList
from openapi_server.models.scale_out_scale_unit_parameters_list import ScaleOutScaleUnitParametersList
from openapi_server.models.scale_unit import ScaleUnit
from openapi_server.models.scale_unit_list import ScaleUnitList
from openapi_server import util


async def scale_units_create_from_json(request: web.Request, subscription_id, resource_group_name, location, scale_unit, api_version, creation_data) -> web.Response:
    """scale_units_create_from_json

    Add a new scale unit.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param scale_unit: Name of the scale units.
    :type scale_unit: str
    :param api_version: Client API Version.
    :type api_version: str
    :param creation_data: A list of input data that allows for creating the new scale unit.
    :type creation_data: dict | bytes

    """
    creation_data = CreateFromJsonScaleUnitParametersList.from_dict(creation_data)
    return web.Response(status=200)


async def scale_units_get(request: web.Request, subscription_id, resource_group_name, location, scale_unit, api_version) -> web.Response:
    """scale_units_get

    Returns the requested scale unit.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param scale_unit: Name of the scale units.
    :type scale_unit: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def scale_units_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """scale_units_list

    Returns a list of all scale units at a location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)


async def scale_units_scale_out(request: web.Request, subscription_id, resource_group_name, location, scale_unit, api_version, scale_unit_node_parameters) -> web.Response:
    """scale_units_scale_out

    Scales out a scale unit.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param scale_unit: Name of the scale units.
    :type scale_unit: str
    :param api_version: Client API Version.
    :type api_version: str
    :param scale_unit_node_parameters: A list of input data that allows for adding a set of scale unit nodes.
    :type scale_unit_node_parameters: dict | bytes

    """
    scale_unit_node_parameters = ScaleOutScaleUnitParametersList.from_dict(scale_unit_node_parameters)
    return web.Response(status=200)
