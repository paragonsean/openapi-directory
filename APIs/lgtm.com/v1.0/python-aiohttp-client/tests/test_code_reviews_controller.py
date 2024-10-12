# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.code_review import CodeReview
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_get_code_review(client):
    """Test case for get_code_review

    Get results of code review
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/codereviews/{review_id}'.format(review_id='review_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_request_review(client):
    """Test case for request_review

    Run code review for a patch
    """
    body = The contents of a binary patch file
    params = [('base', 'base_example'),
                    ('external-id', integer),
                    ('review-url', 'review_url_example'),
                    ('callback-url', 'callback_url_example'),
                    ('callback-secret', 'callback_secret_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1.0/codereviews/{project_id}'.format(project_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

