# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.live_output import LiveOutput
from openapi_server.models.live_output_list_result import LiveOutputListResult


pytestmark = pytest.mark.asyncio

async def test_live_outputs_create(client):
    """Test case for live_outputs_create

    Create Live Output
    """
    parameters = {"properties":{"created":"2000-01-23T04:56:07.000+00:00","manifestName":"manifestName","assetName":"assetName","description":"description","resourceState":"Creating","lastModified":"2000-01-23T04:56:07.000+00:00","outputSnapTime":1,"provisioningState":"provisioningState","archiveWindowLength":"archiveWindowLength","hls":{"fragmentsPerTsSegment":6}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}/liveOutputs/{live_output_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example', live_output_name='live_output_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_outputs_delete(client):
    """Test case for live_outputs_delete

    Delete Live Output
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}/liveOutputs/{live_output_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example', live_output_name='live_output_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_outputs_get(client):
    """Test case for live_outputs_get

    Get Live Output
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}/liveOutputs/{live_output_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example', live_output_name='live_output_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_outputs_list(client):
    """Test case for live_outputs_list

    List Live Outputs
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}/liveOutputs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

