# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model_schema import ModelSchema


pytestmark = pytest.mark.asyncio

async def test_create_or_update_profile_schema(client):
    """Test case for create_or_update_profile_schema

    Create or update profile schema
    """
    body = openapi_server.ModelSchema()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/storage/profile-system/profiles/schema',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

