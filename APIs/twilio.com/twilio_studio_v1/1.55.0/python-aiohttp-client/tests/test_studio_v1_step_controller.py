# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_step_response import ListStepResponse
from openapi_server.models.studio_v1_flow_engagement_step import StudioV1FlowEngagementStep


pytestmark = pytest.mark.asyncio

async def test_fetch_step(client):
    """Test case for fetch_step

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{sid}'.format(flow_sid='flow_sid_example', engagement_sid='engagement_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_step(client):
    """Test case for list_step

    
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
        path='/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps'.format(flow_sid='flow_sid_example', engagement_sid='engagement_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

