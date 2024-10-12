# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.matching_url_read import MatchingUrlRead
from openapi_server.models.matching_url_write import MatchingUrlWrite


pytestmark = pytest.mark.asyncio

async def test_get_matching_url_item(client):
    """Test case for get_matching_url_item

    Retrieves a MatchingUrl resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/matching-urls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_matching_url_collection(client):
    """Test case for post_matching_url_collection

    Creates a MatchingUrl resource.
    """
    matching_url = openapi_server.MatchingUrlWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/matching-urls',
        headers=headers,
        json=matching_url,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

