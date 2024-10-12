# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_wireless_sim_response import ListWirelessSimResponse
from openapi_server.models.preview_wireless_sim import PreviewWirelessSim


pytestmark = pytest.mark.asyncio

async def test_fetch_wireless_sim(client):
    """Test case for fetch_wireless_sim

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/wireless/Sims/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_wireless_sim(client):
    """Test case for list_wireless_sim

    
    """
    params = [('Status', 'status_example'),
                    ('Iccid', 'iccid_example'),
                    ('RatePlan', 'rate_plan_example'),
                    ('EId', 'eid_example'),
                    ('SimRegistrationCode', 'sim_registration_code_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/wireless/Sims',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_wireless_sim(client):
    """Test case for update_wireless_sim

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'commands_callback_method': 'commands_callback_method_example',
        'commands_callback_url': 'commands_callback_url_example',
        'friendly_name': 'friendly_name_example',
        'rate_plan': 'rate_plan_example',
        'sms_fallback_method': 'sms_fallback_method_example',
        'sms_fallback_url': 'sms_fallback_url_example',
        'sms_method': 'sms_method_example',
        'sms_url': 'sms_url_example',
        'status': 'status_example',
        'unique_name': 'unique_name_example',
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/wireless/Sims/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

