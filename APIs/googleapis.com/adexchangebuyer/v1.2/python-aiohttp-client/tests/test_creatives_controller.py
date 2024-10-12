# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.creative import Creative
from openapi_server.models.creatives_list import CreativesList


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_creatives_get(client):
    """Test case for adexchangebuyer_creatives_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.2/creatives/{account_id}/{buyer_creative_id}'.format(account_id=56, buyer_creative_id='buyer_creative_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_creatives_insert(client):
    """Test case for adexchangebuyer_creatives_insert

    
    """
    body = {"disapprovalReasons":[{"reason":"reason","details":["details","details"]},{"reason":"reason","details":["details","details"]}],"vendorType":[9,9],"HTMLSnippet":"HTMLSnippet","filteringReasons":{"date":"date","reasons":[{"filteringStatus":1,"filteringCount":"filteringCount"},{"filteringStatus":1,"filteringCount":"filteringCount"}]},"kind":"adexchangebuyer#creative","clickThroughUrl":["clickThroughUrl","clickThroughUrl"],"impressionTrackingUrl":["impressionTrackingUrl","impressionTrackingUrl"],"agencyId":"agencyId","version":3,"advertiserName":"advertiserName","advertiserId":["advertiserId","advertiserId"],"buyerCreativeId":"buyerCreativeId","restrictedCategories":[2,2],"accountId":0,"productCategories":[5,5],"corrections":[{"reason":"reason","details":["details","details"]},{"reason":"reason","details":["details","details"]}],"videoURL":"videoURL","apiUploadTimestamp":"2000-01-23T04:56:07.000+00:00","width":2,"attribute":[6,6],"height":5,"sensitiveCategories":[7,7],"status":"status"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adexchangebuyer/v1.2/creatives',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_creatives_list(client):
    """Test case for adexchangebuyer_creatives_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('statusFilter', 'status_filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.2/creatives',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

