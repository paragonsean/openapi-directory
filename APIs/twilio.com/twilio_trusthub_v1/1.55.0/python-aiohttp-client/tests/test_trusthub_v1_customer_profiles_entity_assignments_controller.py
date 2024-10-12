# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_customer_profile_entity_assignment_response import ListCustomerProfileEntityAssignmentResponse
from openapi_server.models.trusthub_v1_customer_profile_customer_profile_entity_assignment import TrusthubV1CustomerProfileCustomerProfileEntityAssignment


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_customer_profile_entity_assignment(client):
    """Test case for create_customer_profile_entity_assignment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'object_sid': 'object_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments'.format(customer_profile_sid='customer_profile_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_profile_entity_assignment(client):
    """Test case for delete_customer_profile_entity_assignment

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}'.format(customer_profile_sid='customer_profile_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_customer_profile_entity_assignment(client):
    """Test case for fetch_customer_profile_entity_assignment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}'.format(customer_profile_sid='customer_profile_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_customer_profile_entity_assignment(client):
    """Test case for list_customer_profile_entity_assignment

    
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
        path='/v1/CustomerProfiles/{customer_profile_sid}/EntityAssignments'.format(customer_profile_sid='customer_profile_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

