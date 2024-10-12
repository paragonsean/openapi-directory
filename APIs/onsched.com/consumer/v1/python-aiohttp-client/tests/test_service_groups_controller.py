# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_group_list_view_model import ServiceGroupListViewModel
from openapi_server.models.service_group_view_model import ServiceGroupViewModel


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_servicegroups_get(client):
    """Test case for consumer_v1_servicegroups_get

    List Service Groups
    """
    params = [('locationId', 'location_id_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/servicegroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_servicegroups_id_get(client):
    """Test case for consumer_v1_servicegroups_id_get

    Get Service Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/servicegroups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

