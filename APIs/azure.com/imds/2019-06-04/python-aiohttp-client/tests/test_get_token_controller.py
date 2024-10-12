# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.identity_error_response import IdentityErrorResponse
from openapi_server.models.identity_token_response import IdentityTokenResponse


pytestmark = pytest.mark.asyncio

async def test_identity_get_token(client):
    """Test case for identity_get_token

    
    """
    params = [('resource', 'resource_example'),
                    ('api-version', 'api_version_example'),
                    ('client_id', 'client_id_example'),
                    ('object_id', 'object_id_example'),
                    ('msi_res_id', 'msi_res_id_example'),
                    ('authority', 'authority_example'),
                    ('bypass_cache', 'bypass_cache_example')]
    headers = { 
        'Accept': 'application/json',
        'metadata': 'metadata_example',
    }
    response = await client.request(
        method='GET',
        path='/metadata/identity/oauth2/token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

