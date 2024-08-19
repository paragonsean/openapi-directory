# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.review import Review
from openapi_server.models.review_pages import ReviewPages


pytestmark = pytest.mark.asyncio

async def test_reviews_get(client):
    """Test case for reviews_get

    Find reviews for a particular App and marketplace. Results are automatically paginated when limit is set
    """
    params = [('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('pageNumber', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/reviews',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_post(client):
    """Test case for reviews_post

    Post a review from a User and returns the new post
    """
    params = [('appId', 'app_id_example'),
                    ('userId', 'user_id_example'),
                    ('userAccountId', 'user_account_id_example'),
                    ('headline', 'headline_example'),
                    ('rating', 56),
                    ('description', 'description_example'),
                    ('type', 'type_example'),
                    ('mustOwnApp', True),
                    ('autoApprove', True),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/reviews',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_review_id_delete(client):
    """Test case for reviews_review_id_delete

    Remove a review
    """
    params = [('userId', 'user_id_example'),
                    ('userAccountId', 'user_account_id_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/reviews/{review_id}'.format(review_id='review_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_review_id_get(client):
    """Test case for reviews_review_id_get

    Find a Review within a particular App and marketplace
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/reviews/{review_id}'.format(review_id='review_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_review_id_patch(client):
    """Test case for reviews_review_id_patch

    Update a review fields
    """
    params = [('userId', 'user_id_example'),
                    ('userAccountId', 'user_account_id_example'),
                    ('headline', 'headline_example'),
                    ('rating', 56),
                    ('description', 'description_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/reviews/{review_id}'.format(review_id='review_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_review_id_post(client):
    """Test case for reviews_review_id_post

    Update a review from a User and returns the new post
    """
    params = [('userId', 'user_id_example'),
                    ('userAccountId', 'user_account_id_example'),
                    ('headline', 'headline_example'),
                    ('rating', 56),
                    ('description', 'description_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/reviews/{review_id}'.format(review_id='review_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

