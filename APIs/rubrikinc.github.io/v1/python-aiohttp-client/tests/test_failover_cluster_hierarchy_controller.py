# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.failover_cluster_hierarchy_object_summary import FailoverClusterHierarchyObjectSummary
from openapi_server.models.failover_cluster_hierarchy_object_summary_list_response import FailoverClusterHierarchyObjectSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_get_failover_cluster_hierarchy_children(client):
    """Test case for get_failover_cluster_hierarchy_children

    Get list of immediate descendant objects
    """
    params = [('name', 'name_example'),
                    ('operating_system_type', 'operating_system_type_example'),
                    ('object_type', 'object_type_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('configured_sla_domain_id', 'configured_sla_domain_id_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/failover_cluster/hierarchy/{id}/children'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_failover_cluster_hierarchy_descendants(client):
    """Test case for get_failover_cluster_hierarchy_descendants

    Get list of descendant objects
    """
    params = [('name', 'name_example'),
                    ('operating_system_type', 'operating_system_type_example'),
                    ('object_type', 'object_type_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('configured_sla_domain_id', 'configured_sla_domain_id_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/failover_cluster/hierarchy/{id}/descendants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_failover_cluster_hierarchy_object(client):
    """Test case for get_failover_cluster_hierarchy_object

    Get summary of a hierarchy object
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/failover_cluster/hierarchy/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

