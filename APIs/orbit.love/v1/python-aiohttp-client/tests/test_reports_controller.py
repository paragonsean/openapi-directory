# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_workspace_slug_reports_get(client):
    """Test case for workspace_slug_reports_get

    Get a workspace stats
    """
    params = [('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('relative', 'relative_example'),
                    ('properties', 'properties_example'),
                    ('activity_type', 'activity_type_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/reports'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

