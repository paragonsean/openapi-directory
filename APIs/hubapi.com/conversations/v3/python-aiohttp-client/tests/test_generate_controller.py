# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.identification_token_generation_request import IdentificationTokenGenerationRequest
from openapi_server.models.identification_token_response import IdentificationTokenResponse


pytestmark = pytest.mark.asyncio

async def test_post_conversations_v3_visitor_identification_tokens_create_generate_token(client):
    """Test case for post_conversations_v3_visitor_identification_tokens_create_generate_token

    Generate a token
    """
    body = {"email":"visitor-email@example.com","firstName":"Gob","lastName":"Bluth"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/conversations/v3/visitor-identification/tokens/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

