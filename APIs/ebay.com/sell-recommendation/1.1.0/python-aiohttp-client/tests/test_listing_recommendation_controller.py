# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.find_listing_recommendation_request import FindListingRecommendationRequest
from openapi_server.models.paged_listing_recommendation_collection import PagedListingRecommendationCollection


pytestmark = pytest.mark.asyncio

async def test_find_listing_recommendations(client):
    """Test case for find_listing_recommendations

    
    """
    body = {"listingIds":["listingIds","listingIds"]}
    params = [('filter', 'filter_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/recommendation/v1/find',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

