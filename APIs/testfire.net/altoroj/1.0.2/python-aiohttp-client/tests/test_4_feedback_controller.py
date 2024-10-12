# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.feedback import Feedback


pytestmark = pytest.mark.asyncio

async def test_get_feedback(client):
    """Test case for get_feedback

    
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/api/feedback/{feedback_id}'.format(feedback_id='feedback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_feedback(client):
    """Test case for send_feedback

    
    """
    body = openapi_server.Feedback()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/feedback/submit',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

