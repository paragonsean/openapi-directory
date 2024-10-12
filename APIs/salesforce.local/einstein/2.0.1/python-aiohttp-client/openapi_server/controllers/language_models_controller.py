from typing import List, Dict
from aiohttp import web

from openapi_server.models.deletion_response import DeletionResponse
from openapi_server.models.learning_curve_list import LearningCurveList
from openapi_server.models.metrics import Metrics
from openapi_server.models.model_list import ModelList
from openapi_server import util


async def delete_model(request: web.Request, model_id) -> web.Response:
    """Delete a Model

    Deletes the specified model.

    :param model_id: Model Id
    :type model_id: str

    """
    return web.Response(status=200)


async def get_trained_model_learning_curve(request: web.Request, model_id, offset=None, count=None) -> web.Response:
    """Get Model Learning Curve

    Returns the metrics for each epoch in a model.

    :param model_id: Model Id
    :type model_id: str
    :param offset: Index of the epoch from which you want to start paging
    :type offset: str
    :param count: Number of epoch to return. Maximum valid value is 25.
    :type count: str

    """
    return web.Response(status=200)


async def get_trained_model_metrics(request: web.Request, model_id) -> web.Response:
    """Get Model Metrics

    Returns the metrics for a model

    :param model_id: Model Id
    :type model_id: str

    """
    return web.Response(status=200)


async def get_trained_models(request: web.Request, dataset_id, offset=None, count=None) -> web.Response:
    """Get All Models

    Returns all models for the specified dataset.

    :param dataset_id: Dataset Id
    :type dataset_id: str
    :param offset: Index of the model from which you want to start paging.
    :type offset: str
    :param count: Number of models to return.
    :type count: str

    """
    return web.Response(status=200)
