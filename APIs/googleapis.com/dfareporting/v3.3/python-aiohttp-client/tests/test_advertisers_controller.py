# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advertiser import Advertiser
from openapi_server.models.advertisers_list_response import AdvertisersListResponse


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertisers_get(client):
    """Test case for dfareporting_advertisers_get

    
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertisers/{id}'.format(profile_id='profile_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertisers_insert(client):
    """Test case for dfareporting_advertisers_insert

    
    """
    body = {"subaccountId":"subaccountId","kind":"kind","originalFloodlightConfigurationId":"originalFloodlightConfigurationId","floodlightConfigurationIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"suspended":True,"floodlightConfigurationId":"floodlightConfigurationId","accountId":"accountId","defaultClickThroughEventTagId":"defaultClickThroughEventTagId","advertiserGroupId":"advertiserGroupId","defaultEmail":"defaultEmail","name":"name","clickThroughUrlSuffix":"clickThroughUrlSuffix","id":"id","status":"APPROVED"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertisers'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertisers_list(client):
    """Test case for dfareporting_advertisers_list

    
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
                    ('advertiserGroupIds', ['advertiser_group_ids_example']),
                    ('floodlightConfigurationIds', ['floodlight_configuration_ids_example']),
                    ('ids', ['ids_example']),
                    ('includeAdvertisersWithoutGroupsOnly', True),
                    ('maxResults', 56),
                    ('onlyParent', True),
                    ('pageToken', 'page_token_example'),
                    ('searchString', 'search_string_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('status', 'status_example'),
                    ('subaccountId', 'subaccount_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertisers'.format(profile_id='profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertisers_patch(client):
    """Test case for dfareporting_advertisers_patch

    
    """
    body = {"subaccountId":"subaccountId","kind":"kind","originalFloodlightConfigurationId":"originalFloodlightConfigurationId","floodlightConfigurationIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"suspended":True,"floodlightConfigurationId":"floodlightConfigurationId","accountId":"accountId","defaultClickThroughEventTagId":"defaultClickThroughEventTagId","advertiserGroupId":"advertiserGroupId","defaultEmail":"defaultEmail","name":"name","clickThroughUrlSuffix":"clickThroughUrlSuffix","id":"id","status":"APPROVED"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertisers'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertisers_update(client):
    """Test case for dfareporting_advertisers_update

    
    """
    body = {"subaccountId":"subaccountId","kind":"kind","originalFloodlightConfigurationId":"originalFloodlightConfigurationId","floodlightConfigurationIdDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"idDimensionValue":{"kind":"kind","matchType":"EXACT","etag":"etag","id":"id","value":"value","dimensionName":"dimensionName"},"suspended":True,"floodlightConfigurationId":"floodlightConfigurationId","accountId":"accountId","defaultClickThroughEventTagId":"defaultClickThroughEventTagId","advertiserGroupId":"advertiserGroupId","defaultEmail":"defaultEmail","name":"name","clickThroughUrlSuffix":"clickThroughUrlSuffix","id":"id","status":"APPROVED"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertisers'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

