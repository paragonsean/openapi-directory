# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.host_hierarchy_object_summary import HostHierarchyObjectSummary
from openapi_server.models.host_hierarchy_object_summary_list_response import HostHierarchyObjectSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_get_host_hierarchy_children(client):
    """Test case for get_host_hierarchy_children

    Get immediate descendant objects
    """
    params = [('name', 'name_example'),
                    ('object_type', 'object_type_example'),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('template_id', 'template_id_example'),
                    ('vendor_type', 'vendor_type_example'),
                    ('export_point', 'export_point_example'),
                    ('operating_system_type', 'operating_system_type_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', asc),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/host/hierarchy/{id}/children'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_host_hierarchy_object(client):
    """Test case for get_host_hierarchy_object

    Get summary of a host/share hierarchy object
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/host/hierarchy/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

