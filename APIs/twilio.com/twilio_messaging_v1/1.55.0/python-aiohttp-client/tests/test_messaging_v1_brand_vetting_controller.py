# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.brand_vetting_enum_vetting_provider import BrandVettingEnumVettingProvider
from openapi_server.models.list_brand_vetting_response import ListBrandVettingResponse
from openapi_server.models.messaging_v1_brand_registrations_brand_vetting import MessagingV1BrandRegistrationsBrandVetting


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_brand_vetting(client):
    """Test case for create_brand_vetting

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'vetting_id': 'vetting_id_example',
        'vetting_provider': openapi_server.BrandVettingEnumVettingProvider()
        }
    response = await client.request(
        method='POST',
        path='/v1/a2p/BrandRegistrations/{brand_sid}/Vettings'.format(brand_sid='brand_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_brand_vetting(client):
    """Test case for fetch_brand_vetting

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/a2p/BrandRegistrations/{brand_sid}/Vettings/{brand_vetting_sid}'.format(brand_sid='brand_sid_example', brand_vetting_sid='brand_vetting_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_brand_vetting(client):
    """Test case for list_brand_vetting

    
    """
    params = [('VettingProvider', openapi_server.BrandVettingEnumVettingProvider()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/a2p/BrandRegistrations/{brand_sid}/Vettings'.format(brand_sid='brand_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

