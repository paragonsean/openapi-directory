# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_books200_response import GetBooks200Response


pytestmark = pytest.mark.asyncio

async def test_get_books(client):
    """Test case for get_books

    List all books
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/books',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

