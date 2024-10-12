# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.studio_v1_flow_engagement_engagement_context import StudioV1FlowEngagementEngagementContext


pytestmark = pytest.mark.asyncio

async def test_fetch_engagement_context(client):
    """Test case for fetch_engagement_context

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Flows/{flow_sid}/Engagements/{engagement_sid}/Context'.format(flow_sid='flow_sid_example', engagement_sid='engagement_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

