# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fileset_template_create import FilesetTemplateCreate
from openapi_server.models.fileset_template_detail import FilesetTemplateDetail
from openapi_server.models.fileset_template_detail_list_response import FilesetTemplateDetailListResponse
from openapi_server.models.fileset_template_patch import FilesetTemplatePatch


pytestmark = pytest.mark.asyncio

async def test_create_fileset_template(client):
    """Test case for create_fileset_template

    Create a fileset template
    """
    body = {"excludes":["excludes","excludes"],"operatingSystemType":"UnixLike","preBackupScript":"preBackupScript","backupScriptTimeout":0,"includes":["includes","includes"],"backupScriptErrorHandling":"backupScriptErrorHandling","isArrayEnabled":True,"shareType":"NFS","allowBackupNetworkMounts":True,"exceptions":["exceptions","exceptions"],"allowBackupHiddenFoldersInNetworkMounts":True,"postBackupScript":"postBackupScript","useWindowsVss":True,"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/fileset_template',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_fileset_template(client):
    """Test case for delete_fileset_template

    Delete a fileset template
    """
    params = [('preserve_snapshots', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/fileset_template/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fileset_template(client):
    """Test case for get_fileset_template

    Get information for a fileset template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/fileset_template/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_fileset_template(client):
    """Test case for query_fileset_template

    Get summary information for all fileset templates
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('operating_system_type', 'operating_system_type_example'),
                    ('share_type', 'share_type_example'),
                    ('name', 'name_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/fileset_template',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_fileset_template(client):
    """Test case for update_fileset_template

    Modify a fileset template
    """
    body = {"excludes":["excludes","excludes"],"operatingSystemType":"UnixLike","preBackupScript":"preBackupScript","backupScriptTimeout":0,"includes":["includes","includes"],"backupScriptErrorHandling":"backupScriptErrorHandling","shareType":"NFS","allowBackupNetworkMounts":True,"exceptions":["exceptions","exceptions"],"allowBackupHiddenFoldersInNetworkMounts":True,"postBackupScript":"postBackupScript","useWindowsVss":True,"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/fileset_template/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

