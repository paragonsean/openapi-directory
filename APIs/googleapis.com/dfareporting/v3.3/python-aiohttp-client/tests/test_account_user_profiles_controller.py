# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_user_profile import AccountUserProfile
from openapi_server.models.account_user_profiles_list_response import AccountUserProfilesListResponse


pytestmark = pytest.mark.asyncio

async def test_dfareporting_account_user_profiles_get(client):
    """Test case for dfareporting_account_user_profiles_get

    
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accountUserProfiles/{id}'.format(profile_id='profile_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_account_user_profiles_insert(client):
    """Test case for dfareporting_account_user_profiles_insert

    
    """
    body = {"subaccountId":"subaccountId","userRoleFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"comments":"comments","siteFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"kind":"kind","traffickerType":"INTERNAL_NON_TRAFFICKER","advertiserFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"active":True,"locale":"locale","userAccessType":"NORMAL_USER","accountId":"accountId","name":"name","id":"id","userRoleId":"userRoleId","campaignFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"email":"email"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accountUserProfiles'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_account_user_profiles_list(client):
    """Test case for dfareporting_account_user_profiles_list

    
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
                    ('active', True),
                    ('ids', ['ids_example']),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('searchString', 'search_string_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('subaccountId', 'subaccount_id_example'),
                    ('userRoleId', 'user_role_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accountUserProfiles'.format(profile_id='profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_account_user_profiles_patch(client):
    """Test case for dfareporting_account_user_profiles_patch

    
    """
    body = {"subaccountId":"subaccountId","userRoleFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"comments":"comments","siteFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"kind":"kind","traffickerType":"INTERNAL_NON_TRAFFICKER","advertiserFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"active":True,"locale":"locale","userAccessType":"NORMAL_USER","accountId":"accountId","name":"name","id":"id","userRoleId":"userRoleId","campaignFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"email":"email"}
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
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accountUserProfiles'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_account_user_profiles_update(client):
    """Test case for dfareporting_account_user_profiles_update

    
    """
    body = {"subaccountId":"subaccountId","userRoleFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"comments":"comments","siteFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"kind":"kind","traffickerType":"INTERNAL_NON_TRAFFICKER","advertiserFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"active":True,"locale":"locale","userAccessType":"NORMAL_USER","accountId":"accountId","name":"name","id":"id","userRoleId":"userRoleId","campaignFilter":{"kind":"kind","objectIds":["objectIds","objectIds"],"status":"NONE"},"email":"email"}
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
        method='PUT',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accountUserProfiles'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

