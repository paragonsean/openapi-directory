# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.creative import Creative
from openapi_server.models.creative_deal_ids import CreativeDealIds
from openapi_server.models.creatives_list import CreativesList


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_creatives_add_deal(client):
    """Test case for adexchangebuyer_creatives_add_deal

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adexchangebuyer/v1.4/creatives/{account_id}/{buyer_creative_id}/addDeal/{deal_id}'.format(account_id=56, buyer_creative_id='buyer_creative_id_example', deal_id='deal_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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
        path='/adexchangebuyer/v1.4/creatives/{account_id}/{buyer_creative_id}'.format(account_id=56, buyer_creative_id='buyer_creative_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_creatives_insert(client):
    """Test case for adexchangebuyer_creatives_insert

    
    """
    body = {"vendorType":[7,7],"HTMLSnippet":"HTMLSnippet","dealsStatus":"dealsStatus","servingRestrictions":[{"disapprovalReasons":[{"reason":"reason","details":["details","details"]},{"reason":"reason","details":["details","details"]}],"reason":"reason","contexts":[{"geoCriteriaId":[6,6],"contextType":"contextType","auctionType":["auctionType","auctionType"],"platform":["platform","platform"]},{"geoCriteriaId":[6,6],"contextType":"contextType","auctionType":["auctionType","auctionType"],"platform":["platform","platform"]}]},{"disapprovalReasons":[{"reason":"reason","details":["details","details"]},{"reason":"reason","details":["details","details"]}],"reason":"reason","contexts":[{"geoCriteriaId":[6,6],"contextType":"contextType","auctionType":["auctionType","auctionType"],"platform":["platform","platform"]},{"geoCriteriaId":[6,6],"contextType":"contextType","auctionType":["auctionType","auctionType"],"platform":["platform","platform"]}]}],"agencyId":"agencyId","adTechnologyProviders":{"hasUnidentifiedProvider":True,"detectedProviderIds":["detectedProviderIds","detectedProviderIds"]},"advertiserName":"advertiserName","buyerCreativeId":"buyerCreativeId","videoURL":"videoURL","detectedDomains":["detectedDomains","detectedDomains"],"videoVastXML":"videoVastXML","attribute":[6,6],"creativeStatusIdentityType":"creativeStatusIdentityType","height":5,"sensitiveCategories":[1,1],"languages":["languages","languages"],"filteringReasons":{"date":"date","reasons":[{"filteringStatus":5,"filteringCount":"filteringCount"},{"filteringStatus":5,"filteringCount":"filteringCount"}]},"kind":"adexchangebuyer#creative","clickThroughUrl":["clickThroughUrl","clickThroughUrl"],"impressionTrackingUrl":["impressionTrackingUrl","impressionTrackingUrl"],"version":1,"advertiserId":["advertiserId","advertiserId"],"restrictedCategories":[1,1],"accountId":0,"productCategories":[1,1],"corrections":[{"reason":"reason","details":["details","details"],"contexts":[{"geoCriteriaId":[1,1],"contextType":"contextType","auctionType":["auctionType","auctionType"],"platform":["platform","platform"]},{"geoCriteriaId":[1,1],"contextType":"contextType","auctionType":["auctionType","auctionType"],"platform":["platform","platform"]}]},{"reason":"reason","details":["details","details"],"contexts":[{"geoCriteriaId":[1,1],"contextType":"contextType","auctionType":["auctionType","auctionType"],"platform":["platform","platform"]},{"geoCriteriaId":[1,1],"contextType":"contextType","auctionType":["auctionType","auctionType"],"platform":["platform","platform"]}]}],"nativeAd":{"advertiser":"advertiser","image":{"width":3,"url":"url","height":9},"clickLinkUrl":"clickLinkUrl","impressionTrackingUrl":["impressionTrackingUrl","impressionTrackingUrl"],"body":"body","callToAction":"callToAction","appIcon":{"width":7,"url":"url","height":2},"clickTrackingUrl":"clickTrackingUrl","videoURL":"videoURL","price":"price","logo":{"width":4,"url":"url","height":2},"starRating":7.386281948385884,"headline":"headline"},"adChoicesDestinationUrl":"adChoicesDestinationUrl","apiUploadTimestamp":"2000-01-23T04:56:07.000+00:00","width":4,"openAuctionStatus":"openAuctionStatus"}
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
        path='/adexchangebuyer/v1.4/creatives',
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
                    ('dealsStatusFilter', 'deals_status_filter_example'),
                    ('maxResults', 56),
                    ('openAuctionStatusFilter', 'open_auction_status_filter_example'),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.4/creatives',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_creatives_list_deals(client):
    """Test case for adexchangebuyer_creatives_list_deals

    
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
        path='/adexchangebuyer/v1.4/creatives/{account_id}/{buyer_creative_id}/listDeals'.format(account_id=56, buyer_creative_id='buyer_creative_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_creatives_remove_deal(client):
    """Test case for adexchangebuyer_creatives_remove_deal

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adexchangebuyer/v1.4/creatives/{account_id}/{buyer_creative_id}/removeDeal/{deal_id}'.format(account_id=56, buyer_creative_id='buyer_creative_id_example', deal_id='deal_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

