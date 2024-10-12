# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.folder_data import FolderData


pytestmark = pytest.mark.asyncio

async def test_folder_get(client):
    """Test case for folder_get

    Gets the Values for a folder or a meter
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Folder/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

