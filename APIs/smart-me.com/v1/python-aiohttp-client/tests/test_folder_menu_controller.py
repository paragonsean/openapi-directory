# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.folder_menu_configuration import FolderMenuConfiguration


pytestmark = pytest.mark.asyncio

async def test_folder_menu_get(client):
    """Test case for folder_menu_get

    Gets the folder menu items (each item might contain child items)
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/FolderMenu',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_folder_menu_post(client):
    """Test case for folder_menu_post

    Creates and updates the folder menu items
    """
    body = {"BrowserUtcTime":"BrowserUtcTime","BrowserTimeZoneName":"BrowserTimeZoneName","Items":[{"Description":"Description","MeterSerialNumber":"MeterSerialNumber","AutoExportSettings":{"ExportFormat":"ExportFormat","ExportInterval":"NoExport","MeterPointId":"MeterPointId","UploadType":"UploadType"},"UserId":"UserId","Children":[null,null],"Icon":"Icon","Id":"Id","FolderType":"Folder","Name":"Name"},{"Description":"Description","MeterSerialNumber":"MeterSerialNumber","AutoExportSettings":{"ExportFormat":"ExportFormat","ExportInterval":"NoExport","MeterPointId":"MeterPointId","UploadType":"UploadType"},"UserId":"UserId","Children":[null,null],"Icon":"Icon","Id":"Id","FolderType":"Folder","Name":"Name"}]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/FolderMenu',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

