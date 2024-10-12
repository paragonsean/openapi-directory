# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_response import OperationResponse
from openapi_server.models.synchronization_setting import SynchronizationSetting
from openapi_server.models.synchronization_setting_list import SynchronizationSettingList


pytestmark = pytest.mark.asyncio

async def test_synchronization_settings_create(client):
    """Test case for synchronization_settings_create

    Adds a new synchronization setting to an existing share or updates it if existing.
    """
    synchronization_setting = {"kind":"ScheduleBased"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/synchronizationSettings/{synchronization_setting_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', synchronization_setting_name='synchronization_setting_name_example'),
        headers=headers,
        json=synchronization_setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_synchronization_settings_delete(client):
    """Test case for synchronization_settings_delete

    Delete synchronizationSetting in a share.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/synchronizationSettings/{synchronization_setting_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', synchronization_setting_name='synchronization_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_synchronization_settings_get(client):
    """Test case for synchronization_settings_get

    Get synchronizationSetting in a share.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/synchronizationSettings/{synchronization_setting_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', synchronization_setting_name='synchronization_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_synchronization_settings_list_by_share(client):
    """Test case for synchronization_settings_list_by_share

    List synchronizationSettings in a share.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shares/{share_name}/synchronizationSettings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

