# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_overview import AdminOverview
from openapi_server.models.locations_list import LocationsList
from openapi_server.models.operation_list import OperationList
from openapi_server.models.operation_result_list import OperationResultList


pytestmark = pytest.mark.asyncio

async def test_locations_operation_results_list(client):
    """Test case for locations_operation_results_list

    
    """
    params = [('api-version', '2015-06-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Network.Admin/locations/{location}/operationResults'.format(location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_operations_list(client):
    """Test case for locations_operations_list

    
    """
    params = [('api-version', '2015-06-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Network.Admin/locations/{location}/operations'.format(location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_on_prem_locations_list(client):
    """Test case for on_prem_locations_list

    
    """
    params = [('api-version', '2015-06-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Network.Admin/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', '2015-06-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Network.Admin/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_provider_state_get(client):
    """Test case for resource_provider_state_get

    
    """
    params = [('api-version', '2015-06-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network.Admin/adminOverview'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

