from typing import List, Dict
from aiohttp import web

from openapi_server.models.experiment_model import ExperimentModel
from openapi_server.models.message_model import MessageModel
from openapi_server import util


async def create_experiment_using_post(request: web.Request, api_key, body) -> web.Response:
    """createExperiment

    

    :param api_key: apiKey
    :type api_key: str
    :param body: input
    :type body: dict | bytes

    """
    body = ExperimentModel.from_dict(body)
    return web.Response(status=200)


async def delete_experiment_using_delete(request: web.Request, api_key, id) -> web.Response:
    """deleteExperiment

    

    :param api_key: apiKey
    :type api_key: str
    :param id: id
    :type id: int

    """
    return web.Response(status=200)


async def do_action_experiment_using_post(request: web.Request, api_key, id, action) -> web.Response:
    """doActionExperiment

    

    :param api_key: apiKey
    :type api_key: str
    :param id: id
    :type id: int
    :param action: action
    :type action: str

    """
    return web.Response(status=200)


async def get_experiment_using_get(request: web.Request, api_key, id) -> web.Response:
    """getExperiment

    

    :param api_key: apiKey
    :type api_key: str
    :param id: id
    :type id: int

    """
    return web.Response(status=200)


async def get_experiments_using_get(request: web.Request, api_key) -> web.Response:
    """getExperiments

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def update_experiment_using_put(request: web.Request, api_key, id, body) -> web.Response:
    """updateExperiment

    

    :param api_key: apiKey
    :type api_key: str
    :param id: id
    :type id: int
    :param body: input
    :type body: dict | bytes

    """
    body = ExperimentModel.from_dict(body)
    return web.Response(status=200)
