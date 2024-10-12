from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.image_prediction import ImagePrediction
from openapi_server.models.image_url import ImageUrl
from openapi_server.models.prediction_query_result import PredictionQueryResult
from openapi_server.models.prediction_query_token import PredictionQueryToken
from openapi_server import util


async def delete_prediction(request: web.Request, project_id, ids, training_key) -> web.Response:
    """Delete a set of predicted images and their associated prediction results.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param ids: The prediction ids. Limited to 64.
    :type ids: List[str]
    :param training_key: API key.
    :type training_key: str

    """
    return web.Response(status=200)


async def query_predictions(request: web.Request, project_id, training_key, body) -> web.Response:
    """Get images that were sent to your prediction endpoint.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: Parameters used to query the predictions. Limited to combining 2 tags.
    :type body: dict | bytes

    """
    body = PredictionQueryToken.from_dict(body)
    return web.Response(status=200)


async def quick_test_image(request: web.Request, project_id, training_key, image_data, iteration_id=None) -> web.Response:
    """Quick test an image.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param image_data: Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB.
    :type image_data: str
    :param iteration_id: Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
    :type iteration_id: str
    :type iteration_id: str

    """
    return web.Response(status=200)


async def quick_test_image_url(request: web.Request, project_id, training_key, body, iteration_id=None) -> web.Response:
    """Quick test an image url.

    

    :param project_id: The project to evaluate against.
    :type project_id: str
    :type project_id: str
    :param training_key: API key.
    :type training_key: str
    :param body: An ImageUrl that contains the url of the image to be evaluated.
    :type body: dict | bytes
    :param iteration_id: Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
    :type iteration_id: str
    :type iteration_id: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)
