# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_subject(client):
    """Test case for get_subject

    Explore details about a given subject node
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/id/{identifier}'.format(identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

