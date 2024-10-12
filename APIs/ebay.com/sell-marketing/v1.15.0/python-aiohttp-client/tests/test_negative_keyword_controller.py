# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_create_negative_keyword_request import BulkCreateNegativeKeywordRequest
from openapi_server.models.bulk_create_negative_keyword_response import BulkCreateNegativeKeywordResponse
from openapi_server.models.bulk_update_negative_keyword_request import BulkUpdateNegativeKeywordRequest
from openapi_server.models.bulk_update_negative_keyword_response import BulkUpdateNegativeKeywordResponse
from openapi_server.models.create_negative_keyword_request import CreateNegativeKeywordRequest
from openapi_server.models.negative_keyword import NegativeKeyword
from openapi_server.models.negative_keyword_paged_collection_response import NegativeKeywordPagedCollectionResponse
from openapi_server.models.update_negative_keyword_request import UpdateNegativeKeywordRequest


pytestmark = pytest.mark.asyncio

async def test_bulk_create_negative_keyword(client):
    """Test case for bulk_create_negative_keyword

    
    """
    body = {"requests":[{"negativeKeywordText":"negativeKeywordText","campaignId":"campaignId","negativeKeywordMatchType":"negativeKeywordMatchType","adGroupId":"adGroupId"},{"negativeKeywordText":"negativeKeywordText","campaignId":"campaignId","negativeKeywordMatchType":"negativeKeywordMatchType","adGroupId":"adGroupId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/bulk_create_negative_keyword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_negative_keyword(client):
    """Test case for bulk_update_negative_keyword

    
    """
    body = {"requests":[{"negativeKeywordStatus":"negativeKeywordStatus","negativeKeywordId":"negativeKeywordId"},{"negativeKeywordStatus":"negativeKeywordStatus","negativeKeywordId":"negativeKeywordId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/bulk_update_negative_keyword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_negative_keyword(client):
    """Test case for create_negative_keyword

    
    """
    body = {"negativeKeywordText":"negativeKeywordText","campaignId":"campaignId","negativeKeywordMatchType":"negativeKeywordMatchType","adGroupId":"adGroupId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/negative_keyword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_negative_keyword(client):
    """Test case for get_negative_keyword

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/negative_keyword/{negative_keyword_id}'.format(negative_keyword_id='negative_keyword_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_negative_keywords(client):
    """Test case for get_negative_keywords

    
    """
    params = [('ad_group_ids', 'ad_group_ids_example'),
                    ('campaign_ids', 'campaign_ids_example'),
                    ('limit', 'limit_example'),
                    ('negative_keyword_status', 'negative_keyword_status_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/negative_keyword',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_negative_keyword(client):
    """Test case for update_negative_keyword

    
    """
    body = {"negativeKeywordStatus":"negativeKeywordStatus"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/marketing/v1/negative_keyword/{negative_keyword_id}'.format(negative_keyword_id='negative_keyword_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

