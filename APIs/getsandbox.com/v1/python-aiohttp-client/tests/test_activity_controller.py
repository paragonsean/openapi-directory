# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_message import ActivityMessage


pytestmark = pytest.mark.asyncio

async def test_get_sandboxes_activity(client):
    """Test case for get_sandboxes_activity

    searchActivity
    """
    params = [('fromTimestamp', 56),
                    ('sourceSandboxes', 'source_sandboxes_example'),
                    ('keyword', 'keyword_example'),
                    ('allTypes', True),
                    ('maxResults', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/1/activity/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

