# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auto_provisioning_setting import AutoProvisioningSetting
from openapi_server.models.auto_provisioning_setting_list import AutoProvisioningSettingList
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_auto_provisioning_settings_create(client):
    """Test case for auto_provisioning_settings_create

    
    """
    setting = {"properties":{"autoProvision":"On"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/autoProvisioningSettings/{setting_name}'.format(subscription_id='subscription_id_example', setting_name='setting_name_example'),
        headers=headers,
        json=setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_provisioning_settings_get(client):
    """Test case for auto_provisioning_settings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/autoProvisioningSettings/{setting_name}'.format(subscription_id='subscription_id_example', setting_name='setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_provisioning_settings_list(client):
    """Test case for auto_provisioning_settings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/autoProvisioningSettings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

