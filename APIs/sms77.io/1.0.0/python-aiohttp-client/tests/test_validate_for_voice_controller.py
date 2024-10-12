# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.validate_for_voice200_response import ValidateForVoice200Response


pytestmark = pytest.mark.asyncio

async def test_validate_for_voice(client):
    """Test case for validate_for_voice

    
    """
    params = [('number', 'number_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/validate_for_voice',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

