# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_create import ClusterCreate
from openapi_server.models.cluster_result import ClusterResult
from openapi_server.models.error import Error
from openapi_server.models.instance import Instance
from openapi_server.models.instance_result import InstanceResult
from openapi_server.models.multi_cluster_result import MultiClusterResult


pytestmark = pytest.mark.asyncio

async def test_cluster_cluster_key_delete(client):
    """Test case for cluster_cluster_key_delete

    delete cluster
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/cluster/{cluster_key}'.format(cluster_key='7ef80556-60bb-46bd-4cec-f4e2533aa75c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_cluster_key_get(client):
    """Test case for cluster_cluster_key_get

    get cluster
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/cluster/{cluster_key}'.format(cluster_key='7ef80556-60bb-46bd-4cec-f4e2533aa75c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_cluster_key_instances_instance_identifier_delete(client):
    """Test case for cluster_cluster_key_instances_instance_identifier_delete

    remove instance
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/cluster/{cluster_key}/instances/{instance_identifier}'.format(cluster_key='7ef80556-60bb-46bd-4cec-f4e2533aa75c', instance_identifier='foo-1.useast.test.com:8080'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_cluster_key_instances_post(client):
    """Test case for cluster_cluster_key_instances_post

    add instance
    """
    instance = {"metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"port":1,"host":"host"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/cluster/{cluster_key}/instances'.format(cluster_key='1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c'),
        headers=headers,
        json=instance,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_cluster_key_put(client):
    """Test case for cluster_cluster_key_put

    modify cluster
    """
    cluster = {"circuit_breakers":{"max_connections":0,"max_requests":1,"max_retries":5,"max_pending_requests":6},"cluster_key":"cluster_key","require_tls":True,"instances":[{"metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"port":1,"host":"host"},{"metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"port":1,"host":"host"}],"health_checks":[{"no_traffic_interval_msec":3,"healthy_threshold":2,"unhealthy_threshold":1,"interval_msec":9,"unhealthy_edge_interval_msec":4,"health_checker":{"tcp_health_check":{"receive":["receive","receive"],"send":"send"},"http_health_check":{"path":"path","service_name":"service_name","host":"host","request_headers_to_add":"{}"}},"unhealthy_interval_msec":7,"healthy_edge_interval_msec":5,"reuse_connection":True,"timeout_msec":2,"interval_jitter_msec":7},{"no_traffic_interval_msec":3,"healthy_threshold":2,"unhealthy_threshold":1,"interval_msec":9,"unhealthy_edge_interval_msec":4,"health_checker":{"tcp_health_check":{"receive":["receive","receive"],"send":"send"},"http_health_check":{"path":"path","service_name":"service_name","host":"host","request_headers_to_add":"{}"}},"unhealthy_interval_msec":7,"healthy_edge_interval_msec":5,"reuse_connection":True,"timeout_msec":2,"interval_jitter_msec":7}],"name":"name","zone_key":"zone_key","checksum":"checksum","outlier_detection":{"max_ejection_percent":9,"success_rate_minimum_hosts":6,"consecutive_5xx":6,"success_rate_stdev_factor":9,"consecutive_gateway_failure":7,"enforcing_consecutive_gateway_failure":4,"interval_msec":9,"enforcing_consecutive_5xx":1,"enforcing_success_rate":5,"success_rate_request_volume":8,"base_ejection_time_msec":1}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.0/cluster/{cluster_key}'.format(cluster_key='5074fe62-821e-4034-55bd-b9caa09af2a1'),
        headers=headers,
        json=cluster,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_get(client):
    """Test case for cluster_get

    get clusters
    """
    params = [('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/cluster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_post(client):
    """Test case for cluster_post

    create cluster
    """
    cluster = {"circuit_breakers":{"max_connections":0,"max_requests":1,"max_retries":5,"max_pending_requests":6},"require_tls":True,"instances":[{"metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"port":1,"host":"host"},{"metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"port":1,"host":"host"}],"health_checks":[{"no_traffic_interval_msec":3,"healthy_threshold":2,"unhealthy_threshold":1,"interval_msec":9,"unhealthy_edge_interval_msec":4,"health_checker":{"tcp_health_check":{"receive":["receive","receive"],"send":"send"},"http_health_check":{"path":"path","service_name":"service_name","host":"host","request_headers_to_add":"{}"}},"unhealthy_interval_msec":7,"healthy_edge_interval_msec":5,"reuse_connection":True,"timeout_msec":2,"interval_jitter_msec":7},{"no_traffic_interval_msec":3,"healthy_threshold":2,"unhealthy_threshold":1,"interval_msec":9,"unhealthy_edge_interval_msec":4,"health_checker":{"tcp_health_check":{"receive":["receive","receive"],"send":"send"},"http_health_check":{"path":"path","service_name":"service_name","host":"host","request_headers_to_add":"{}"}},"unhealthy_interval_msec":7,"healthy_edge_interval_msec":5,"reuse_connection":True,"timeout_msec":2,"interval_jitter_msec":7}],"name":"name","zone_key":"zone_key","outlier_detection":{"max_ejection_percent":9,"success_rate_minimum_hosts":6,"consecutive_5xx":6,"success_rate_stdev_factor":9,"consecutive_gateway_failure":7,"enforcing_consecutive_gateway_failure":4,"interval_msec":9,"enforcing_consecutive_5xx":1,"enforcing_success_rate":5,"success_rate_request_volume":8,"base_ejection_time_msec":1}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/cluster',
        headers=headers,
        json=cluster,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

