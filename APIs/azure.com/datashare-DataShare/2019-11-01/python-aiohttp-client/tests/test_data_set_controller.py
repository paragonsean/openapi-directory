# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_set import DataSet
from openapi_server.models.data_set_list import DataSetList
from openapi_server.models.data_share_error import DataShareError


pytestmark = pytest.mark.asyncio

async def test_data_sets_create(client):
    """Test case for data_sets_create

    Adds a new data set to an existing share or updates it if existing.
    """
    data_set = {"kind":"Blob"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/dataSets/{data_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', data_set_name='data_set_name_example'),
        headers=headers,
        json=data_set,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_sets_delete(client):
    """Test case for data_sets_delete

    Delete DataSet in a share.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/dataSets/{data_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', data_set_name='data_set_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_sets_get(client):
    """Test case for data_sets_get

    Get DataSet in a share.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/dataSets/{data_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', data_set_name='data_set_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_sets_list_by_share(client):
    """Test case for data_sets_list_by_share

    List DataSets in a share.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/dataSets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

