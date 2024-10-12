# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_review_post200_response import PostReviewPost200Response
from openapi_server.models.post_review_post400_response import PostReviewPost400Response
from openapi_server.models.post_review_post401_response import PostReviewPost401Response
from openapi_server.models.post_review_post403_response import PostReviewPost403Response
from openapi_server.models.post_review_post_request import PostReviewPostRequest


pytestmark = pytest.mark.asyncio

async def test_post_review_post(client):
    """Test case for post_review_post

    Posts the user's review to Stellastra
    """
    body = openapi_server.PostReviewPostRequest()
    params = [('user_email', '{\"user_email\":\"johnsmith@companyxyz.com\"}'),
                    ('user_name', '{\"user_name\":\"John\"}'),
                    ('rating', {"rating":5})]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/post-review',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

