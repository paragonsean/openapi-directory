# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.slide_slide_masters import SlideSlideMasters


pytestmark = pytest.mark.asyncio

async def test_slides_slidemasters_get_id(client):
    """Test case for slides_slidemasters_get_id

    SlideMasters: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Slides/SlideMasters/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

