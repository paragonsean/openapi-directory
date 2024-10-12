from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_config_template_request import CreateOrganizationConfigTemplateRequest
from openapi_server.models.get_organization_config_template_switch_profile_ports200_response_inner import GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner
from openapi_server.models.get_organization_config_template_switch_profiles200_response import GetOrganizationConfigTemplateSwitchProfiles200Response
from openapi_server.models.update_organization_config_template_request import UpdateOrganizationConfigTemplateRequest
from openapi_server.models.update_organization_config_template_switch_profile_port_request import UpdateOrganizationConfigTemplateSwitchProfilePortRequest
from openapi_server import util


async def create_organization_config_template_1(request: web.Request, organization_id, body) -> web.Response:
    """Create a new configuration template

    Create a new configuration template

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationConfigTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_config_template_1(request: web.Request, organization_id, config_template_id) -> web.Response:
    """Remove a configuration template

    Remove a configuration template

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_1(request: web.Request, organization_id, config_template_id) -> web.Response:
    """Return a single configuration template

    Return a single configuration template

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profile_port_1(request: web.Request, organization_id, config_template_id, profile_id, port_id) -> web.Response:
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


async def get_organization_config_template_switch_profile_ports_1(request: web.Request, organization_id, config_template_id, profile_id) -> web.Response:
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


async def get_organization_config_template_switch_profiles_1(request: web.Request, organization_id, config_template_id) -> web.Response:
    """List the switch profiles for your switch template configuration

    List the switch profiles for your switch template configuration

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)


async def get_organization_config_templates_1(request: web.Request, organization_id) -> web.Response:
    """List the configuration templates for this organization

    List the configuration templates for this organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_config_template_1(request: web.Request, organization_id, config_template_id, body=None) -> web.Response:
    """Update a configuration template

    Update a configuration template

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationConfigTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_config_template_switch_profile_port_1(request: web.Request, organization_id, config_template_id, profile_id, port_id, body=None) -> web.Response:
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
