# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.theme_background_fills import ThemeBackgroundFills


pytestmark = pytest.mark.asyncio

async def test_themes_backgroundfills_get_id(client):
    """Test case for themes_backgroundfills_get_id

    BackgroundFills: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Themes/BackgroundFills/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

