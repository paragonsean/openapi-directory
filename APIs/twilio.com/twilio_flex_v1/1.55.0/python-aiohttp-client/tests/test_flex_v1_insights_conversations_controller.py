# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_insights_conversations_response import ListInsightsConversationsResponse


pytestmark = pytest.mark.asyncio

async def test_list_insights_conversations(client):
    """Test case for list_insights_conversations

    
    """
    params = [('SegmentId', 'segment_id_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Insights/Conversations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

