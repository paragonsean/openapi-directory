# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.explain_url import ExplainUrl
from openapi_server.models.explain_url_write import ExplainUrlWrite


pytestmark = pytest.mark.asyncio

async def test_get_explain_url_item(client):
    """Test case for get_explain_url_item

    Retrieves a ExplainUrl resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/explain-urls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_explain_url_collection(client):
    """Test case for post_explain_url_collection

    Creates a ExplainUrl resource.
    """
    explain_url = openapi_server.ExplainUrlWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/explain-urls',
        headers=headers,
        json=explain_url,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

