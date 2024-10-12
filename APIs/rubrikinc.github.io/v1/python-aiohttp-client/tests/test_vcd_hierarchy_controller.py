# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vcd_hierarchy_object_summary import VcdHierarchyObjectSummary
from openapi_server.models.vcd_hierarchy_object_summary_list_response import VcdHierarchyObjectSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_get_vcd_hierarchy_children_v1(client):
    """Test case for get_vcd_hierarchy_children_v1

    Get immediate descendant objects
    """
    params = [('sort_by', 'sort_by_example'),
                    ('sort_order', asc),
                    ('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('is_relic', True),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('object_type', 'object_type_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/hierarchy/{id}/children'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcd_hierarchy_descendants_v1(client):
    """Test case for get_vcd_hierarchy_descendants_v1

    Get list of descendant objects
    """
    params = [('sort_by', 'sort_by_example'),
                    ('sort_order', asc),
                    ('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('is_relic', True),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('object_type', 'object_type_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/hierarchy/{id}/descendants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcd_hierarchy_object_v1(client):
    """Test case for get_vcd_hierarchy_object_v1

    Get summary of a vCD hierarchy object
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/hierarchy/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

