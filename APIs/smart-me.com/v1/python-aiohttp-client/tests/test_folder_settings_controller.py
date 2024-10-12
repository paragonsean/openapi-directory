# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.folder_menu_item import FolderMenuItem
from openapi_server.models.folder_settings import FolderSettings


pytestmark = pytest.mark.asyncio

async def test_folder_settings_delete(client):
    """Test case for folder_settings_delete

    Deletes a folder
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/folder/settings/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_folder_settings_get(client):
    """Test case for folder_settings_get

    Gets the settings of a folder or meter
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/folder/settings/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_folder_settings_post(client):
    """Test case for folder_settings_post

    Add or edit a folder or a meter. To add a new folder use and empty ID
    """
    body = {"Description":"Description","SerialNumber":0,"ValueCorrectionParentFolder":1.4658129805029452,"VisualizationName":"VisualizationName","Enable":True,"UseableForVirtualBillingMeters":True,"ValueCorrection":6.027456183070403,"ParentFolderId":"ParentFolderId","FolderType":"Folder","Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/folder/settings/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

