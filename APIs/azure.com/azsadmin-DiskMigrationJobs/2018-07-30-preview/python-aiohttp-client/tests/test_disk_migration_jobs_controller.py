# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.disk_migration_jobs_create_request_inner import DiskMigrationJobsCreateRequestInner
from openapi_server.models.disk_migration_jobs_get200_response import DiskMigrationJobsGet200Response
from openapi_server.models.disk_migration_jobs_list200_response import DiskMigrationJobsList200Response


pytestmark = pytest.mark.asyncio

async def test_disk_migration_jobs_cancel(client):
    """Test case for disk_migration_jobs_cancel

    
    """
    params = [('api-version', '2018-07-30-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migration_id}/Cancel'.format(subscription_id='subscription_id_example', location='location_example', migration_id='migration_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disk_migration_jobs_create(client):
    """Test case for disk_migration_jobs_create

    
    """
    disks = [openapi_server.DiskMigrationJobsCreateRequestInner()]
    params = [('targetShare', 'target_share_example'),
                    ('api-version', '2018-07-30-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migration_id}'.format(subscription_id='subscription_id_example', location='location_example', migration_id='migration_id_example'),
        headers=headers,
        json=disks,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disk_migration_jobs_get(client):
    """Test case for disk_migration_jobs_get

    
    """
    params = [('api-version', '2018-07-30-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migration_id}'.format(subscription_id='subscription_id_example', location='location_example', migration_id='migration_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disk_migration_jobs_list(client):
    """Test case for disk_migration_jobs_list

    
    """
    params = [('status', 'status_example'),
                    ('api-version', '2018-07-30-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

