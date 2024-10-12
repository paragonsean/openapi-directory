# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.network_status_contract import NetworkStatusContract
from openapi_server.models.network_status_contract_by_location import NetworkStatusContractByLocation
from openapi_server.models.network_status_list_by_location_default_response import NetworkStatusListByLocationDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_network_status_list_by_location(client):
    """Test case for network_status_list_by_location

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/locations/{location_name}/networkstatus'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example', location_name='location_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_status_list_by_service(client):
    """Test case for network_status_list_by_service

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/networkstatus'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

