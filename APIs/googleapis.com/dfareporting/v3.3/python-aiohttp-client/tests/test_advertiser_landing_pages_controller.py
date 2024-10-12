# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advertiser_landing_pages_list_response import AdvertiserLandingPagesListResponse
from openapi_server.models.landing_page import LandingPage


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertiser_landing_pages_get(client):
    """Test case for dfareporting_advertiser_landing_pages_get

    
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertiserLandingPages/{id}'.format(profile_id='profile_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertiser_landing_pages_insert(client):
    """Test case for dfareporting_advertiser_landing_pages_insert

    
    """
    body = {"archived":True,"kind":"kind","name":"name","deepLinks":[{"fallbackUrl":"fallbackUrl","kind":"kind","mobileApp":{"kind":"kind","publisherName":"publisherName","id":"id","title":"title","directory":"UNKNOWN"},"appUrl":"appUrl","remarketingListIds":["remarketingListIds","remarketingListIds"]},{"fallbackUrl":"fallbackUrl","kind":"kind","mobileApp":{"kind":"kind","publisherName":"publisherName","id":"id","title":"title","directory":"UNKNOWN"},"appUrl":"appUrl","remarketingListIds":["remarketingListIds","remarketingListIds"]}],"id":"id","url":"url","advertiserId":"advertiserId"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertiserLandingPages'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertiser_landing_pages_list(client):
    """Test case for dfareporting_advertiser_landing_pages_list

    
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
                    ('advertiserIds', ['advertiser_ids_example']),
                    ('archived', True),
                    ('campaignIds', ['campaign_ids_example']),
                    ('ids', ['ids_example']),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('searchString', 'search_string_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('subaccountId', 'subaccount_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertiserLandingPages'.format(profile_id='profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertiser_landing_pages_patch(client):
    """Test case for dfareporting_advertiser_landing_pages_patch

    
    """
    body = {"archived":True,"kind":"kind","name":"name","deepLinks":[{"fallbackUrl":"fallbackUrl","kind":"kind","mobileApp":{"kind":"kind","publisherName":"publisherName","id":"id","title":"title","directory":"UNKNOWN"},"appUrl":"appUrl","remarketingListIds":["remarketingListIds","remarketingListIds"]},{"fallbackUrl":"fallbackUrl","kind":"kind","mobileApp":{"kind":"kind","publisherName":"publisherName","id":"id","title":"title","directory":"UNKNOWN"},"appUrl":"appUrl","remarketingListIds":["remarketingListIds","remarketingListIds"]}],"id":"id","url":"url","advertiserId":"advertiserId"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertiserLandingPages'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_advertiser_landing_pages_update(client):
    """Test case for dfareporting_advertiser_landing_pages_update

    
    """
    body = {"archived":True,"kind":"kind","name":"name","deepLinks":[{"fallbackUrl":"fallbackUrl","kind":"kind","mobileApp":{"kind":"kind","publisherName":"publisherName","id":"id","title":"title","directory":"UNKNOWN"},"appUrl":"appUrl","remarketingListIds":["remarketingListIds","remarketingListIds"]},{"fallbackUrl":"fallbackUrl","kind":"kind","mobileApp":{"kind":"kind","publisherName":"publisherName","id":"id","title":"title","directory":"UNKNOWN"},"appUrl":"appUrl","remarketingListIds":["remarketingListIds","remarketingListIds"]}],"id":"id","url":"url","advertiserId":"advertiserId"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/advertiserLandingPages'.format(profile_id='profile_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

