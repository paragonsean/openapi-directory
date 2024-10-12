# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_engagement_response import ListEngagementResponse
from openapi_server.models.studio_v1_flow_engagement import StudioV1FlowEngagement


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_engagement(client):
    """Test case for create_engagement

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        '_from': '_from_example',
        'parameters': None,
        'to': 'to_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Flows/{flow_sid}/Engagements'.format(flow_sid='flow_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_engagement(client):
    """Test case for delete_engagement

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Flows/{flow_sid}/Engagements/{sid}'.format(flow_sid='flow_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_engagement(client):
    """Test case for fetch_engagement

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Flows/{flow_sid}/Engagements/{sid}'.format(flow_sid='flow_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_engagement(client):
    """Test case for list_engagement

    
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
        path='/v1/Flows/{flow_sid}/Engagements'.format(flow_sid='flow_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

