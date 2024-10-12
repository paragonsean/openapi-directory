# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_client_id_get200_response import ClientClientIdGet200Response
from openapi_server.models.client_post_request import ClientPostRequest


pytestmark = pytest.mark.asyncio

async def test_client_client_id_get(client):
    """Test case for client_client_id_get

    Get a Client
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/client/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_client_id_token_kind_get(client):
    """Test case for client_client_id_token_kind_get

    Get a Client Token
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/client/{client_id}/token/{kind}'.format(client_id='client_id_example', kind='kind_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_post(client):
    """Test case for client_post

    Create a Client Selfie
    """
    body = openapi_server.ClientPostRequest()
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/client',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

