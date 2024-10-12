# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.studio_v2_flow_test_user import StudioV2FlowTestUser


pytestmark = pytest.mark.asyncio

async def test_fetch_test_user(client):
    """Test case for fetch_test_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Flows/{sid}/TestUsers'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_test_user(client):
    """Test case for update_test_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'test_users': ['test_users_example']
        }
    response = await client.request(
        method='POST',
        path='/v2/Flows/{sid}/TestUsers'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

