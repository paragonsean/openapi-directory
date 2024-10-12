# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_delete_object_snapshots_config import BulkDeleteObjectSnapshotsConfig
from openapi_server.models.bulk_delete_snapshots_config import BulkDeleteSnapshotsConfig
from openapi_server.models.expired_custom_retention_snapshots import ExpiredCustomRetentionSnapshots
from openapi_server.models.request_failed_exception import RequestFailedException


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_snapshots(client):
    """Test case for bulk_delete_snapshots

    Bulk delete all snapshots for the given objects
    """
    body = {"objectIds":["objectIds","objectIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/data_source/snapshot/bulk_delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_snapshots_for_object(client):
    """Test case for bulk_delete_snapshots_for_object

    Bulk delete specified snapshots for the given object
    """
    body = {"locationId":"locationId","snapshotIds":["snapshotIds","snapshotIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/data_source/{id}/snapshot/bulk_delete'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expired_custom_retention_snapshots(client):
    """Test case for expired_custom_retention_snapshots

    Returns a list of snapshots that have expired according to their snapshot-level SLA Domain assignments 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data_source/{id}/expired_custom_retention_snapshots'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

