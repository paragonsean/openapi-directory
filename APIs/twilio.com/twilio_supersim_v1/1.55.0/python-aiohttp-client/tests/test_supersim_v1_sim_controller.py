# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sim_response import ListSimResponse
from openapi_server.models.sim_enum_status import SimEnumStatus
from openapi_server.models.sim_enum_status_update import SimEnumStatusUpdate
from openapi_server.models.supersim_v1_sim import SupersimV1Sim


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sim(client):
    """Test case for create_sim

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'iccid': 'iccid_example',
        'registration_code': 'registration_code_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Sims',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sim(client):
    """Test case for fetch_sim

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Sims/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sim(client):
    """Test case for list_sim

    
    """
    params = [('Status', openapi_server.SimEnumStatus()),
                    ('Fleet', 'fleet_example'),
                    ('Iccid', 'iccid_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Sims',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sim(client):
    """Test case for update_sim

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'account_sid': 'account_sid_example',
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'fleet': 'fleet_example',
        'status': openapi_server.SimEnumStatusUpdate(),
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Sims/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

