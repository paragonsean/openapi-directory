# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bot import Bot
from openapi_server.models.bot_response_list import BotResponseList
from openapi_server.models.check_name_availability_request_body import CheckNameAvailabilityRequestBody
from openapi_server.models.check_name_availability_response_body import CheckNameAvailabilityResponseBody
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_bots_create(client):
    """Test case for bots_create

    
    """
    parameters = {"properties":{"enabledChannels":["enabledChannels","enabledChannels"],"displayName":"displayName","endpointVersion":"endpointVersion","description":"description","luisKey":"luisKey","developerAppInsightsApplicationId":"developerAppInsightsApplicationId","endpoint":"endpoint","developerAppInsightKey":"developerAppInsightKey","developerAppInsightsApiKey":"developerAppInsightsApiKey","configuredChannels":["configuredChannels","configuredChannels"],"luisAppIds":["luisAppIds","luisAppIds"],"msaAppId":"msaAppId","iconUrl":"iconUrl"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bots_delete(client):
    """Test case for bots_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bots_get(client):
    """Test case for bots_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bots_get_check_name_availability(client):
    """Test case for bots_get_check_name_availability

    
    """
    parameters = {"name":"name","type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.BotService/botServices/checkNameAvailability',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bots_list(client):
    """Test case for bots_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.BotService/botServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bots_list_by_resource_group(client):
    """Test case for bots_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bots_update(client):
    """Test case for bots_update

    
    """
    parameters = {"properties":{"enabledChannels":["enabledChannels","enabledChannels"],"displayName":"displayName","endpointVersion":"endpointVersion","description":"description","luisKey":"luisKey","developerAppInsightsApplicationId":"developerAppInsightsApplicationId","endpoint":"endpoint","developerAppInsightKey":"developerAppInsightKey","developerAppInsightsApiKey":"developerAppInsightsApiKey","configuredChannels":["configuredChannels","configuredChannels"],"luisAppIds":["luisAppIds","luisAppIds"],"msaAppId":"msaAppId","iconUrl":"iconUrl"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

