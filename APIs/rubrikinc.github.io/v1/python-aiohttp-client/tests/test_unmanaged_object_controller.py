# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.bulk_tier_snapshots_config import BulkTierSnapshotsConfig
from openapi_server.models.managed_object_pending_sla_info import ManagedObjectPendingSlaInfo
from openapi_server.models.snapshot_summary_list_response import SnapshotSummaryListResponse
from openapi_server.models.unmanaged_object_details_list_response import UnmanagedObjectDetailsListResponse
from openapi_server.models.unmanaged_object_sla_assignment_info import UnmanagedObjectSlaAssignmentInfo
from openapi_server.models.unmanaged_object_summary_list_response import UnmanagedObjectSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_assign_to_retention_sla_async(client):
    """Test case for assign_to_retention_sla_async

    Assign relic/unmanaged entities to an SLA Domain for managing retention asynchronously
    """
    body = {"shouldApplyToNonPolicySnapshots":True,"slaDomainId":"slaDomainId","managedIds":["managedIds","managedIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/unmanaged_object/assign_retention_sla',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_tier_existing_snapshots(client):
    """Test case for bulk_tier_existing_snapshots

    Bulk tier existing snapshots to cold storage
    """
    body = {"locationId":"locationId","objectIds":["objectIds","objectIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/unmanaged_object/snapshot/bulk_archive_tier',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_unmanaged_object_snapshots_v1(client):
    """Test case for query_unmanaged_object_snapshots_v1

    Get summary of all the snapshots for a given object
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('search_value', 'search_value_example'),
                    ('snapshot_type', 'snapshot_type_example'),
                    ('before_date', '2013-10-20T19:20:30+01:00'),
                    ('after_date', '2013-10-20T19:20:30+01:00'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/unmanaged_object/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_unmanaged_object_v1(client):
    """Test case for query_unmanaged_object_v1

    Get summary of all the objects with unmanaged snapshots
    """
    params = [('limit', 56),
                    ('after_id', 'after_id_example'),
                    ('search_value', 'search_value_example'),
                    ('unmanaged_status', 'unmanaged_status_example'),
                    ('object_type', 'object_type_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/unmanaged_object',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_unmanaged_reader_object(client):
    """Test case for query_unmanaged_reader_object

    Get summary of all unmanaged reader objects
    """
    params = [('limit', 56),
                    ('after_id', 'after_id_example'),
                    ('object_name', 'object_name_example'),
                    ('unmanaged_status', 'unmanaged_status_example'),
                    ('object_type', 'object_type_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/unmanaged_object/reader_object',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

