# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_tags_list_result import ServiceTagsListResult


pytestmark = pytest.mark.asyncio

async def test_service_tags_list(client):
    """Test case for service_tags_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/locations/{location}/serviceTags'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

