# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.file import File


pytestmark = pytest.mark.asyncio

async def test_download_file_by_id(client):
    """Test case for download_file_by_id

    Get the content of a File
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/vaults/{vault_uuid}/items/{item_uuid}/files/{file_uuid}/content'.format(vault_uuid='vault_uuid_example', item_uuid='item_uuid_example', file_uuid='file_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_details_of_file_by_id(client):
    """Test case for get_details_of_file_by_id

    Get the details of a File
    """
    params = [('inline_files', true)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/vaults/{vault_uuid}/items/{item_uuid}/files/{file_uuid}'.format(vault_uuid='vault_uuid_example', item_uuid='item_uuid_example', file_uuid='file_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_files(client):
    """Test case for get_item_files

    Get all the files inside an Item
    """
    params = [('inline_files', true)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/vaults/{vault_uuid}/items/{item_uuid}/files'.format(vault_uuid='vault_uuid_example', item_uuid='item_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

