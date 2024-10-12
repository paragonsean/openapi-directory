# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.multi_route_result import MultiRouteResult
from openapi_server.models.route import Route
from openapi_server.models.route_create import RouteCreate
from openapi_server.models.route_result import RouteResult


pytestmark = pytest.mark.asyncio

async def test_route_get(client):
    """Test case for route_get

    get routes
    """
    params = [('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/route',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_post(client):
    """Test case for route_post

    create route
    """
    route = {"path":"path","response_data":"{}","domain_key":"domain_key","checksum":"checksum","zone_key":"zone_key","cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"route_key":"route_key","rules":[{"methods":["methods","methods"],"cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rule_key":"rule_key","constraints":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"matches":[{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"},{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"}]},{"methods":["methods","methods"],"cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rule_key":"rule_key","constraints":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"matches":[{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"},{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"}]}],"shared_rules_key":"shared_rules_key","retry_policy":{"per_try_timeout_msec":6,"num_retries":0,"timeout_msec":1}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/route',
        headers=headers,
        json=route,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_route_key_delete(client):
    """Test case for route_route_key_delete

    delete route
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/route/{route_key}'.format(route_key='1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_route_key_get(client):
    """Test case for route_route_key_get

    get route
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/route/{route_key}'.format(route_key='1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_route_key_put(client):
    """Test case for route_route_key_put

    modify route
    """
    route = {"path":"path","response_data":"{}","domain_key":"domain_key","checksum":"checksum","zone_key":"zone_key","cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"route_key":"route_key","rules":[{"methods":["methods","methods"],"cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rule_key":"rule_key","constraints":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"matches":[{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"},{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"}]},{"methods":["methods","methods"],"cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rule_key":"rule_key","constraints":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"matches":[{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"},{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"}]}],"shared_rules_key":"shared_rules_key","retry_policy":{"per_try_timeout_msec":6,"num_retries":0,"timeout_msec":1}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.0/route/{route_key}'.format(route_key='1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c'),
        headers=headers,
        json=route,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_rules_shared_rules_key_delete(client):
    """Test case for shared_rules_shared_rules_key_delete

    delete shared_rules object
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/shared_rules/{shared_rules_key}'.format(shared_rules_key='1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

