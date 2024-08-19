# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_installation200_response import DeleteInstallation200Response


pytestmark = pytest.mark.asyncio

async def test_delete_installation(client):
    """Test case for delete_installation

    アプリストアアプリのアンインストール
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/appstore/v1/installation.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

