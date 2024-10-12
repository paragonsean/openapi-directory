# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.streaming_endpoint import StreamingEndpoint


pytestmark = pytest.mark.asyncio

async def test_streaming_endpoints_update(client):
    """Test case for streaming_endpoints_update

    Update StreamingEndpoint
    """
    parameters = {"properties":{"accessControl":{"ip":{"allow":[{"address":"address","name":"name","subnetPrefixLength":6},{"address":"address","name":"name","subnetPrefixLength":6}]},"akamai":{"akamaiSignatureHeaderAuthenticationKeyList":[{"identifier":"identifier","expiration":"2000-01-23T04:56:07.000+00:00","base64Key":"base64Key"},{"identifier":"identifier","expiration":"2000-01-23T04:56:07.000+00:00","base64Key":"base64Key"}]}},"hostName":"hostName","created":"2000-01-23T04:56:07.000+00:00","scaleUnits":1,"description":"description","maxCacheAge":6,"provisioningState":"provisioningState","customHostNames":["customHostNames","customHostNames"],"cdnProfile":"cdnProfile","cdnProvider":"cdnProvider","resourceState":"Stopped","lastModified":"2000-01-23T04:56:07.000+00:00","availabilitySetName":"availabilitySetName","crossSiteAccessPolicies":{"crossDomainPolicy":"crossDomainPolicy","clientAccessPolicy":"clientAccessPolicy"},"freeTrialEndTime":"2000-01-23T04:56:07.000+00:00","cdnEnabled":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaservices/{account_name}/streamingEndpoints/{streaming_endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_endpoint_name='streaming_endpoint_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

