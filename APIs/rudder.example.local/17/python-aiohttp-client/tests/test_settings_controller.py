# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_all_settings200_response import GetAllSettings200Response
from openapi_server.models.get_allowed_networks200_response import GetAllowedNetworks200Response
from openapi_server.models.get_setting200_response import GetSetting200Response
from openapi_server.models.modify_allowed_networks200_response import ModifyAllowedNetworks200Response
from openapi_server.models.modify_allowed_networks_request import ModifyAllowedNetworksRequest
from openapi_server.models.modify_setting200_response import ModifySetting200Response
from openapi_server.models.modify_setting_request import ModifySettingRequest
from openapi_server.models.set_allowed_networks200_response import SetAllowedNetworks200Response
from openapi_server.models.set_allowed_networks_request import SetAllowedNetworksRequest


pytestmark = pytest.mark.asyncio

async def test_get_all_settings(client):
    """Test case for get_all_settings

    List all settings
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_allowed_networks(client):
    """Test case for get_allowed_networks

    Get allowed networks for a policy server
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/settings/allowed_networks/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_setting(client):
    """Test case for get_setting

    Get the value of a setting
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/settings/{setting_id}'.format(setting_id='global_policy_mode'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modify_allowed_networks(client):
    """Test case for modify_allowed_networks

    Modify allowed networks for a policy server
    """
    body = openapi_server.ModifyAllowedNetworksRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/settings/allowed_networks/{node_id}/diff'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modify_setting(client):
    """Test case for modify_setting

    Set the value of a setting
    """
    body = openapi_server.ModifySettingRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/settings/{setting_id}'.format(setting_id='global_policy_mode'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_allowed_networks(client):
    """Test case for set_allowed_networks

    Set allowed networks for a policy server
    """
    body = openapi_server.SetAllowedNetworksRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/settings/allowed_networks/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

