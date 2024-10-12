# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_customer_profile_channel_endpoint_assignment_response import ListCustomerProfileChannelEndpointAssignmentResponse
from openapi_server.models.trusthub_v1_customer_profile_customer_profile_channel_endpoint_assignment import TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_customer_profile_channel_endpoint_assignment(client):
    """Test case for create_customer_profile_channel_endpoint_assignment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'channel_endpoint_sid': 'channel_endpoint_sid_example',
        'channel_endpoint_type': 'channel_endpoint_type_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments'.format(customer_profile_sid='customer_profile_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_profile_channel_endpoint_assignment(client):
    """Test case for delete_customer_profile_channel_endpoint_assignment

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}'.format(customer_profile_sid='customer_profile_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_customer_profile_channel_endpoint_assignment(client):
    """Test case for fetch_customer_profile_channel_endpoint_assignment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}'.format(customer_profile_sid='customer_profile_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_customer_profile_channel_endpoint_assignment(client):
    """Test case for list_customer_profile_channel_endpoint_assignment

    
    """
    params = [('ChannelEndpointSid', 'channel_endpoint_sid_example'),
                    ('ChannelEndpointSids', 'channel_endpoint_sids_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments'.format(customer_profile_sid='customer_profile_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

