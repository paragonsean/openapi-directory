from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.test_harness_scenario_model import TestHarnessScenarioModel
from openapi_server import util


async def create_test_harness_scenario_using_post(request: web.Request, api_key, body) -> web.Response:
    """createTestHarnessScenario

    

    :param api_key: apiKey
    :type api_key: str
    :param body: testHarnessScenarioDTO
    :type body: dict | bytes

    """
    body = TestHarnessScenarioModel.from_dict(body)
    return web.Response(status=200)


async def delete_test_harness_scenario_using_delete(request: web.Request, api_key, scenario_name) -> web.Response:
    """deleteTestHarnessScenario

    

    :param api_key: apiKey
    :type api_key: str
    :param scenario_name: scenarioName
    :type scenario_name: str

    """
    return web.Response(status=200)


async def get_test_harness_scenario_using_get(request: web.Request, api_key, scenario_name) -> web.Response:
    """getTestHarnessScenario

    

    :param api_key: apiKey
    :type api_key: str
    :param scenario_name: scenarioName
    :type scenario_name: str

    """
    return web.Response(status=200)


async def get_test_harness_scenarios_using_get(request: web.Request, api_key) -> web.Response:
    """getTestHarnessScenarios

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def update_test_harness_scenario_using_put(request: web.Request, api_key, scenario_name, body) -> web.Response:
    """updateTestHarnessScenario

    

    :param api_key: apiKey
    :type api_key: str
    :param scenario_name: scenarioName
    :type scenario_name: str
    :param body: testHarnessScenarioDTO
    :type body: dict | bytes

    """
    body = TestHarnessScenarioModel.from_dict(body)
    return web.Response(status=200)
