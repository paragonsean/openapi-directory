# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_review_request import EditReviewRequest
from openapi_server.models.get_reviewby_review_id200_response import GetReviewbyReviewId200Response
from openapi_server.models.getalistof_reviews200_response import GetalistofReviews200Response
from openapi_server.models.save_multiple_reviews_request import SaveMultipleReviewsRequest
from openapi_server.models.save_review200_response import SaveReview200Response
from openapi_server.models.save_review_request import SaveReviewRequest


pytestmark = pytest.mark.asyncio

async def test_delete_multiple_reviews(client):
    """Test case for delete_multiple_reviews

    Delete Multiple Reviews
    """
    body = ["babefcf4-e0f7-11ec-835d-16c4e59c4351","qweqweee-e0f7-11ec-835d-16c4e59c4351","asdffggg-e0f7-11ec-835d-16c4e59c4351"]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/reviews',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_review(client):
    """Test case for delete_review

    Delete Review
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/review/{review_id}'.format(review_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_review(client):
    """Test case for edit_review

    Update a Review
    """
    body = openapi_server.EditReviewRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/review/{review_id}'.format(review_id='5323fdaa-c012-11ec-835d-0ebee58edbb3'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reviewby_review_id(client):
    """Test case for get_reviewby_review_id

    Get Review by Review ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/review/{review_id}'.format(review_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getalistof_reviews(client):
    """Test case for getalistof_reviews

    Get a list of Reviews
    """
    params = [('search_term', 'search_term'),
                    ('from', '0'),
                    ('to', '3'),
                    ('order_by', ':asc'),
                    ('status', true),
                    ('product_id', '1')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/reviews',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_multiple_reviews(client):
    """Test case for save_multiple_reviews

    Create Multiple Reviews
    """
    body = {"approved":False,"productId":"1","rating":4,"reviewerName":"Arturo","text":"Great product!","title":"Great product","verifiedPurchaser":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/reviews',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_review(client):
    """Test case for save_review

    Create a Review
    """
    body = {"productId":"65444","rating":5,"reviewerName":"Arturo","text":"It is the best product that I have seen","title":"Good Product"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/review',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

