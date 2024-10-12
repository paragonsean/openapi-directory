# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.delete_operation_result import DeleteOperationResult
from openapi_server.models.endpoint import Endpoint


pytestmark = pytest.mark.asyncio

async def test_endpoints_create_or_update(client):
    """Test case for endpoints_create_or_update

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"targetResourceId":"targetResourceId","endpointLocation":"endpointLocation","endpointStatus":"endpointStatus","minChildEndpoints":6,"weight":5,"priority":1,"geoMapping":["geoMapping","geoMapping"],"endpointMonitorStatus":"endpointMonitorStatus","target":"target"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}/{endpoint_type}/{endpoint_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_type='endpoint_type_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_delete(client):
    """Test case for endpoints_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}/{endpoint_type}/{endpoint_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_type='endpoint_type_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_get(client):
    """Test case for endpoints_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}/{endpoint_type}/{endpoint_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_type='endpoint_type_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoints_update(client):
    """Test case for endpoints_update

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"targetResourceId":"targetResourceId","endpointLocation":"endpointLocation","endpointStatus":"endpointStatus","minChildEndpoints":6,"weight":5,"priority":1,"geoMapping":["geoMapping","geoMapping"],"endpointMonitorStatus":"endpointMonitorStatus","target":"target"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}/{endpoint_type}/{endpoint_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_type='endpoint_type_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

