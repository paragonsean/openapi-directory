# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profiles(client):
    """Test case for get_organization_config_template_switch_profiles

    List the switch profiles for your switch template configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/configTemplates/{config_template_id}/switchProfiles'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

