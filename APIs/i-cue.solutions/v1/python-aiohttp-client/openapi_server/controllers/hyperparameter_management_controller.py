from typing import List, Dict
from aiohttp import web

from openapi_server.models.hyperparameter_model import HyperparameterModel
from openapi_server import util


async def hyperparameter_get(request: web.Request, token=None) -> web.Response:
    """Get hyperparameters

    Get entity global hyperparameters.

    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def hyperparameter_post(request: web.Request, token=None, body=None) -> web.Response:
    """Set hyperparameters

    Set entity global hyperparameters. Hyperparameters can be overwritten by user and planning level (add to JSON body).

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = HyperparameterModel.from_dict(body)
    return web.Response(status=200)
