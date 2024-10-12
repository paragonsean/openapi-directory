# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.theme_fills import ThemeFills


pytestmark = pytest.mark.asyncio

async def test_themes_fills_get_id(client):
    """Test case for themes_fills_get_id

    Fills: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/Fills/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

