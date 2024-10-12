# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.spatial_anchors_account_key_regenerate_request import SpatialAnchorsAccountKeyRegenerateRequest
from openapi_server.models.spatial_anchors_account_keys import SpatialAnchorsAccountKeys


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_get_keys(client):
    """Test case for spatial_anchors_accounts_get_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatial_anchors_account_name}/keys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', spatial_anchors_account_name='spatial_anchors_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_regenerate_keys(client):
    """Test case for spatial_anchors_accounts_regenerate_keys

    
    """
    spatial_anchors_account_key_regenerate = {"serial":0}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatial_anchors_account_name}/keys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', spatial_anchors_account_name='spatial_anchors_account_name_example'),
        headers=headers,
        json=spatial_anchors_account_key_regenerate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

