# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversion_parameters import ConversionParameters


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api2_convert_post(client):
    """Test case for api2_convert_post

    Performs a html to pdf conversion
    """
    parameters = {"margin_bottom":5,"page_orientation":"Portrait","margin_top":5,"base_url":"https://selectpdf.com","html":"<b>test html string</b>","key":"d290f1ee-6c54-4b01-90e6-d701748f0851","margin_right":5,"url":"https://selectpdf.com","margin_left":5,"page_size":"A4"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api2/convert',
        headers=headers,
        json=parameters,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

