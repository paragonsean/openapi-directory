# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_list_view_model import ResourceListViewModel
from openapi_server.models.service_allocation_list_view_model import ServiceAllocationListViewModel
from openapi_server.models.service_allocation_view_model import ServiceAllocationViewModel
from openapi_server.models.service_list_view_model import ServiceListViewModel
from openapi_server.models.service_sort_order import ServiceSortOrder
from openapi_server.models.service_view_model import ServiceViewModel
from openapi_server.models.services_scope import ServicesScope


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_services_allocations_id_get(client):
    """Test case for consumer_v1_services_allocations_id_get

    Get Service Allocation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/services/allocations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_services_get(client):
    """Test case for consumer_v1_services_get

    List Services
    """
    params = [('locationId', 'location_id_example'),
                    ('serviceGroupId', 56),
                    ('defaultService', True),
                    ('allLocations', True),
                    ('scope', openapi_server.ServicesScope()),
                    ('name', 'name_example'),
                    ('serviceId', 'service_id_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('sortOrder', openapi_server.ServiceSortOrder()),
                    ('sortDescending', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_services_id_allocations_get(client):
    """Test case for consumer_v1_services_id_allocations_get

    List Service Allocations
    """
    params = [('locationId', 'location_id_example'),
                    ('resourceId', 'resource_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/services/{id}/allocations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_services_id_get(client):
    """Test case for consumer_v1_services_id_get

    Get Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/services/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_services_id_resources_get(client):
    """Test case for consumer_v1_services_id_resources_get

    List Resources for Service
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
        path='/consumer/v1/services/{id}/resources'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

