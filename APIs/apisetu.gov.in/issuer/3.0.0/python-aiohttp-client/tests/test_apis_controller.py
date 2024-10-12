# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pull_doc_request import PullDocRequest
from openapi_server.models.pull_doc_response import PullDocResponse
from openapi_server.models.pull_uri_request import PullURIRequest
from openapi_server.models.pull_uri_response import PullURIResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_pull_doc(client):
    """Test case for pull_doc

    Pull Doc Request API.
    """
    body = openapi_server.PullDocRequest()
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'application/xml',
        'content_type': 'content_type_example',
        'x_digilocker_hmac': 'x_digilocker_hmac_example',
    }
    response = await client.request(
        method='POST',
        path='/Your Pull DOC Request API Path',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_pull_uri(client):
    """Test case for pull_uri

    Pull URI Request API .
    """
    body = openapi_server.PullURIRequest()
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'application/xml',
        'content_type': 'content_type_example',
        'x_digilocker_hmac': 'x_digilocker_hmac_example',
    }
    response = await client.request(
        method='POST',
        path='/Your Pull URI Request API Path',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

