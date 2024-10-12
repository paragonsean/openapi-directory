# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.dedicated_cloud_service import DedicatedCloudService
from openapi_server.models.dedicated_cloud_service_list_response import DedicatedCloudServiceListResponse
from openapi_server.models.patch_payload import PatchPayload


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_services_create_or_update(client):
    """Test case for dedicated_cloud_services_create_or_update

    Implements dedicated cloud service PUT method
    """
    dedicated_cloud_service_request = {"name":"name","location":"location","id":"id","type":"type","properties":{"isAccountOnboarded":"notOnBoarded","nodes":0,"gatewaySubnet":"gatewaySubnet","serviceURL":"serviceURL"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicated_cloud_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dedicated_cloud_service_name='dedicated_cloud_service_name_example'),
        headers=headers,
        json=dedicated_cloud_service_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_services_delete(client):
    """Test case for dedicated_cloud_services_delete

    Implements dedicatedCloudService DELETE method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicated_cloud_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dedicated_cloud_service_name='dedicated_cloud_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_services_get(client):
    """Test case for dedicated_cloud_services_get

    Implements dedicatedCloudService GET method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicated_cloud_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dedicated_cloud_service_name='dedicated_cloud_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_services_list_by_resource_group(client):
    """Test case for dedicated_cloud_services_list_by_resource_group

    Implements list of dedicatedCloudService objects within RG method
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_services_list_by_subscription(client):
    """Test case for dedicated_cloud_services_list_by_subscription

    Implements list of dedicatedCloudService objects within subscription method
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_services_update(client):
    """Test case for dedicated_cloud_services_update

    Implements dedicatedCloudService PATCH method
    """
    dedicated_cloud_service_request = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicated_cloud_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dedicated_cloud_service_name='dedicated_cloud_service_name_example'),
        headers=headers,
        json=dedicated_cloud_service_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

