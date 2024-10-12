# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.test_harness_scenario_model import TestHarnessScenarioModel


pytestmark = pytest.mark.asyncio

async def test_create_test_harness_scenario_using_post(client):
    """Test case for create_test_harness_scenario_using_post

    createTestHarnessScenario
    """
    body = {"scenarioJson":"{}","scenarioName":"scenarioName"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/admin/testHarness/scenarios'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_test_harness_scenario_using_delete(client):
    """Test case for delete_test_harness_scenario_using_delete

    deleteTestHarnessScenario
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/restv2/game/{api_key}/admin/testHarness/scenarios/{scenario_name}'.format(api_key='api_key_example', scenario_name='scenario_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_harness_scenario_using_get(client):
    """Test case for get_test_harness_scenario_using_get

    getTestHarnessScenario
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/testHarness/scenarios/{scenario_name}'.format(api_key='api_key_example', scenario_name='scenario_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_harness_scenarios_using_get(client):
    """Test case for get_test_harness_scenarios_using_get

    getTestHarnessScenarios
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/testHarness/scenarios'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_test_harness_scenario_using_put(client):
    """Test case for update_test_harness_scenario_using_put

    updateTestHarnessScenario
    """
    body = {"scenarioJson":"{}","scenarioName":"scenarioName"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/restv2/game/{api_key}/admin/testHarness/scenarios/{scenario_name}'.format(api_key='api_key_example', scenario_name='scenario_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

