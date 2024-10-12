# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bandwidth_setting import BandwidthSetting
from openapi_server.models.bandwidth_setting_list import BandwidthSettingList


pytestmark = pytest.mark.asyncio

async def test_bandwidth_settings_create_or_update(client):
    """Test case for bandwidth_settings_create_or_update

    
    """
    parameters = {"properties":{"schedules":[{"stop":{"hours":13,"seconds":35,"minutes":8},"start":{"hours":13,"seconds":35,"minutes":8},"days":["Sunday","Sunday"],"rateInMbps":0},{"stop":{"hours":13,"seconds":35,"minutes":8},"start":{"hours":13,"seconds":35,"minutes":8},"days":["Sunday","Sunday"],"rateInMbps":0}],"volumeCount":5}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/bandwidthSettings/{bandwidth_setting_name}'.format(bandwidth_setting_name='bandwidth_setting_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bandwidth_settings_delete(client):
    """Test case for bandwidth_settings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/bandwidthSettings/{bandwidth_setting_name}'.format(bandwidth_setting_name='bandwidth_setting_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bandwidth_settings_get(client):
    """Test case for bandwidth_settings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/bandwidthSettings/{bandwidth_setting_name}'.format(bandwidth_setting_name='bandwidth_setting_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bandwidth_settings_list_by_manager(client):
    """Test case for bandwidth_settings_list_by_manager

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/bandwidthSettings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

