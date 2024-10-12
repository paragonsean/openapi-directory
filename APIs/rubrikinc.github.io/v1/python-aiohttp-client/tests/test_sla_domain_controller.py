# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_async_request_status import BatchAsyncRequestStatus
from openapi_server.models.downloaded_snapshot_sla_assignment_info import DownloadedSnapshotSlaAssignmentInfo
from openapi_server.models.sla_domain_definition import SlaDomainDefinition
from openapi_server.models.sla_domain_patch_definition import SlaDomainPatchDefinition
from openapi_server.models.sla_domain_summary import SlaDomainSummary
from openapi_server.models.sla_domain_summary_list_response import SlaDomainSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_assign_sla_to_downloaded_snapshots(client):
    """Test case for assign_sla_to_downloaded_snapshots

    Assign retention SLA Domain to the downloaded snapshots of a single object
    """
    body = {"slaDomainId":"slaDomainId","snapshotIds":["snapshotIds","snapshotIds"],"objectId":"objectId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sla_domain/assign_to_downloaded_snapshots',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_sla_domain(client):
    """Test case for create_sla_domain

    Create SLA Domain
    """
    body = {"isRetentionLocked":True,"archivalSpecs":[{"archivalThreshold":5,"archivalTieringSpec":{"shouldTierExistingSnapshots":True,"minAccessibleDurationInSeconds":1,"coldStorageClass":"AzureArchive","isInstantTieringEnabled":True},"isPassthroughSupported":True,"locationName":"locationName","locationId":"locationId"},{"archivalThreshold":5,"archivalTieringSpec":{"shouldTierExistingSnapshots":True,"minAccessibleDurationInSeconds":1,"coldStorageClass":"AzureArchive","isInstantTieringEnabled":True},"isPassthroughSupported":True,"locationName":"locationName","locationId":"locationId"}],"name":"name","firstFullAllowedBackupWindows":[{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6},{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6}],"allowedBackupWindows":[{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6},{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6}],"localRetentionLimit":0,"frequencies":[{"retention":9,"frequency":9,"timeUnit":"timeUnit"},{"retention":9,"frequency":9,"timeUnit":"timeUnit"}],"replicationSpecs":[{"locationName":"locationName","replicationType":"REPLICATION_TO_CLUSTER","locationId":"locationId","retentionLimit":6,"logRetentionLimit":9},{"locationName":"locationName","replicationType":"REPLICATION_TO_CLUSTER","locationId":"locationId","retentionLimit":6,"logRetentionLimit":9}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sla_domain',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sla_domain(client):
    """Test case for delete_sla_domain

    Remove SLA Domain
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sla_domain/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sla_domain(client):
    """Test case for get_sla_domain

    Get SLA Domain details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sla_domain/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_sla_domain(client):
    """Test case for patch_sla_domain

    Patch SLA Domain
    """
    body = {"isRetentionLocked":True,"archivalSpecs":[{"archivalThreshold":5,"archivalTieringSpec":{"shouldTierExistingSnapshots":True,"minAccessibleDurationInSeconds":1,"coldStorageClass":"AzureArchive","isInstantTieringEnabled":True},"isPassthroughSupported":True,"locationName":"locationName","locationId":"locationId"},{"archivalThreshold":5,"archivalTieringSpec":{"shouldTierExistingSnapshots":True,"minAccessibleDurationInSeconds":1,"coldStorageClass":"AzureArchive","isInstantTieringEnabled":True},"isPassthroughSupported":True,"locationName":"locationName","locationId":"locationId"}],"name":"name","firstFullAllowedBackupWindows":[{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6},{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6}],"allowedBackupWindows":[{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6},{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6}],"localRetentionLimit":0,"frequencies":[{"retention":9,"frequency":9,"timeUnit":"timeUnit"},{"retention":9,"frequency":9,"timeUnit":"timeUnit"}],"replicationSpecs":[{"locationName":"locationName","replicationType":"REPLICATION_TO_CLUSTER","locationId":"locationId","retentionLimit":6,"logRetentionLimit":9},{"locationName":"locationName","replicationType":"REPLICATION_TO_CLUSTER","locationId":"locationId","retentionLimit":6,"logRetentionLimit":9}]}
    params = [('should_apply_to_existing_snapshots', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/sla_domain/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_sla_domain(client):
    """Test case for query_sla_domain

    Get list of SLA Domains
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example'),
                    ('name', 'name_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('data_sources', ['data_sources_example']),
                    ('snapshot_ids', ['snapshot_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sla_domain',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_sla_domain(client):
    """Test case for update_sla_domain

    Update SLA Domain
    """
    body = {"isRetentionLocked":True,"archivalSpecs":[{"archivalThreshold":5,"archivalTieringSpec":{"shouldTierExistingSnapshots":True,"minAccessibleDurationInSeconds":1,"coldStorageClass":"AzureArchive","isInstantTieringEnabled":True},"isPassthroughSupported":True,"locationName":"locationName","locationId":"locationId"},{"archivalThreshold":5,"archivalTieringSpec":{"shouldTierExistingSnapshots":True,"minAccessibleDurationInSeconds":1,"coldStorageClass":"AzureArchive","isInstantTieringEnabled":True},"isPassthroughSupported":True,"locationName":"locationName","locationId":"locationId"}],"name":"name","firstFullAllowedBackupWindows":[{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6},{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6}],"allowedBackupWindows":[{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6},{"startTimeAttributes":{"dayOfWeek":7,"hour":1,"minutes":4},"durationInHours":6}],"localRetentionLimit":0,"frequencies":[{"retention":9,"frequency":9,"timeUnit":"timeUnit"},{"retention":9,"frequency":9,"timeUnit":"timeUnit"}],"replicationSpecs":[{"locationName":"locationName","replicationType":"REPLICATION_TO_CLUSTER","locationId":"locationId","retentionLimit":6,"logRetentionLimit":9},{"locationName":"locationName","replicationType":"REPLICATION_TO_CLUSTER","locationId":"locationId","retentionLimit":6,"logRetentionLimit":9}]}
    params = [('should_apply_to_existing_snapshots', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sla_domain/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

