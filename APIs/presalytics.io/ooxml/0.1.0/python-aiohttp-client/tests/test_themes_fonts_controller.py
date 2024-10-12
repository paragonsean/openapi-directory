# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.theme_fonts import ThemeFonts


pytestmark = pytest.mark.asyncio

async def test_themes_fonts_get_id(client):
    """Test case for themes_fonts_get_id

    Fonts: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/Fonts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

