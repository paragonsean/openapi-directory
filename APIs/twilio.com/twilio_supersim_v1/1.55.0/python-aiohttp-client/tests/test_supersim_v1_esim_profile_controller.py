# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.esim_profile_enum_status import EsimProfileEnumStatus
from openapi_server.models.list_esim_profile_response import ListEsimProfileResponse
from openapi_server.models.supersim_v1_esim_profile import SupersimV1EsimProfile


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_esim_profile(client):
    """Test case for create_esim_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'eid': 'eid_example',
        'generate_matching_id': True
        }
    response = await client.request(
        method='POST',
        path='/v1/ESimProfiles',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_esim_profile(client):
    """Test case for fetch_esim_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/ESimProfiles/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_esim_profile(client):
    """Test case for list_esim_profile

    
    """
    params = [('Eid', 'eid_example'),
                    ('SimSid', 'sim_sid_example'),
                    ('Status', openapi_server.EsimProfileEnumStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/ESimProfiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

