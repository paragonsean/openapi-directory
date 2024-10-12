# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.critics_resource_type_json_get200_response import CriticsResourceTypeJsonGet200Response
from openapi_server.models.reviews_search_json_get200_response import ReviewsSearchJsonGet200Response


pytestmark = pytest.mark.asyncio

async def test_critics_resource_type_json_get(client):
    """Test case for critics_resource_type_json_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/movies/v2/critics/{resource_type_jso}'.format(resource_type='resource_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_resource_type_json_get(client):
    """Test case for reviews_resource_type_json_get

    
    """
    params = [('offset', 20),
                    ('order', by-publication-date)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/movies/v2/reviews/{resource_type_jso}'.format(resource_type='resource_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_search_json_get(client):
    """Test case for reviews_search_json_get

    
    """
    params = [('query', 'query_example'),
                    ('critics-pick', 'critics_pick_example'),
                    ('reviewer', 'reviewer_example'),
                    ('publication-date', 'publication_date_example'),
                    ('opening-date', 'opening_date_example'),
                    ('offset', 20),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/movies/v2/reviews/search.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

