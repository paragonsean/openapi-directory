# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_set_mapping import DataSetMapping
from openapi_server.models.data_set_mapping_list import DataSetMappingList
from openapi_server.models.data_share_error import DataShareError


pytestmark = pytest.mark.asyncio

async def test_data_set_mappings_create(client):
    """Test case for data_set_mappings_create

    Maps a source data set in the source share to a sink data set in the share subscription.  Enables copying the data set from source to destination.
    """
    data_set_mapping = {"kind":"Blob"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/dataSetMappings/{data_set_mapping_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example', data_set_mapping_name='data_set_mapping_name_example'),
        headers=headers,
        json=data_set_mapping,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_set_mappings_delete(client):
    """Test case for data_set_mappings_delete

    Delete DataSetMapping in a shareSubscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/dataSetMappings/{data_set_mapping_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example', data_set_mapping_name='data_set_mapping_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_set_mappings_get(client):
    """Test case for data_set_mappings_get

    Get DataSetMapping in a shareSubscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/dataSetMappings/{data_set_mapping_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example', data_set_mapping_name='data_set_mapping_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_set_mappings_list_by_share_subscription(client):
    """Test case for data_set_mappings_list_by_share_subscription

    List DataSetMappings in a share subscription.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/dataSetMappings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

