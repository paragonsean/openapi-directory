# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_seo_latest_rankings(client):
    """Test case for seo_latest_rankings

    SEO Latest Rankings
    """
    params = [('', '')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/seo/ranking/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

