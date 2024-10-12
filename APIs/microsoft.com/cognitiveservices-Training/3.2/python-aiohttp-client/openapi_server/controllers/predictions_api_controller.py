from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.image_prediction import ImagePrediction
from openapi_server.models.image_url import ImageUrl
from openapi_server.models.prediction_query_result import PredictionQueryResult
from openapi_server.models.prediction_query_token import PredictionQueryToken
from openapi_server import util


async def delete_prediction(request: web.Request, project_id, ids) -> web.Response:
    """Delete a set of predicted images and their associated prediction results.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param ids: The prediction ids. Limited to 64.
    :type ids: List[str]

    """
    return web.Response(status=200)


async def query_predictions(request: web.Request, project_id, body) -> web.Response:
    """Get images that were sent to your prediction endpoint.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param body: Parameters used to query the predictions. Limited to combining 2 tags.
    :type body: dict | bytes

    """
    body = PredictionQueryToken.from_dict(body)
    return web.Response(status=200)


async def quick_test_image(request: web.Request, project_id, image_data, iteration_id=None, store=None) -> web.Response:
    """Quick test an image.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param image_data: Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB.
    :type image_data: str
    :param iteration_id: Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
    :type iteration_id: str
    :type iteration_id: str
    :param store: Optional. Specifies whether or not to store the result of this prediction. The default is true, to store.
    :type store: bool

    """
    return web.Response(status=200)


async def quick_test_image_url(request: web.Request, project_id, body, iteration_id=None, store=None) -> web.Response:
    """Quick test an image url.

    

    :param project_id: The project to evaluate against.
    :type project_id: str
    :type project_id: str
    :param body: An ImageUrl that contains the url of the image to be evaluated.
    :type body: dict | bytes
    :param iteration_id: Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified.
    :type iteration_id: str
    :type iteration_id: str
    :param store: Optional. Specifies whether or not to store the result of this prediction. The default is true, to store.
    :type store: bool

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)
