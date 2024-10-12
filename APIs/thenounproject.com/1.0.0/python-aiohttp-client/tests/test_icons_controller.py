# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_icons_by_term(client):
    """Test case for get_icons_by_term

    Get icons by term
    """
    params = [('limit_to_public_domain', 56),
                    ('limit', 56),
                    ('offset', 56),
                    ('page', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/icons/{term}'.format(term='term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_icons(client):
    """Test case for get_recent_icons

    Get recent icons
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('page', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/icons/recent_uploads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

