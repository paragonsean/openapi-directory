# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_create_keyword_request import BulkCreateKeywordRequest
from openapi_server.models.bulk_create_keyword_response import BulkCreateKeywordResponse
from openapi_server.models.bulk_update_keyword_request import BulkUpdateKeywordRequest
from openapi_server.models.bulk_update_keyword_response import BulkUpdateKeywordResponse
from openapi_server.models.create_keyword_request import CreateKeywordRequest
from openapi_server.models.keyword import Keyword
from openapi_server.models.keyword_paged_collection_response import KeywordPagedCollectionResponse
from openapi_server.models.update_keyword_request import UpdateKeywordRequest


pytestmark = pytest.mark.asyncio

async def test_bulk_create_keyword(client):
    """Test case for bulk_create_keyword

    
    """
    body = {"requests":[{"matchType":"matchType","bid":{"currency":"currency","value":"value"},"adGroupId":"adGroupId","keywordText":"keywordText"},{"matchType":"matchType","bid":{"currency":"currency","value":"value"},"adGroupId":"adGroupId","keywordText":"keywordText"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_keyword'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_keyword(client):
    """Test case for bulk_update_keyword

    
    """
    body = {"requests":[{"keywordId":"keywordId","keywordStatus":"keywordStatus","bid":{"currency":"currency","value":"value"}},{"keywordId":"keywordId","keywordStatus":"keywordStatus","bid":{"currency":"currency","value":"value"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_keyword'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_keyword(client):
    """Test case for create_keyword

    
    """
    body = {"matchType":"matchType","bid":{"currency":"currency","value":"value"},"adGroupId":"adGroupId","keywordText":"keywordText"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/keyword'.format(campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keyword(client):
    """Test case for get_keyword

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/keyword/{keyword_id}'.format(campaign_id='campaign_id_example', keyword_id='keyword_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keywords(client):
    """Test case for get_keywords

    
    """
    params = [('ad_group_ids', 'ad_group_ids_example'),
                    ('keyword_status', 'keyword_status_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/keyword'.format(campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_keyword(client):
    """Test case for update_keyword

    
    """
    body = {"keywordStatus":"keywordStatus","bid":{"currency":"currency","value":"value"}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/marketing/v1/ad_campaign/{campaign_id}/keyword/{keyword_id}'.format(campaign_id='campaign_id_example', keyword_id='keyword_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

