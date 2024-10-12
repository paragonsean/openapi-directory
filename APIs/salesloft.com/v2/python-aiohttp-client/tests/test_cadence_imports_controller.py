# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cadence_import import CadenceImport


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_cadence_imports_json_post(client):
    """Test case for v2_cadence_imports_json_post

    Import cadences from JSON
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'cadence_content': None,
        'settings': None,
        'sharing_settings': None
        }
    response = await client.request(
        method='POST',
        path='/v2/cadence_imports.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

