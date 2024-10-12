# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.spatial_anchors_account import SpatialAnchorsAccount
from openapi_server.models.spatial_anchors_account_list import SpatialAnchorsAccountList


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_create(client):
    """Test case for spatial_anchors_accounts_create

    
    """
    spatial_anchors_account = {"properties":{"accountId":"accountId","accountDomain":"accountDomain"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatial_anchors_account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', spatial_anchors_account_name='spatial_anchors_account_name_example'),
        headers=headers,
        json=spatial_anchors_account,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_delete(client):
    """Test case for spatial_anchors_accounts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatial_anchors_account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', spatial_anchors_account_name='spatial_anchors_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_get(client):
    """Test case for spatial_anchors_accounts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatial_anchors_account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', spatial_anchors_account_name='spatial_anchors_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_list_by_resource_group(client):
    """Test case for spatial_anchors_accounts_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_list_by_subscription(client):
    """Test case for spatial_anchors_accounts_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MixedReality/spatialAnchorsAccounts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_update(client):
    """Test case for spatial_anchors_accounts_update

    
    """
    spatial_anchors_account = {"properties":{"accountId":"accountId","accountDomain":"accountDomain"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{spatial_anchors_account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', spatial_anchors_account_name='spatial_anchors_account_name_example'),
        headers=headers,
        json=spatial_anchors_account,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

