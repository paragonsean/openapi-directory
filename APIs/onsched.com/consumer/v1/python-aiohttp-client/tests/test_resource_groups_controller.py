# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_group_list_view_model import ResourceGroupListViewModel
from openapi_server.models.resource_group_view_model import ResourceGroupViewModel


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_resourcegroups_get(client):
    """Test case for consumer_v1_resourcegroups_get

    List Resource Groups
    """
    params = [('locationId', 'location_id_example'),
                    ('deleted', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/resourcegroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_resourcegroups_id_get(client):
    """Test case for consumer_v1_resourcegroups_id_get

    Get Resource Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/resourcegroups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

