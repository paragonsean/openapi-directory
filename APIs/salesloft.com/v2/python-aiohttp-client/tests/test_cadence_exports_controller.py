# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cadence_export import CadenceExport


pytestmark = pytest.mark.asyncio

async def test_v2_cadence_exports_id_json_get(client):
    """Test case for v2_cadence_exports_id_json_get

    Export a cadence
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/cadence_exports/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

