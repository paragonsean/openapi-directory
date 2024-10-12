# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_v1_safelist import AccountsV1Safelist


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_safelist(client):
    """Test case for create_safelist

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'phone_number': 'phone_number_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/SafeList/Numbers',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_safelist(client):
    """Test case for delete_safelist

    
    """
    params = [('PhoneNumber', 'phone_number_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/SafeList/Numbers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_safelist(client):
    """Test case for fetch_safelist

    
    """
    params = [('PhoneNumber', 'phone_number_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/SafeList/Numbers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

