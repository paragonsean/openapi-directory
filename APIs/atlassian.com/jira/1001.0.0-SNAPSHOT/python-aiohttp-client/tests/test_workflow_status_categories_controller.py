# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.status_category import StatusCategory


pytestmark = pytest.mark.asyncio

async def test_get_status_categories(client):
    """Test case for get_status_categories

    Get all status categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/statuscategory',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status_category(client):
    """Test case for get_status_category

    Get status category
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/statuscategory/{id_or_key}'.format(id_or_key='id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

