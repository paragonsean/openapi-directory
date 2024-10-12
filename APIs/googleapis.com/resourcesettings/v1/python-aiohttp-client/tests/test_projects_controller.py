# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_resourcesettings_v1_list_settings_response import GoogleCloudResourcesettingsV1ListSettingsResponse
from openapi_server.models.google_cloud_resourcesettings_v1_setting import GoogleCloudResourcesettingsV1Setting


pytestmark = pytest.mark.asyncio

async def test_resourcesettings_projects_settings_get(client):
    """Test case for resourcesettings_projects_settings_get

    
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
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resourcesettings_projects_settings_list(client):
    """Test case for resourcesettings_projects_settings_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/settings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resourcesettings_projects_settings_patch(client):
    """Test case for resourcesettings_projects_settings_patch

    
    """
    body = {"metadata":{"defaultValue":{"stringValue":"stringValue","stringSetValue":{"values":["values","values"]},"enumValue":{"value":"value"},"stringMapValue":{"mappings":{"key":"mappings"}},"durationValue":"durationValue","booleanValue":True},"displayName":"displayName","dataType":"DATA_TYPE_UNSPECIFIED","description":"description","readOnly":True},"effectiveValue":{"stringValue":"stringValue","stringSetValue":{"values":["values","values"]},"enumValue":{"value":"value"},"stringMapValue":{"mappings":{"key":"mappings"}},"durationValue":"durationValue","booleanValue":True},"name":"name","etag":"etag","localValue":{"stringValue":"stringValue","stringSetValue":{"values":["values","values"]},"enumValue":{"value":"value"},"stringMapValue":{"mappings":{"key":"mappings"}},"durationValue":"durationValue","booleanValue":True}}
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
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

