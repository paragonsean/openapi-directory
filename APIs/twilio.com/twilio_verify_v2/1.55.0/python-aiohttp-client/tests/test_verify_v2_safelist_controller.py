# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verify_v2_safelist import VerifyV2Safelist


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
        path='/v2/SafeList/Numbers',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_safelist(client):
    """Test case for delete_safelist

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/SafeList/Numbers/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_safelist(client):
    """Test case for fetch_safelist

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/SafeList/Numbers/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

