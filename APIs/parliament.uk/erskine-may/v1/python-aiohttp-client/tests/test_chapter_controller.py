# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erskine_may_chapter_overview import ErskineMayChapterOverview


pytestmark = pytest.mark.asyncio

async def test_api_chapter_chapter_number_get(client):
    """Test case for api_chapter_chapter_number_get

    Returns a single chapter overview by chapter number.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Chapter/{chapter_number}'.format(chapter_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

