# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_feedback_feedback_id_get(client):
    """Test case for feedback_feedback_id_get

    Feedback details
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/feedback/{feedback_id}'.format(feedback_id='feedback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

