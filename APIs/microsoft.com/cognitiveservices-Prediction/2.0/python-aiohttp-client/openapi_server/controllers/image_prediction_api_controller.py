from typing import List, Dict
from aiohttp import web

from openapi_server.models.image_prediction import ImagePrediction
from openapi_server.models.image_url import ImageUrl
from openapi_server import util


async def predict_image(request: web.Request, project_id, prediction_key, image_data, iteration_id=None, application=None) -> web.Response:
    """Predict an image and saves the result

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param prediction_key: 
    :type prediction_key: str
    :param image_data: 
    :type image_data: str
    :param iteration_id: Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
    :type iteration_id: str
    :type iteration_id: str
    :param application: Optional. Specifies the name of application using the endpoint
    :type application: str

    """
    return web.Response(status=200)


async def predict_image_url(request: web.Request, project_id, prediction_key, body, iteration_id=None, application=None) -> web.Response:
    """Predict an image url and saves the result

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param prediction_key: 
    :type prediction_key: str
    :param body: An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated
    :type body: dict | bytes
    :param iteration_id: Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
    :type iteration_id: str
    :type iteration_id: str
    :param application: Optional. Specifies the name of application using the endpoint
    :type application: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def predict_image_url_with_no_store(request: web.Request, project_id, prediction_key, body, iteration_id=None, application=None) -> web.Response:
    """Predict an image url without saving the result

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param prediction_key: 
    :type prediction_key: str
    :param body: An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated
    :type body: dict | bytes
    :param iteration_id: Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
    :type iteration_id: str
    :type iteration_id: str
    :param application: Optional. Specifies the name of application using the endpoint
    :type application: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def predict_image_with_no_store(request: web.Request, project_id, prediction_key, image_data, iteration_id=None, application=None) -> web.Response:
    """Predict an image without saving the result

    

    :param project_id: The project id
    :type project_id: str
    :type project_id: str
    :param prediction_key: 
    :type prediction_key: str
    :param image_data: 
    :type image_data: str
    :param iteration_id: Optional. Specifies the id of a particular iteration to evaluate against.              The default iteration for the project will be used when not specified
    :type iteration_id: str
    :type iteration_id: str
    :param application: Optional. Specifies the name of application using the endpoint
    :type application: str

    """
    return web.Response(status=200)
