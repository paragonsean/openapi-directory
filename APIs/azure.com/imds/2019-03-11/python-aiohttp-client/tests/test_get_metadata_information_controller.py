# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.identity_error_response import IdentityErrorResponse
from openapi_server.models.identity_info_response import IdentityInfoResponse


pytestmark = pytest.mark.asyncio

async def test_identity_get_info(client):
    """Test case for identity_get_info

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'metadata': 'metadata_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/metadata/identity/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

