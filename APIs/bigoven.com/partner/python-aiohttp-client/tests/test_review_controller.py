# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api2_controllers_web_api_review_controller_post_reply_req import API2ControllersWebAPIReviewControllerPostReplyReq
from openapi_server.models.api2_controllers_web_api_review_controller_review_request import API2ControllersWebAPIReviewControllerReviewRequest
from openapi_server.models.api2_controllers_web_api_review_controller_review_request_legacy import API2ControllersWebAPIReviewControllerReviewRequestLegacy
from openapi_server.models.big_oven_model_api_reply import BigOvenModelAPIReply
from openapi_server.models.big_oven_model_api_review import BigOvenModelAPIReview


pytestmark = pytest.mark.asyncio

async def test_recipe_recipe_id_review_get(client):
    """Test case for recipe_recipe_id_review_get

    Get *my* review for the recipe {recipeId}, where \"me\" is determined by standard authentication headers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/review'.format(recipe_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipe_review_review_id_get(client):
    """Test case for recipe_review_review_id_get

    Get a given review by string-style ID. This will return a payload with FeaturedReply, ReplyCount.              Recommended display is to list top-level reviews with one featured reply underneath.               Currently, the FeaturedReply is the most recent one for that rating.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/review/{review_id}'.format(review_id='review_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_review_delete(client):
    """Test case for review_delete

    DEPRECATED! - Deletes a review by recipeId and reviewId. Please use recipe/review/{reviewId} instead.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/recipe/{recipe_id}/review/{review_id}'.format(recipe_id=56, review_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_review_delete_reply(client):
    """Test case for review_delete_reply

    DELETE a reply to a given review. Authenticated user must be the one who originally posted the reply.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/recipe/review/replies/{reply_id}'.format(reply_id='reply_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_review_get(client):
    """Test case for review_get

    Get a given review - DEPRECATED. See recipe/review/{reviewId} for the current usage.              Beginning in January 2017, BigOven moded from an integer-based ID system to a GUID-style string-based ID system for reviews and replies.              We are also supporting more of a \"Google Play\" style model for Reviews and Replies. That is, there are top-level Reviews and then              an unlimited list of replies (which do not carry star ratings) underneath existing reviews. Also, a given user can only have one review               per recipe. Existing legacy endpoints will continue to work, but we strongly recommend you migrate to using the newer endpoints listed              which do NOT carry the \"DEPRECATED\" flag.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/review/{review_id}'.format(review_id=56, recipe_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_review_get_replies(client):
    """Test case for review_get_replies

    Get a paged list of replies for a given review.
    """
    params = [('pg', 56),
                    ('rpp', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/review/{review_id}/replies'.format(review_id='review_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_review_get_reviews(client):
    """Test case for review_get_reviews

    Get paged list of reviews for a recipe. Each review will have at most one FeaturedReply, as well as a ReplyCount.
    """
    params = [('pg', 56),
                    ('rpp', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recipe/{recipe_id}/reviews'.format(recipe_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_review_post(client):
    """Test case for review_post

    Add a new review. Only one review can be provided per {userId, recipeId} pair. Otherwise your review will be updated.
    """
    body = openapi_server.API2ControllersWebAPIReviewControllerReviewRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe/{recipe_id}/review'.format(recipe_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_review_post_reply(client):
    """Test case for review_post_reply

    POST a reply to a given review. The date will be set by server. Note that replies no longer have star ratings, only top-level reviews do.
    """
    body = openapi_server.API2ControllersWebAPIReviewControllerPostReplyReq()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/recipe/review/{review_id}/replies'.format(review_id='review_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_review_put(client):
    """Test case for review_put

    Update a given top-level review.
    """
    body = openapi_server.API2ControllersWebAPIReviewControllerReviewRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/recipe/review/{review_id}'.format(review_id='review_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_review_put_legacy(client):
    """Test case for review_put_legacy

    HTTP PUT (update) a recipe review. DEPRECATED. Please see recipe/review/{reviewId} PUT for the new endpoint.              We are moving to a string-based primary key system, no longer integers, for reviews and replies.
    """
    body = openapi_server.API2ControllersWebAPIReviewControllerReviewRequestLegacy()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/recipe/{recipe_id}/review/{review_id}'.format(review_id=56, recipe_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_review_put_reply(client):
    """Test case for review_put_reply

    Update (PUT) a reply to a given review. Authenticated user must be the original one that posted the reply.
    """
    body = openapi_server.API2ControllersWebAPIReviewControllerPostReplyReq()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/recipe/review/replies/{reply_id}'.format(reply_id='reply_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

