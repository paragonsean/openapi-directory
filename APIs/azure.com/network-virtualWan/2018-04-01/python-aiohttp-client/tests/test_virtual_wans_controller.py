# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_hub import VirtualHub
from openapi_server.models.virtual_hubs_list_default_response import VirtualHubsListDefaultResponse
from openapi_server.models.virtual_hubs_update_tags_request import VirtualHubsUpdateTagsRequest
from openapi_server.models.virtual_wan import VirtualWAN


pytestmark = pytest.mark.asyncio

async def test_virtual_hubs_update_tags(client):
    """Test case for virtual_hubs_update_tags

    
    """
    virtual_hub_parameters = openapi_server.VirtualHubsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualHubs/{virtual_hub_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_hub_name='virtual_hub_name_example'),
        headers=headers,
        json=virtual_hub_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_wans_update_tags(client):
    """Test case for virtual_wans_update_tags

    
    """
    wan_parameters = openapi_server.VirtualHubsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example'),
        headers=headers,
        json=wan_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

