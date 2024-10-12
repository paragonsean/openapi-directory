# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_config_template_request import CreateOrganizationConfigTemplateRequest
from openapi_server.models.get_organization_config_template_switch_profile_ports200_response_inner import GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner
from openapi_server.models.get_organization_config_template_switch_profiles200_response import GetOrganizationConfigTemplateSwitchProfiles200Response
from openapi_server.models.update_organization_config_template_request import UpdateOrganizationConfigTemplateRequest
from openapi_server.models.update_organization_config_template_switch_profile_port_request import UpdateOrganizationConfigTemplateSwitchProfilePortRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_config_template_1(client):
    """Test case for create_organization_config_template_1

    Create a new configuration template
    """
    body = openapi_server.CreateOrganizationConfigTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/configTemplates'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_config_template_1(client):
    """Test case for delete_organization_config_template_1

    Remove a configuration template
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_1(client):
    """Test case for get_organization_config_template_1

    Return a single configuration template
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profile_port_1(client):
    """Test case for get_organization_config_template_switch_profile_port_1

    Return a switch profile port
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example', port_id='port_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profile_ports_1(client):
    """Test case for get_organization_config_template_switch_profile_ports_1

    Return all the ports of a switch profile
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profiles_1(client):
    """Test case for get_organization_config_template_switch_profiles_1

    List the switch profiles for your switch template configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_templates_1(client):
    """Test case for get_organization_config_templates_1

    List the configuration templates for this organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_config_template_1(client):
    """Test case for update_organization_config_template_1

    Update a configuration template
    """
    body = openapi_server.UpdateOrganizationConfigTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_config_template_switch_profile_port_1(client):
    """Test case for update_organization_config_template_switch_profile_port_1

    Update a switch profile port
    """
    body = openapi_server.UpdateOrganizationConfigTemplateSwitchProfilePortRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example', port_id='port_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

