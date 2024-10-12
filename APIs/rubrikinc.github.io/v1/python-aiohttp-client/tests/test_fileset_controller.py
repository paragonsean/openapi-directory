# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.browse_response_list_response import BrowseResponseListResponse
from openapi_server.models.fileset_create import FilesetCreate
from openapi_server.models.fileset_detail import FilesetDetail
from openapi_server.models.fileset_download_file_job_config import FilesetDownloadFileJobConfig
from openapi_server.models.fileset_export_file_job_config import FilesetExportFileJobConfig
from openapi_server.models.fileset_restore_file_job_config import FilesetRestoreFileJobConfig
from openapi_server.models.fileset_snapshot_detail import FilesetSnapshotDetail
from openapi_server.models.fileset_summary_list_response import FilesetSummaryListResponse
from openapi_server.models.fileset_update import FilesetUpdate
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.search_response_list_response import SearchResponseListResponse


pytestmark = pytest.mark.asyncio

async def test_browse_fileset_snapshot(client):
    """Test case for browse_fileset_snapshot

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
        path='/api/v1/fileset/snapshot/{id}/browse'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_download_fileset_snapshot_from_cloud(client):
    """Test case for create_download_fileset_snapshot_from_cloud

    Create a download fileset snapshot from archival request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/fileset/snapshot/{id}/download'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_fileset(client):
    """Test case for create_fileset

    Create one fileset for a host
    """
    body = {"snapMirrorLabelForIncrementalBackup":"snapMirrorLabelForIncrementalBackup","arraySpec":{"proxyHostId":"proxyHostId"},"enableSymlinkResolution":True,"failoverClusterAppId":"failoverClusterAppId","hostId":"hostId","shareId":"shareId","isPassthrough":True,"snapMirrorLabelForFullBackup":"snapMirrorLabelForFullBackup","templateId":"templateId","enableHardlinkSupport":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/fileset',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_fileset_backup_job(client):
    """Test case for create_fileset_backup_job

    Initiate an on-demand backup for a fileset
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
        path='/api/v1/fileset/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_fileset_download_file_job(client):
    """Test case for create_fileset_download_file_job

    Create a file download job from a fileset backup
    """
    body = {"sourceDir":"sourceDir","legalHoldDownloadConfig":{"isLegalHoldDownload":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/fileset/snapshot/{id}/download_file'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_fileset_export_file_job(client):
    """Test case for create_fileset_export_file_job

    Create export job
    """
    body = {"sourceDir":"sourceDir","destinationDir":"destinationDir","hostId":"hostId","shareId":"shareId","ignoreErrors":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/fileset/snapshot/{id}/export_file'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_fileset_restore_file_job(client):
    """Test case for create_fileset_restore_file_job

    Create restore job
    """
    body = {"sourceDir":"sourceDir","destinationDir":"destinationDir","ignoreErrors":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/fileset/snapshot/{id}/restore_file'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_fileset(client):
    """Test case for delete_fileset

    Delete a fileset
    """
    params = [('preserve_snapshots', True)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/fileset/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_fileset_snapshot(client):
    """Test case for delete_fileset_snapshot

    Delete a fileset snapshot
    """
    params = [('location', 'location_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/fileset/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_fileset_snapshots(client):
    """Test case for delete_fileset_snapshots

    Delete all snapshots of a fileset
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/fileset/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fileset(client):
    """Test case for get_fileset

    Get information for a single fileset
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/fileset/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fileset_async_request_status(client):
    """Test case for get_fileset_async_request_status

    Get details about an async request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/fileset/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fileset_snapshot(client):
    """Test case for get_fileset_snapshot

    Get information for a fileset snapshot
    """
    params = [('verbose', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/fileset/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_missed_fileset_snapshots(client):
    """Test case for get_missed_fileset_snapshots

    Get missed snapshots for a fileset
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/fileset/{id}/missed_snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_fileset(client):
    """Test case for query_fileset

    Get summary information for all filesets
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('host_id', 'host_id_example'),
                    ('share_id', 'share_id_example'),
                    ('is_relic', True),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('template_id', 'template_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('host_name', 'host_name_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/fileset',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_fileset(client):
    """Test case for search_fileset

    Search for a file within the fileset
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
        path='/api/v1/fileset/{id}/search'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_fileset(client):
    """Test case for update_fileset

    Update a Fileset
    """
    body = {"forceFullPartitionIds":[0,0],"snapMirrorLabelForIncrementalBackup":"snapMirrorLabelForIncrementalBackup","forceFull":True,"configuredSlaDomainId":"configuredSlaDomainId","snapMirrorLabelForFullBackup":"snapMirrorLabelForFullBackup"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/fileset/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

