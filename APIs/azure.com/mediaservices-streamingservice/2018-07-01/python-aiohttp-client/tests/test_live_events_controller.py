# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.live_event import LiveEvent
from openapi_server.models.live_event_action_input import LiveEventActionInput
from openapi_server.models.live_event_list_result import LiveEventListResult


pytestmark = pytest.mark.asyncio

async def test_live_events_create(client):
    """Test case for live_events_create

    Create Live Event
    """
    parameters = {"properties":{"preview":{"accessControl":{"ip":{"allow":[{"address":"address","name":"name","subnetPrefixLength":6},{"address":"address","name":"name","subnetPrefixLength":6}]}},"endpoints":[{"protocol":"protocol","url":"url"},{"protocol":"protocol","url":"url"}],"alternativeMediaId":"alternativeMediaId","streamingPolicyName":"streamingPolicyName","previewLocator":"previewLocator"},"input":{"accessControl":{"ip":{"allow":[{"address":"address","name":"name","subnetPrefixLength":6},{"address":"address","name":"name","subnetPrefixLength":6}]}},"endpoints":[{"protocol":"protocol","url":"url"},{"protocol":"protocol","url":"url"}],"streamingProtocol":"FragmentedMP4","accessToken":"accessToken","keyFrameIntervalDuration":"keyFrameIntervalDuration"},"created":"2000-01-23T04:56:07.000+00:00","vanityUrl":True,"streamOptions":["Default","Default"],"description":"description","resourceState":"Stopped","lastModified":"2000-01-23T04:56:07.000+00:00","provisioningState":"provisioningState","encoding":{"presetName":"presetName","encodingType":"None"},"crossSiteAccessPolicies":{"crossDomainPolicy":"crossDomainPolicy","clientAccessPolicy":"clientAccessPolicy"}}}
    params = [('api-version', 'api_version_example'),
                    ('autoStart', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_events_delete(client):
    """Test case for live_events_delete

    Delete Live Event
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_events_get(client):
    """Test case for live_events_get

    Get Live Event
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_events_list(client):
    """Test case for live_events_list

    List Live Events
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_events_reset(client):
    """Test case for live_events_reset

    Reset Live Event
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}/reset'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_events_start(client):
    """Test case for live_events_start

    Start Live Event
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_events_stop(client):
    """Test case for live_events_stop

    Stop Live Event
    """
    parameters = {"removeOutputsOnStop":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_events_update(client):
    """Test case for live_events_update

    
    """
    parameters = {"properties":{"preview":{"accessControl":{"ip":{"allow":[{"address":"address","name":"name","subnetPrefixLength":6},{"address":"address","name":"name","subnetPrefixLength":6}]}},"endpoints":[{"protocol":"protocol","url":"url"},{"protocol":"protocol","url":"url"}],"alternativeMediaId":"alternativeMediaId","streamingPolicyName":"streamingPolicyName","previewLocator":"previewLocator"},"input":{"accessControl":{"ip":{"allow":[{"address":"address","name":"name","subnetPrefixLength":6},{"address":"address","name":"name","subnetPrefixLength":6}]}},"endpoints":[{"protocol":"protocol","url":"url"},{"protocol":"protocol","url":"url"}],"streamingProtocol":"FragmentedMP4","accessToken":"accessToken","keyFrameIntervalDuration":"keyFrameIntervalDuration"},"created":"2000-01-23T04:56:07.000+00:00","vanityUrl":True,"streamOptions":["Default","Default"],"description":"description","resourceState":"Stopped","lastModified":"2000-01-23T04:56:07.000+00:00","provisioningState":"provisioningState","encoding":{"presetName":"presetName","encodingType":"None"},"crossSiteAccessPolicies":{"crossDomainPolicy":"crossDomainPolicy","clientAccessPolicy":"clientAccessPolicy"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/liveEvents/{live_event_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', live_event_name='live_event_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

