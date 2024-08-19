# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_issue(client):
    """Test case for get_issue

    Get detailed alert information for an issue
    """
    headers = { 
        'Accept': 'application/sarif+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/issues/{project_id}/{alert_key}'.format(project_id=56, alert_key='+ja0cf6+84AGgat15W1jooeMfUY='),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

