# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.traffic_manager_geographic_hierarchy import TrafficManagerGeographicHierarchy


pytestmark = pytest.mark.asyncio

async def test_geographic_hierarchies_get_default(client):
    """Test case for geographic_hierarchies_get_default

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Network/trafficManagerGeographicHierarchies/default',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

