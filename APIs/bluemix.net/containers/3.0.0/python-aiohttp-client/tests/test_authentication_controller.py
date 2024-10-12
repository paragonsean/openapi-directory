# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_refresh import CertificateRefresh


pytestmark = pytest.mark.asyncio

async def test_tlskey_get(client):
    """Test case for tlskey_get

    Retrieve the TLS Certificate
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/tlskey',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tlskey_refresh_put(client):
    """Test case for tlskey_refresh_put

    Refresh the TLS Certificate
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='PUT',
        path='/v3/tlskey/refresh',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

