# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.enable_two_step_request_body import EnableTwoStepRequestBody


pytestmark = pytest.mark.asyncio

async def test_disable_two_step(client):
    """Test case for disable_two_step

    Disable-Two-Step
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/settings/account/two-step',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_two_step(client):
    """Test case for enable_two_step

    Enable-Two-Step
    """
    body = {"pin":"<Two-Step Verification PIN>"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/settings/account/two-step',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

