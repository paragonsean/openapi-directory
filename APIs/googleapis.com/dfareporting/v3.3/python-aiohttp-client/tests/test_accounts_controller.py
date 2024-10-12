# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts_list_response import AccountsListResponse


pytestmark = pytest.mark.asyncio

async def test_dfareporting_accounts_get(client):
    """Test case for dfareporting_accounts_get

    
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accounts/{id}'.format(profile_id='profile_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_accounts_list(client):
    """Test case for dfareporting_accounts_list

    
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
                    ('sortOrder', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accounts'.format(profile_id='profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_accounts_patch(client):
    """Test case for dfareporting_accounts_patch

    
    """
    body = {"shareReportsWithTwitter":True,"teaserSizeLimit":"teaserSizeLimit","accountPermissionIds":["accountPermissionIds","accountPermissionIds"],"nielsenOcrEnabled":True,"accountProfile":"ACCOUNT_PROFILE_BASIC","kind":"kind","activeAdsLimitTier":"ACTIVE_ADS_TIER_40K","activeViewOptOut":True,"maximumImageSize":"maximumImageSize","active":True,"description":"description","locale":"locale","countryId":"countryId","reportsConfiguration":{"reportGenerationTimeZoneId":"reportGenerationTimeZoneId","lookbackConfiguration":{"postImpressionActivitiesDuration":6,"clickDuration":0},"exposureToConversionEnabled":True},"defaultCreativeSizeId":"defaultCreativeSizeId","availablePermissionIds":["availablePermissionIds","availablePermissionIds"],"name":"name","id":"id","currencyId":"currencyId"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accounts'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_accounts_update(client):
    """Test case for dfareporting_accounts_update

    
    """
    body = {"shareReportsWithTwitter":True,"teaserSizeLimit":"teaserSizeLimit","accountPermissionIds":["accountPermissionIds","accountPermissionIds"],"nielsenOcrEnabled":True,"accountProfile":"ACCOUNT_PROFILE_BASIC","kind":"kind","activeAdsLimitTier":"ACTIVE_ADS_TIER_40K","activeViewOptOut":True,"maximumImageSize":"maximumImageSize","active":True,"description":"description","locale":"locale","countryId":"countryId","reportsConfiguration":{"reportGenerationTimeZoneId":"reportGenerationTimeZoneId","lookbackConfiguration":{"postImpressionActivitiesDuration":6,"clickDuration":0},"exposureToConversionEnabled":True},"defaultCreativeSizeId":"defaultCreativeSizeId","availablePermissionIds":["availablePermissionIds","availablePermissionIds"],"name":"name","id":"id","currencyId":"currencyId"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accounts'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

