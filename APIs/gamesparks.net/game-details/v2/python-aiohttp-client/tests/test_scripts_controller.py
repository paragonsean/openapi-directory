# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.message_model import MessageModel
from openapi_server.models.scripts_difference_list_model import ScriptsDifferenceListModel
from openapi_server.models.snapshot_script_version_list_model import SnapshotScriptVersionListModel


pytestmark = pytest.mark.asyncio

async def test_export_zip_using_get(client):
    """Test case for export_zip_using_get

    exportZip
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/scripts/export'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_script_differences_using_get(client):
    """Test case for get_script_differences_using_get

    getScriptDifferences
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/scripts/differences/{snapshot_id1}/{snapshot_id2}'.format(api_key='api_key_example', snapshot_id1='snapshot_id1_example', snapshot_id2='snapshot_id2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_script_versions_using_get(client):
    """Test case for get_script_versions_using_get

    getScriptVersions
    """
    params = [('pageSize', 100)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/scripts/versions/{page}'.format(api_key='api_key_example', page=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_script_versions_using_get1(client):
    """Test case for get_script_versions_using_get1

    getScriptVersions
    """
    params = [('pageSize', 100)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/scripts/versions'.format(api_key='api_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_import_accept_using_post(client):
    """Test case for import_accept_using_post

    importAccept
    """
    params = [('body', 'body_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/scripts/import/accept'.format(api_key='api_key_example'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_import_zip_using_post(client):
    """Test case for import_zip_using_post

    importZip
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/scripts/import/preview'.format(api_key='api_key_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

