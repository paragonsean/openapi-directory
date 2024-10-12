# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_showtime_searchall_read(client):
    """Test case for showtime_searchall_read

    Return showtime search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/showtime/searchall/{param}'.format(param='param_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

