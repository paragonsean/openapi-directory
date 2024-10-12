# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advanced_threat_protection_setting import AdvancedThreatProtectionSetting
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_advanced_threat_protection_create(client):
    """Test case for advanced_threat_protection_create

    
    """
    advanced_threat_protection_setting = {"properties":{"isEnabled":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{resource_id}/providers/Microsoft.Security/advancedThreatProtectionSettings/{setting_name}'.format(resource_id='resource_id_example', setting_name='setting_name_example'),
        headers=headers,
        json=advanced_threat_protection_setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_advanced_threat_protection_get(client):
    """Test case for advanced_threat_protection_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_id}/providers/Microsoft.Security/advancedThreatProtectionSettings/{setting_name}'.format(resource_id='resource_id_example', setting_name='setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

