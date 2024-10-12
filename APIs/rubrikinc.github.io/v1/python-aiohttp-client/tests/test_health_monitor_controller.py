# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.health_monitor_policy import HealthMonitorPolicy
from openapi_server.models.node_policy_check_result import NodePolicyCheckResult
from openapi_server.models.run_policy_arg import RunPolicyArg


pytestmark = pytest.mark.asyncio

async def test_get_policies(client):
    """Test case for get_policies

    Get details of health monitor policies
    """
    params = [('policy_ids', ['policy_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/health_monitor/policies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_policy_status(client):
    """Test case for get_policy_status

    Get the status of health monitor policy enforcement
    """
    params = [('policy_ids', ['policy_ids_example']),
                    ('node_ids', ['node_ids_example']),
                    ('has_detailed_status', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/health_monitor/policy_status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_policies(client):
    """Test case for run_policies

    Enforce health monitor policies
    """
    body = {"nodeIds":["nodeIds","nodeIds"],"policyIds":["policyIds","policyIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/health_monitor/run_policy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

