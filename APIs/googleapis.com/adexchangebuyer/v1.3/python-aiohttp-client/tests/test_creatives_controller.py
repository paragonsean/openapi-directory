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
        path='/adexchangebuyer/v1.3/creatives/{account_id}/{buyer_creative_id}'.format(account_id=56, buyer_creative_id='buyer_creative_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_creatives_insert(client):
    """Test case for adexchangebuyer_creatives_insert

    
    """
    body = {"disapprovalReasons":[{"reason":"reason","details":["details","details"]},{"reason":"reason","details":["details","details"]}],"vendorType":[1,1],"HTMLSnippet":"HTMLSnippet","agencyId":"agencyId","adTechnologyProviders":{"hasUnidentifiedProvider":True,"detectedProviderIds":["detectedProviderIds","detectedProviderIds"]},"advertiserName":"advertiserName","buyerCreativeId":"buyerCreativeId","videoURL":"videoURL","attribute":[6,6],"height":5,"sensitiveCategories":[1,1],"filteringReasons":{"date":"date","reasons":[{"filteringStatus":1,"filteringCount":"filteringCount"},{"filteringStatus":1,"filteringCount":"filteringCount"}]},"kind":"adexchangebuyer#creative","clickThroughUrl":["clickThroughUrl","clickThroughUrl"],"impressionTrackingUrl":["impressionTrackingUrl","impressionTrackingUrl"],"version":6,"advertiserId":["advertiserId","advertiserId"],"restrictedCategories":[1,1],"accountId":0,"productCategories":[7,7],"corrections":[{"reason":"reason","details":["details","details"]},{"reason":"reason","details":["details","details"]}],"nativeAd":{"advertiser":"advertiser","image":{"width":9,"url":"url","height":7},"appIcon":{"width":2,"url":"url","height":5},"clickTrackingUrl":"clickTrackingUrl","price":"price","impressionTrackingUrl":["impressionTrackingUrl","impressionTrackingUrl"],"logo":{"width":2,"url":"url","height":3},"body":"body","starRating":4.145608029883936,"headline":"headline","callToAction":"callToAction"},"apiUploadTimestamp":"2000-01-23T04:56:07.000+00:00","width":7,"status":"status"}
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
        path='/adexchangebuyer/v1.3/creatives',
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
                    ('accountId', [56]),
                    ('buyerCreativeId', ['buyer_creative_id_example']),
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
        path='/adexchangebuyer/v1.3/creatives',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

