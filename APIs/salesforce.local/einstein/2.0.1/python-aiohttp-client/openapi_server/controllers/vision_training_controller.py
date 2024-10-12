from typing import List, Dict
from aiohttp import web

from openapi_server.models.train_response import TrainResponse
from openapi_server.models.v2_vision_train_params import V2VisionTrainParams
from openapi_server import util


async def get_train_status_and_progress1(request: web.Request, model_id) -> web.Response:
    """Get Training Status

    Returns the status of a model&#39;s training process. Use the progress field to determine how far the training has progressed. When training completes successfully, the status is SUCCEEDED and the progress is 1.

    :param model_id: 
    :type model_id: str

    """
    return web.Response(status=200)


async def retrain1(request: web.Request, algorithm=None, epochs=None, learning_rate=None, model_id=None, train_params=None) -> web.Response:
    """Retrain a Dataset

    Retrains a dataset and updates a model. Use this API call when you want to update a model and keep the model ID instead of creating a new model.

    :param algorithm: Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution.
    :type algorithm: str
    :param epochs: Number of training iterations for the neural network. Optional.
    :type epochs: int
    :param learning_rate: Specifies how much the gradient affects the optimization of the model at each time step. Optional.
    :type learning_rate: float
    :param model_id: ID of the model to be updated from the training.
    :type model_id: str
    :param train_params: 
    :type train_params: dict | bytes

    """
    train_params = V2VisionTrainParams.from_dict(train_params)
    return web.Response(status=200)


async def train1(request: web.Request, algorithm=None, dataset_id=None, epochs=None, learning_rate=None, name=None, train_params=None) -> web.Response:
    """Train a Dataset

    Trains a dataset and creates a model.

    :param algorithm: Specifies the algorithm used to train the dataset. Optional. Use this parameter only when training a dataset with a type of image-detection. Valid values are object-detection-v1 and retail-execution.
    :type algorithm: str
    :param dataset_id: ID of the dataset to train.
    :type dataset_id: int
    :param epochs: Number of training iterations for the neural network. Optional.
    :type epochs: int
    :param learning_rate: Specifies how much the gradient affects the optimization of the model at each time step. Optional.
    :type learning_rate: float
    :param name: Name of the model. Maximum length is 180 characters.
    :type name: str
    :param train_params: 
    :type train_params: dict | bytes

    """
    train_params = V2VisionTrainParams.from_dict(train_params)
    return web.Response(status=200)
