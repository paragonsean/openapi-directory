# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_entity import AppEntity


pytestmark = pytest.mark.asyncio

async def test_get_apps(client):
    """Test case for get_apps

    List Apps
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_prefix', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/apps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

