# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.browse_response_list_response import BrowseResponseListResponse
from openapi_server.models.hdfs_create import HdfsCreate
from openapi_server.models.hdfs_detail import HdfsDetail
from openapi_server.models.hdfs_export_file_job_config import HdfsExportFileJobConfig
from openapi_server.models.hdfs_restore_file_job_config import HdfsRestoreFileJobConfig
from openapi_server.models.hdfs_snapshot_detail import HdfsSnapshotDetail
from openapi_server.models.hdfs_summary_list_response import HdfsSummaryListResponse
from openapi_server.models.hdfs_update import HdfsUpdate
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.search_response_list_response import SearchResponseListResponse


pytestmark = pytest.mark.asyncio

async def test_browse_hdfs_snapshot(client):
    """Test case for browse_hdfs_snapshot

    Lists all files and directories in a given path
    """
    params = [('path', 'path_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs/snapshot/{id}/browse'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_hdfs(client):
    """Test case for create_hdfs

    Create one HDFS directory for a host
    """
    body = {"hostId":"hostId","templateId":"templateId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hdfs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_hdfs_backup_job(client):
    """Test case for create_hdfs_backup_job

    Initiate an on-demand backup for a HDFS directory
    """
    body = {"slaId":"slaId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hdfs/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_hdfs_export_file_job(client):
    """Test case for create_hdfs_export_file_job

    Create export job
    """
    body = {"sourceDir":"sourceDir","destinationDir":"destinationDir","hostId":"hostId","shouldIgnoreErrors":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hdfs/snapshot/{id}/export_file'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_hdfs_restore_file_job(client):
    """Test case for create_hdfs_restore_file_job

    Create restore job
    """
    body = {"sourceDir":"sourceDir","destinationDir":"destinationDir","shouldIgnoreErrors":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hdfs/snapshot/{id}/restore_file'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hdfs(client):
    """Test case for delete_hdfs

    Delete a HDFS directory
    """
    params = [('preserve_snapshots', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/hdfs/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hdfs_snapshot(client):
    """Test case for delete_hdfs_snapshot

    Delete a HDFS directory snapshot
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/hdfs/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hdfs_snapshots(client):
    """Test case for delete_hdfs_snapshots

    Delete all snapshots of a HDFS directory
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/hdfs/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hdfs(client):
    """Test case for get_hdfs

    Get information for a single HDFS directory
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hdfs_async_request_status(client):
    """Test case for get_hdfs_async_request_status

    Get details about an asynchronous request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hdfs_snapshot(client):
    """Test case for get_hdfs_snapshot

    Get information for a HDFS directory snapshot
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_missed_hdfs_snapshots(client):
    """Test case for get_missed_hdfs_snapshots

    Get missed snapshots for a HDFS directory
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs/{id}/missed_snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_hdfs(client):
    """Test case for query_hdfs

    Get summary information for all HDFS directories
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('host_id', 'host_id_example'),
                    ('is_relic', True),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('template_id', 'template_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('host_name', 'host_name_example'),
                    ('sort_by', name),
                    ('sort_order', asc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_hdfs(client):
    """Test case for search_hdfs

    Search for a file within the HDFS directory
    """
    params = [('path', 'path_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hdfs/{id}/search'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_hdfs(client):
    """Test case for update_hdfs

    Update a HDFS directory
    """
    body = {"configuredSlaDomainId":"configuredSlaDomainId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/hdfs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

