# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ad_group import AdGroup
from openapi_server.models.ad_group_paged_collection_response import AdGroupPagedCollectionResponse
from openapi_server.models.create_ad_group_request import CreateAdGroupRequest
from openapi_server.models.targeted_bid_request import TargetedBidRequest
from openapi_server.models.targeted_bids_paged_collection import TargetedBidsPagedCollection
from openapi_server.models.targeted_keyword_request import TargetedKeywordRequest
from openapi_server.models.targeted_keywords_paged_collection import TargetedKeywordsPagedCollection
from openapi_server.models.update_ad_group_request import UpdateAdGroupRequest


pytestmark = pytest.mark.asyncio

async def test_create_ad_group(client):
    """Test case for create_ad_group

    
    """
    body = {"name":"name","defaultBid":{"currency":"currency","value":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ad_group(client):
    """Test case for get_ad_group

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}'.format(ad_group_id='ad_group_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ad_groups(client):
    """Test case for get_ad_groups

    
    """
    params = [('ad_group_status', 'ad_group_status_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group'.format(campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suggest_bids(client):
    """Test case for suggest_bids

    
    """
    body = {"keywords":[{"matchType":"matchType","keywordText":"keywordText"},{"matchType":"matchType","keywordText":"keywordText"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids'.format(ad_group_id='ad_group_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suggest_keywords(client):
    """Test case for suggest_keywords

    
    """
    body = {"listingIds":["listingIds","listingIds"],"matchType":"matchType","additionalInfo":["additionalInfo","additionalInfo"],"exclusions":["exclusions","exclusions"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_keywords'.format(ad_group_id='ad_group_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ad_group(client):
    """Test case for update_ad_group

    
    """
    body = {"adGroupStatus":"adGroupStatus","name":"name","defaultBid":{"currency":"currency","value":"value"}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}'.format(ad_group_id='ad_group_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

