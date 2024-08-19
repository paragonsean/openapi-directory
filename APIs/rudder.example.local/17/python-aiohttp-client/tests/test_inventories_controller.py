# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.file_watcher_restart200_response import FileWatcherRestart200Response
from openapi_server.models.file_watcher_start200_response import FileWatcherStart200Response
from openapi_server.models.file_watcher_stop200_response import FileWatcherStop200Response
from openapi_server.models.queue_information200_response import QueueInformation200Response
from openapi_server.models.upload_inventory200_response import UploadInventory200Response


pytestmark = pytest.mark.asyncio

async def test_file_watcher_restart(client):
    """Test case for file_watcher_restart

    Restart inventory watcher
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/inventories/watcher/restart',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_watcher_start(client):
    """Test case for file_watcher_start

    Start inventory watcher
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/inventories/watcher/start',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_watcher_stop(client):
    """Test case for file_watcher_stop

    Stop inventory watcher
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/inventories/watcher/stop',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queue_information(client):
    """Test case for queue_information

    Get information about inventory processing queue
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/inventories/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_inventory(client):
    """Test case for upload_inventory

    Upload an inventory for processing
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'API-Tokens': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('signature', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/inventories/upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

