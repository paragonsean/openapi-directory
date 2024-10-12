# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_tier_config import DeviceTierConfig
from openapi_server.models.list_device_tier_configs_response import ListDeviceTierConfigsResponse
from openapi_server.models.safety_labels_update_request import SafetyLabelsUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_applications_data_safety(client):
    """Test case for androidpublisher_applications_data_safety

    
    """
    body = {"safetyLabels":"safetyLabels"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v3/applications/{package_name}/dataSafety'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_applications_device_tier_configs_create(client):
    """Test case for androidpublisher_applications_device_tier_configs_create

    
    """
    body = {"userCountrySets":[{"countryCodes":["countryCodes","countryCodes"],"name":"name"},{"countryCodes":["countryCodes","countryCodes"],"name":"name"}],"deviceTierSet":{"deviceTiers":[{"deviceGroupNames":["deviceGroupNames","deviceGroupNames"],"level":0},{"deviceGroupNames":["deviceGroupNames","deviceGroupNames"],"level":0}]},"deviceTierConfigId":"deviceTierConfigId","deviceGroups":[{"deviceSelectors":[{"requiredSystemFeatures":[{"name":"name"},{"name":"name"}],"forbiddenSystemFeatures":[{"name":"name"},{"name":"name"}],"deviceRam":{"minBytes":"minBytes","maxBytes":"maxBytes"},"excludedDeviceIds":[{"buildBrand":"buildBrand","buildDevice":"buildDevice"},{"buildBrand":"buildBrand","buildDevice":"buildDevice"}],"includedDeviceIds":[{"buildBrand":"buildBrand","buildDevice":"buildDevice"},{"buildBrand":"buildBrand","buildDevice":"buildDevice"}]},{"requiredSystemFeatures":[{"name":"name"},{"name":"name"}],"forbiddenSystemFeatures":[{"name":"name"},{"name":"name"}],"deviceRam":{"minBytes":"minBytes","maxBytes":"maxBytes"},"excludedDeviceIds":[{"buildBrand":"buildBrand","buildDevice":"buildDevice"},{"buildBrand":"buildBrand","buildDevice":"buildDevice"}],"includedDeviceIds":[{"buildBrand":"buildBrand","buildDevice":"buildDevice"},{"buildBrand":"buildBrand","buildDevice":"buildDevice"}]}],"name":"name"},{"deviceSelectors":[{"requiredSystemFeatures":[{"name":"name"},{"name":"name"}],"forbiddenSystemFeatures":[{"name":"name"},{"name":"name"}],"deviceRam":{"minBytes":"minBytes","maxBytes":"maxBytes"},"excludedDeviceIds":[{"buildBrand":"buildBrand","buildDevice":"buildDevice"},{"buildBrand":"buildBrand","buildDevice":"buildDevice"}],"includedDeviceIds":[{"buildBrand":"buildBrand","buildDevice":"buildDevice"},{"buildBrand":"buildBrand","buildDevice":"buildDevice"}]},{"requiredSystemFeatures":[{"name":"name"},{"name":"name"}],"forbiddenSystemFeatures":[{"name":"name"},{"name":"name"}],"deviceRam":{"minBytes":"minBytes","maxBytes":"maxBytes"},"excludedDeviceIds":[{"buildBrand":"buildBrand","buildDevice":"buildDevice"},{"buildBrand":"buildBrand","buildDevice":"buildDevice"}],"includedDeviceIds":[{"buildBrand":"buildBrand","buildDevice":"buildDevice"},{"buildBrand":"buildBrand","buildDevice":"buildDevice"}]}],"name":"name"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('allowUnknownDevices', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v3/applications/{package_name}/deviceTierConfigs'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_applications_device_tier_configs_get(client):
    """Test case for androidpublisher_applications_device_tier_configs_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v3/applications/{package_name}/deviceTierConfigs/{device_tier_config_id}'.format(package_name='package_name_example', device_tier_config_id='device_tier_config_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_applications_device_tier_configs_list(client):
    """Test case for androidpublisher_applications_device_tier_configs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v3/applications/{package_name}/deviceTierConfigs'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

