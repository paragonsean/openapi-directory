# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_brand_registrations_response import ListBrandRegistrationsResponse
from openapi_server.models.messaging_v1_brand_registrations import MessagingV1BrandRegistrations


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_brand_registrations(client):
    """Test case for create_brand_registrations

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'a2_p_profile_bundle_sid': 'a2_p_profile_bundle_sid_example',
        'brand_type': 'brand_type_example',
        'customer_profile_bundle_sid': 'customer_profile_bundle_sid_example',
        'mock': True,
        'skip_automatic_sec_vet': True
        }
    response = await client.request(
        method='POST',
        path='/v1/a2p/BrandRegistrations',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_brand_registrations(client):
    """Test case for fetch_brand_registrations

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/a2p/BrandRegistrations/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_brand_registrations(client):
    """Test case for list_brand_registrations

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/a2p/BrandRegistrations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_brand_registrations(client):
    """Test case for update_brand_registrations

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/a2p/BrandRegistrations/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

