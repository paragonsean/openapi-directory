# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.theme_effect_map import ThemeEffectMap


pytestmark = pytest.mark.asyncio

async def test_themes_effectmap_get_id(client):
    """Test case for themes_effectmap_get_id

    EffectMap: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/EffectMap/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

