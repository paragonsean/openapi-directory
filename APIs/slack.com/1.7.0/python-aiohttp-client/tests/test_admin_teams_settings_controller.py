# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_admin_teams_settings_info(client):
    """Test case for admin_teams_settings_info

    
    """
    params = [('team_id', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.teams.settings.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_default_channels(client):
    """Test case for admin_teams_settings_set_default_channels

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'team_id': 'team_id_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setDefaultChannels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_description(client):
    """Test case for admin_teams_settings_set_description

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'description': 'description_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setDescription',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_discoverability(client):
    """Test case for admin_teams_settings_set_discoverability

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'discoverability': 'discoverability_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setDiscoverability',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_icon(client):
    """Test case for admin_teams_settings_set_icon

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'image_url': 'image_url_example',
        'team_id': 'team_id_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setIcon',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_name(client):
    """Test case for admin_teams_settings_set_name

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'name': 'name_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setName',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

