# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_exports_response import ListExportsResponse
from openapi_server.models.list_video_view_exports_response import ListVideoViewExportsResponse


pytestmark = pytest.mark.asyncio

async def test_list_exports(client):
    """Test case for list_exports

    List property video view export links
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/exports',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_exports_views(client):
    """Test case for list_exports_views

    List available property view exports
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/exports/views',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

