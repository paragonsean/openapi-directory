# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError


pytestmark = pytest.mark.asyncio

async def test_extractor_extractor_id_cancel_post(client):
    """Test case for extractor_extractor_id_cancel_post

    Cancel an existing crawl.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/extractor/{extractor_id}/cancel'.format(extractor_id='extractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extractor_extractor_id_start_post(client):
    """Test case for extractor_extractor_id_start_post

    Launch a crawl from an extractor that a user owns.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/extractor/{extractor_id}/start'.format(extractor_id='extractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

