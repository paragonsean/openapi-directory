# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_post_action_webhook_failures_id_retry(client):
    """Test case for post_action_webhook_failures_id_retry

    retry Action Webhook Failure
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/action_webhook_failures/{id}/retry'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

