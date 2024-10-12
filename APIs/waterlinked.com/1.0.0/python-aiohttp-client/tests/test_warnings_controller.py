# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.waterlinked_operation_response import WaterlinkedOperationResponse
from openapi_server.models.wl_warning import WlWarning


pytestmark = pytest.mark.asyncio

async def test_warnings_get(client):
    """Test case for warnings_get

    Get warnings
    """
    headers = { 
        'Accept': 'application/vnd.wl.warning+json; type=collection',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/warnings/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

