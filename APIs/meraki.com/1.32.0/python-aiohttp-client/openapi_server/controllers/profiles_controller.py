from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_sensor_alerts_profile_request import CreateNetworkSensorAlertsProfileRequest
from openapi_server.models.create_organization_alerts_profile_request import CreateOrganizationAlertsProfileRequest
from openapi_server.models.get_network_sensor_alerts_profiles200_response_inner import GetNetworkSensorAlertsProfiles200ResponseInner
from openapi_server.models.get_network_sm_profiles200_response_inner import GetNetworkSmProfiles200ResponseInner
from openapi_server.models.get_organization_config_template_switch_profile_ports200_response_inner import GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner
from openapi_server.models.get_organization_config_template_switch_profiles200_response import GetOrganizationConfigTemplateSwitchProfiles200Response
from openapi_server.models.update_network_sensor_alerts_profile_request import UpdateNetworkSensorAlertsProfileRequest
from openapi_server.models.update_organization_alerts_profile_request import UpdateOrganizationAlertsProfileRequest
from openapi_server.models.update_organization_config_template_switch_profile_port_request import UpdateOrganizationConfigTemplateSwitchProfilePortRequest
from openapi_server import util


async def create_network_sensor_alerts_profile_2(request: web.Request, network_id, body) -> web.Response:
    """Creates a sensor alert profile for a network.

    Creates a sensor alert profile for a network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSensorAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_alerts_profile_2(request: web.Request, organization_id, body) -> web.Response:
    """Create an organization-wide alert configuration

    Create an organization-wide alert configuration

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_sensor_alerts_profile_2(request: web.Request, network_id, id) -> web.Response:
    """Deletes a sensor alert profile from a network.

    Deletes a sensor alert profile from a network.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organization_alerts_profile_2(request: web.Request, organization_id, alert_config_id) -> web.Response:
    """Removes an organization-wide alert config

    Removes an organization-wide alert config

    :param organization_id: 
    :type organization_id: str
    :param alert_config_id: 
    :type alert_config_id: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_profile_2(request: web.Request, network_id, id) -> web.Response:
    """Show details of a sensor alert profile for a network.

    Show details of a sensor alert profile for a network.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_profiles_2(request: web.Request, network_id) -> web.Response:
    """Lists all sensor alert profiles for a network.

    Lists all sensor alert profiles for a network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sm_profiles_1(request: web.Request, network_id) -> web.Response:
    """List all profiles in a network

    List all profiles in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_alerts_profiles_2(request: web.Request, organization_id) -> web.Response:
    """List all organization-wide alert configurations

    List all organization-wide alert configurations

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profile_port_2(request: web.Request, organization_id, config_template_id, profile_id, port_id) -> web.Response:
    """Return a switch profile port

    Return a switch profile port

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str
    :param port_id: 
    :type port_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profile_ports_2(request: web.Request, organization_id, config_template_id, profile_id) -> web.Response:
    """Return all the ports of a switch profile

    Return all the ports of a switch profile

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profiles_2(request: web.Request, organization_id, config_template_id) -> web.Response:
    """List the switch profiles for your switch template configuration

    List the switch profiles for your switch template configuration

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)


async def update_network_sensor_alerts_profile_2(request: web.Request, network_id, id, body=None) -> web.Response:
    """Updates a sensor alert profile for a network.

    Updates a sensor alert profile for a network.

    :param network_id: 
    :type network_id: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSensorAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_alerts_profile_2(request: web.Request, organization_id, alert_config_id, body=None) -> web.Response:
    """Update an organization-wide alert config

    Update an organization-wide alert config

    :param organization_id: 
    :type organization_id: str
    :param alert_config_id: 
    :type alert_config_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAlertsProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_config_template_switch_profile_port_2(request: web.Request, organization_id, config_template_id, profile_id, port_id, body=None) -> web.Response:
    """Update a switch profile port

    Update a switch profile port

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str
    :param port_id: 
    :type port_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationConfigTemplateSwitchProfilePortRequest.from_dict(body)
    return web.Response(status=200)
