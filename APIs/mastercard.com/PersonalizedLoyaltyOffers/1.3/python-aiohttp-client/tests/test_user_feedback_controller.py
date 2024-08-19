# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_feedback_response import UserFeedbackResponse


pytestmark = pytest.mark.asyncio

async def test_userfeedback_post(client):
    """Test case for userfeedback_post

    Provide User Feedback on Offer
    """
    params = [('FId', '999999'),
                    ('UserToken', 'user_token_example'),
                    ('OfferId', 'd82e1e7c-c6b9-3b46-acd0-5498731c2838'),
                    ('Feedback', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plo/v1/userfeedback',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

