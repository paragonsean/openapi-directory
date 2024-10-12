# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.origin_group import OriginGroup
from openapi_server.models.origin_group_list_result import OriginGroupListResult
from openapi_server.models.origin_group_update_parameters import OriginGroupUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_origin_groups_create(client):
    """Test case for origin_groups_create

    
    """
    origin_group = {"properties":{"resourceState":"Creating","provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/originGroups/{origin_group_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', origin_group_name='origin_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=origin_group,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origin_groups_delete(client):
    """Test case for origin_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/originGroups/{origin_group_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', origin_group_name='origin_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origin_groups_get(client):
    """Test case for origin_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/originGroups/{origin_group_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', origin_group_name='origin_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origin_groups_list_by_endpoint(client):
    """Test case for origin_groups_list_by_endpoint

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/originGroups'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origin_groups_update(client):
    """Test case for origin_groups_update

    
    """
    origin_group_update_properties = {"properties":{"responseBasedOriginErrorDetectionSettings":{"responseBasedFailoverThresholdPercentage":59,"httpErrorRanges":[{"end":231,"begin":641},{"end":231,"begin":641}],"responseBasedDetectedErrorTypes":"None"},"healthProbeSettings":{"probeProtocol":"NotSet","probeIntervalInSeconds":21,"probePath":"probePath","probeRequestType":"NotSet"},"origins":[{"id":"id"},{"id":"id"}],"trafficRestorationTimeToHealedOrNewEndpointsInMinutes":4}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/originGroups/{origin_group_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', origin_group_name='origin_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=origin_group_update_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

