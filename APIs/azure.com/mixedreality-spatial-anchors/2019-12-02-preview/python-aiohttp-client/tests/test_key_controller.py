# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.spatial_anchors_accounts_get_keys200_response import SpatialAnchorsAccountsGetKeys200Response
from openapi_server.models.spatial_anchors_accounts_list_by_subscription_default_response import SpatialAnchorsAccountsListBySubscriptionDefaultResponse
from openapi_server.models.spatial_anchors_accounts_regenerate_keys_request import SpatialAnchorsAccountsRegenerateKeysRequest


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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{account_name}/keys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_regenerate_keys(client):
    """Test case for spatial_anchors_accounts_regenerate_keys

    
    """
    regenerate = openapi_server.SpatialAnchorsAccountsRegenerateKeysRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{account_name}/keys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        json=regenerate,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

