# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.async_event_get200_response import AsyncEventGet200Response


pytestmark = pytest.mark.asyncio

async def test_async_event_get(client):
    """Test case for async_event_get

    
    """
    params = [('last_id', 'last_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/async_event/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

