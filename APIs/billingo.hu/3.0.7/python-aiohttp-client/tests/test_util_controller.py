# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.id import Id
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_id(client):
    """Test case for get_id

    Convert legacy ID to v3 ID.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/utils/convert-legacy-id/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

