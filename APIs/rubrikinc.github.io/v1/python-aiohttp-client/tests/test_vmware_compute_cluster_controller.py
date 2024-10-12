# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.compute_cluster_detail import ComputeClusterDetail
from openapi_server.models.compute_cluster_summary_list_response import ComputeClusterSummaryListResponse
from openapi_server.models.compute_cluster_update import ComputeClusterUpdate
from openapi_server.models.fully_qualified_domain_name_info import FullyQualifiedDomainNameInfo
from openapi_server.models.io_filter_summary_list_response import IoFilterSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_get_async_request_status_for_compute_cluster(client):
    """Test case for get_async_request_status_for_compute_cluster

    Get asynchronous request details for VMware cluster
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/compute_cluster/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compute_cluster(client):
    """Test case for get_compute_cluster

    Get details for the compute cluster
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/compute_cluster/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_io_filters(client):
    """Test case for get_io_filters

    Get the ioFilters on the VMware compute cluster with a specific ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/compute_cluster/{id}/io_filter'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_install_io_filter(client):
    """Test case for install_io_filter

    Install the Rubrik ioFilter to the VMware cluster with a specific ID
    """
    body = {"fqdn":"fqdn"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/compute_cluster/{id}/install_io_filter'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_compute_cluster(client):
    """Test case for query_compute_cluster

    Get all the clusters belonging to this datacenter
    """
    params = [('datacenter_id', 'datacenter_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/compute_cluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uninstall_io_filter(client):
    """Test case for uninstall_io_filter

    Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/compute_cluster/{id}/uninstall_io_filter'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_compute_cluster(client):
    """Test case for update_compute_cluster

    Modify information for a VMware compute cluster
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
        path='/api/v1/vmware/compute_cluster/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upgrade_io_filter(client):
    """Test case for upgrade_io_filter

    Upgrade the Rubrik ioFilter for the VMware cluster with a specific ID
    """
    body = {"fqdn":"fqdn"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/compute_cluster/{id}/upgrade_io_filter'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

