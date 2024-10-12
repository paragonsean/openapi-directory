# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.multi_shared_rules_result import MultiSharedRulesResult
from openapi_server.models.shared_rules import SharedRules
from openapi_server.models.shared_rules_create import SharedRulesCreate
from openapi_server.models.shared_rules_result import SharedRulesResult


pytestmark = pytest.mark.asyncio

async def test_shared_rules_get(client):
    """Test case for shared_rules_get

    get shared_rules
    """
    params = [('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/shared_rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_rules_post(client):
    """Test case for shared_rules_post

    create shared_rules
    """
    shared_rules = {"default":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"response_data":"{}","checksum":"checksum","zone_key":"zone_key","cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rules":[{"methods":["methods","methods"],"cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rule_key":"rule_key","constraints":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"matches":[{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"},{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"}]},{"methods":["methods","methods"],"cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rule_key":"rule_key","constraints":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"matches":[{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"},{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"}]}],"shared_rules_key":"shared_rules_key","retry_policy":{"per_try_timeout_msec":6,"num_retries":0,"timeout_msec":1},"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/shared_rules',
        headers=headers,
        json=shared_rules,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_rules_shared_rules_key_get(client):
    """Test case for shared_rules_shared_rules_key_get

    get shared_rules object
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/shared_rules/{shared_rules_key}'.format(shared_rules_key='1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_rules_shared_rules_key_put(client):
    """Test case for shared_rules_shared_rules_key_put

    modify shared_rules object
    """
    shared_rules = {"default":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"response_data":"{}","checksum":"checksum","zone_key":"zone_key","cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rules":[{"methods":["methods","methods"],"cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rule_key":"rule_key","constraints":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"matches":[{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"},{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"}]},{"methods":["methods","methods"],"cohort_seed":{"name":"name","use_zero_value_seed":True,"type":"header"},"rule_key":"rule_key","constraints":{"tap":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"light":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"dark":[{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"cluster_key":"cluster_key","metadata":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"response_data":"{}","constraint_key":"constraint_key","weight":5,"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}]},"matches":[{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"},{"kind":"kind","from":"{}","to":"{}","behavior":"behavior"}]}],"shared_rules_key":"shared_rules_key","retry_policy":{"per_try_timeout_msec":6,"num_retries":0,"timeout_msec":1},"properties":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.0/shared_rules/{shared_rules_key}'.format(shared_rules_key='1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c'),
        headers=headers,
        json=shared_rules,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

