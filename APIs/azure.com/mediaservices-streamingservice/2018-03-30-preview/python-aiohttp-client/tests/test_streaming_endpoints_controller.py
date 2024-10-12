# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.live_events_list_default_response import LiveEventsListDefaultResponse
from openapi_server.models.streaming_endpoint import StreamingEndpoint
from openapi_server.models.streaming_endpoint_list_result import StreamingEndpointListResult
from openapi_server.models.streaming_entity_scale_unit import StreamingEntityScaleUnit


pytestmark = pytest.mark.asyncio

async def test_streaming_endpoints_create(client):
    """Test case for streaming_endpoints_create

    Create StreamingEndpoint
    """
    parameters = {"properties":{"accessControl":{"ip":{"allow":[{"address":"address","name":"name","subnetPrefixLength":6},{"address":"address","name":"name","subnetPrefixLength":6}]},"akamai":{"akamaiSignatureHeaderAuthenticationKeyList":[{"identifier":"identifier","expiration":"2000-01-23T04:56:07.000+00:00","base64Key":"base64Key"},{"identifier":"identifier","expiration":"2000-01-23T04:56:07.000+00:00","base64Key":"base64Key"}]}},"hostName":"hostName","created":"2000-01-23T04:56:07.000+00:00","scaleUnits":1,"description":"description","maxCacheAge":6,"provisioningState":"provisioningState","customHostNames":["customHostNames","customHostNames"],"cdnProfile":"cdnProfile","cdnProvider":"cdnProvider","resourceState":"Stopped","lastModified":"2000-01-23T04:56:07.000+00:00","availabilitySetName":"availabilitySetName","crossSiteAccessPolicies":{"crossDomainPolicy":"crossDomainPolicy","clientAccessPolicy":"clientAccessPolicy"},"freeTrialEndTime":"2000-01-23T04:56:07.000+00:00","cdnEnabled":True}}
    params = [('api-version', 'api_version_example'),
                    ('autoStart', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/streamingEndpoints/{streaming_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_endpoint_name='streaming_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_endpoints_delete(client):
    """Test case for streaming_endpoints_delete

    Delete StreamingEndpoint
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/streamingEndpoints/{streaming_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_endpoint_name='streaming_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_endpoints_get(client):
    """Test case for streaming_endpoints_get

    Get StreamingEndpoint
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/streamingEndpoints/{streaming_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_endpoint_name='streaming_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_endpoints_list(client):
    """Test case for streaming_endpoints_list

    List StreamingEndpoints
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/streamingEndpoints'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_endpoints_scale(client):
    """Test case for streaming_endpoints_scale

    Scale StreamingEndpoint
    """
    parameters = {"scaleUnit":0}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/streamingEndpoints/{streaming_endpoint_name}/scale'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_endpoint_name='streaming_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_endpoints_start(client):
    """Test case for streaming_endpoints_start

    Start StreamingEndpoint
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/streamingEndpoints/{streaming_endpoint_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_endpoint_name='streaming_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_endpoints_stop(client):
    """Test case for streaming_endpoints_stop

    Stop StreamingEndpoint
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/streamingEndpoints/{streaming_endpoint_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_endpoint_name='streaming_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

