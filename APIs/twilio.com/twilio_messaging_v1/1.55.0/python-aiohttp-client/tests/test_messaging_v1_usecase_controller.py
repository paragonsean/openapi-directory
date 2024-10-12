# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_usecase import MessagingV1Usecase


pytestmark = pytest.mark.asyncio

async def test_fetch_usecase(client):
    """Test case for fetch_usecase

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/Usecases',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

