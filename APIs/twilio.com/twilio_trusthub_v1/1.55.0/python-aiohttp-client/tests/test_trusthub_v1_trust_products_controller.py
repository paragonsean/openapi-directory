# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_trust_product_response import ListTrustProductResponse
from openapi_server.models.trust_product_enum_status import TrustProductEnumStatus
from openapi_server.models.trusthub_v1_trust_product import TrusthubV1TrustProduct


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_trust_product(client):
    """Test case for create_trust_product

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'email': 'email_example',
        'friendly_name': 'friendly_name_example',
        'policy_sid': 'policy_sid_example',
        'status_callback': 'status_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/TrustProducts',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_trust_product(client):
    """Test case for delete_trust_product

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/TrustProducts/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_trust_product(client):
    """Test case for fetch_trust_product

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/TrustProducts/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_trust_product(client):
    """Test case for list_trust_product

    
    """
    params = [('Status', openapi_server.TrustProductEnumStatus()),
                    ('FriendlyName', 'friendly_name_example'),
                    ('PolicySid', 'policy_sid_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/TrustProducts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_trust_product(client):
    """Test case for update_trust_product

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'email': 'email_example',
        'friendly_name': 'friendly_name_example',
        'status': openapi_server.TrustProductEnumStatus(),
        'status_callback': 'status_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/TrustProducts/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

