# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.enterprise_channel import EnterpriseChannel
from openapi_server.models.enterprise_channel_check_name_availability_request import EnterpriseChannelCheckNameAvailabilityRequest
from openapi_server.models.enterprise_channel_check_name_availability_response import EnterpriseChannelCheckNameAvailabilityResponse
from openapi_server.models.enterprise_channel_response_list import EnterpriseChannelResponseList
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_enterprise_channels_check_name_availability(client):
    """Test case for enterprise_channels_check_name_availability

    
    """
    parameters = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.BotService/checkEnterpriseChannelNameAvailability',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_channels_create(client):
    """Test case for enterprise_channels_create

    
    """
    parameters = {"properties":{"nodes":[{"azureLocation":"azureLocation","azureSku":"azureSku","name":"name","id":"id","state":"Creating"},{"azureLocation":"azureLocation","azureSku":"azureSku","name":"name","id":"id","state":"Creating"}],"state":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/enterpriseChannels/{resource_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_channels_delete(client):
    """Test case for enterprise_channels_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/enterpriseChannels/{resource_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_channels_get(client):
    """Test case for enterprise_channels_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/enterpriseChannels/{resource_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_channels_list_by_resource_group(client):
    """Test case for enterprise_channels_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/enterpriseChannels'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_channels_update(client):
    """Test case for enterprise_channels_update

    
    """
    parameters = {"properties":{"nodes":[{"azureLocation":"azureLocation","azureSku":"azureSku","name":"name","id":"id","state":"Creating"},{"azureLocation":"azureLocation","azureSku":"azureSku","name":"name","id":"id","state":"Creating"}],"state":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/enterpriseChannels/{resource_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

