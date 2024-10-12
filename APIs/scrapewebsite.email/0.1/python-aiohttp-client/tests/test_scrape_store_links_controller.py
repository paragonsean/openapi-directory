# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_g_etv1_scrape_store_links_format(client):
    """Test case for g_etv1_scrape_store_links_format

    Attempts to grab the google store url or the ios store url for a site, after searching through the site.
    """
    params = [('website', 'website_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/scrape_store_links.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

