# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_workspace_slug_activity_types_get(client):
    """Test case for workspace_slug_activity_types_get

    List all activity types for a workspace
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/activity_types'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

