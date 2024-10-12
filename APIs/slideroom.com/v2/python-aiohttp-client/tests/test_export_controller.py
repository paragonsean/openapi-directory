# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.export_result_v2 import ExportResultV2


pytestmark = pytest.mark.asyncio

async def test_export_get_v2(client):
    """Test case for export_get_v2

    Gets the status/result of a requested export.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/export/{token}'.format(token=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

