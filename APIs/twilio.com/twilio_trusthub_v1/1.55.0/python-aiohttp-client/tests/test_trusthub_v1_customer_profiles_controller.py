# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_profile_enum_status import CustomerProfileEnumStatus
from openapi_server.models.list_customer_profile_response import ListCustomerProfileResponse
from openapi_server.models.trusthub_v1_customer_profile import TrusthubV1CustomerProfile


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_customer_profile(client):
    """Test case for create_customer_profile

    
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
        path='/v1/CustomerProfiles',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_profile(client):
    """Test case for delete_customer_profile

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/CustomerProfiles/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_customer_profile(client):
    """Test case for fetch_customer_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/CustomerProfiles/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_customer_profile(client):
    """Test case for list_customer_profile

    
    """
    params = [('Status', openapi_server.CustomerProfileEnumStatus()),
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
        path='/v1/CustomerProfiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_customer_profile(client):
    """Test case for update_customer_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'email': 'email_example',
        'friendly_name': 'friendly_name_example',
        'status': openapi_server.CustomerProfileEnumStatus(),
        'status_callback': 'status_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/CustomerProfiles/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

