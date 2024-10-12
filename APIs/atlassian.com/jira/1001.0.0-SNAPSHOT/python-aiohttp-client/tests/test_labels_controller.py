# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_bean_string import PageBeanString


pytestmark = pytest.mark.asyncio

async def test_get_all_labels(client):
    """Test case for get_all_labels

    Get all labels
    """
    params = [('startAt', 0),
                    ('maxResults', 1000)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/label',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

