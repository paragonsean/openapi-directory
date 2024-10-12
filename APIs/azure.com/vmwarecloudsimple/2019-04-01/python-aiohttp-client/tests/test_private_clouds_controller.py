# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.private_cloud import PrivateCloud
from openapi_server.models.private_cloud_list import PrivateCloudList


pytestmark = pytest.mark.asyncio

async def test_private_clouds_get(client):
    """Test case for private_clouds_get

    Implements private cloud GET method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}'.format(subscription_id='subscription_id_example', pc_name='pc_name_example', region_id='region_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_clouds_list(client):
    """Test case for private_clouds_list

    Implements private cloud list GET method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds'.format(subscription_id='subscription_id_example', region_id='region_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

