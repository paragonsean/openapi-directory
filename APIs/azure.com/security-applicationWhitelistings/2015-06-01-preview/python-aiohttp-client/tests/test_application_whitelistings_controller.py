# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.adaptive_application_controls_list_default_response import AdaptiveApplicationControlsListDefaultResponse
from openapi_server.models.app_whitelisting_group import AppWhitelistingGroup
from openapi_server.models.app_whitelisting_groups import AppWhitelistingGroups
from openapi_server.models.app_whitelisting_put_group_data import AppWhitelistingPutGroupData


pytestmark = pytest.mark.asyncio

async def test_adaptive_application_controls_get(client):
    """Test case for adaptive_application_controls_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations/{asc_location}/applicationWhitelistings/{group_name}'.format(subscription_id='subscription_id_example', asc_location='asc_location_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adaptive_application_controls_list(client):
    """Test case for adaptive_application_controls_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('includePathRecommendations', True),
                    ('summary', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/applicationWhitelistings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adaptive_application_controls_put(client):
    """Test case for adaptive_application_controls_put

    
    """
    body = {"protectionMode":{},"vmRecommendations":[{"resourceId":"/subscriptions/12345678-1234-1234-1234-123456789123/resourcegroups/group/providers/microsoft.compute/virtualmachines/vm"},{"resourceId":"/subscriptions/12345678-1234-1234-1234-123456789123/resourcegroups/group/providers/microsoft.compute/virtualmachines/vm"}],"pathRecommendations":[{"path":"C:\\Windows\\System32\\calc.exe","common":True,"publisherInfo":{"publisherName":"O=GOOGLE INC, L=MOUNTAIN VIEW, S=CALIFORNIA, C=US","version":"66.0.3359.139","productName":"GOOGLE CHROME","binaryName":"CHROME.EXE"},"action":"Recommended","usernames":[{"username":"LOCAL SYSTEM"},{"username":"LOCAL SYSTEM"}],"type":"File","userSids":["S-1-5-18","S-1-5-18"],"fileType":"Exe"},{"path":"C:\\Windows\\System32\\calc.exe","common":True,"publisherInfo":{"publisherName":"O=GOOGLE INC, L=MOUNTAIN VIEW, S=CALIFORNIA, C=US","version":"66.0.3359.139","productName":"GOOGLE CHROME","binaryName":"CHROME.EXE"},"action":"Recommended","usernames":[{"username":"LOCAL SYSTEM"},{"username":"LOCAL SYSTEM"}],"type":"File","userSids":["S-1-5-18","S-1-5-18"],"fileType":"Exe"}],"enforcementMode":"Audit"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations/{asc_location}/applicationWhitelistings/{group_name}'.format(subscription_id='subscription_id_example', asc_location='asc_location_example', group_name='group_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

