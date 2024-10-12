# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_failed import AuthFailed
from openapi_server.models.rate_limit import RateLimit
from openapi_server.models.remove_bg_json import RemoveBgJson
from openapi_server.models.remove_bg_json_response import RemoveBgJsonResponse
from openapi_server.models.remove_bg_multipart import RemoveBgMultipart
from openapi_server.models.removebg_post400_response import RemovebgPost400Response
from openapi_server.models.removebg_post402_response import RemovebgPost402Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_removebg_post(client):
    """Test case for removebg_post

    Remove the background of an image
    """
    body = {"image_file_b64":"","bg_image_url":"","image_url":"https://www.remove.bg/example-hd.jpg","add_shadow":False,"format":"auto","scale":"original","type_level":"1","crop_margin":"0","type":"auto","roi":"0% 0% 100% 100%","bg_color":"","channels":"rgba","size":"preview","semitransparency":True,"position":"original","crop":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/removebg',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

