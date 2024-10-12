# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_insights_settings_comment import FlexV1InsightsSettingsComment


pytestmark = pytest.mark.asyncio

async def test_fetch_insights_settings_comment(client):
    """Test case for fetch_insights_settings_comment

    
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Insights/QualityManagement/Settings/CommentTags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

