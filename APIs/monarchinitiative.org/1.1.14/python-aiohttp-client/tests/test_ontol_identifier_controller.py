# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_ontol_identifier_resource(client):
    """Test case for get_ontol_identifier_resource

    Fetches a map from CURIEs/IDs to labels
    """
    params = [('label', ['label_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/ontol/identifier/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_ontol_identifier_resource(client):
    """Test case for post_ontol_identifier_resource

    Fetches a map from CURIEs/IDs to labels
    """
    params = [('label', ['label_example'])]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/ontol/identifier/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

