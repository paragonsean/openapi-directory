# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_list_view_model import ResourceListViewModel
from openapi_server.models.resource_service_list_view_model import ResourceServiceListViewModel
from openapi_server.models.resource_view_model import ResourceViewModel


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_resources_get(client):
    """Test case for consumer_v1_resources_get

    List Resources
    """
    params = [('locationId', 'location_id_example'),
                    ('resourceGroupId', 56),
                    ('email', 'email_example'),
                    ('name', 'name_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/resources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_resources_id_get(client):
    """Test case for consumer_v1_resources_id_get

    Get Resource
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/resources/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_resources_id_services_get(client):
    """Test case for consumer_v1_resources_id_services_get

    Get Resource Linked Services
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/resources/{id}/services'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

