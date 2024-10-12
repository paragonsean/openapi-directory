# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulkexports_v1_export import BulkexportsV1Export


pytestmark = pytest.mark.asyncio

async def test_fetch_export(client):
    """Test case for fetch_export

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Exports/{resource_type}'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

