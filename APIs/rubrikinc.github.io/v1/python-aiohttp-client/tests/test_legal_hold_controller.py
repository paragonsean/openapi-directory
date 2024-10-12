# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apply_legal_hold_definition import ApplyLegalHoldDefinition
from openapi_server.models.dissolve_legal_hold_definition import DissolveLegalHoldDefinition
from openapi_server.models.dissolve_legal_hold_response import DissolveLegalHoldResponse
from openapi_server.models.legal_hold_summary import LegalHoldSummary
from openapi_server.models.legal_hold_summary_list_response import LegalHoldSummaryListResponse
from openapi_server.models.object_hold_summary_list_response import ObjectHoldSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_apply_legal_hold(client):
    """Test case for apply_legal_hold

    Apply a Legal Hold
    """
    body = {"snapshotId":"snapshotId","holdConfig":{"isHoldInPlace":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/legal_hold/snapshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dissolve_legal_hold_snapshots(client):
    """Test case for dissolve_legal_hold_snapshots

    Dissolve a collection of snapshots of specified data source from Legal Hold
    """
    body = {"snapshotIds":["snapshotIds","snapshotIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/legal_hold/object/{id}/dissolve'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_legal_hold_objects(client):
    """Test case for get_legal_hold_objects

    Get objects part of Legal Hold
    """
    params = [('object_id', 'object_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('object_name', 'object_name_example'),
                    ('object_type', 'object_type_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', asc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/legal_hold/object',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_legal_hold(client):
    """Test case for query_legal_hold

    Get snasphots held under legal hold
    """
    params = [('object_id', 'object_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('object_name', 'object_name_example'),
                    ('object_type', 'object_type_example'),
                    ('before_date', '2013-10-20T19:20:30+01:00'),
                    ('after_date', '2013-10-20T19:20:30+01:00'),
                    ('placed_on_hold_before_date', '2013-10-20T19:20:30+01:00'),
                    ('placed_on_hold_after_date', '2013-10-20T19:20:30+01:00'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', asc),
                    ('snapshot_type', 'snapshot_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/legal_hold/snapshot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

