from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.image_prediction import ImagePrediction
from openapi_server.models.image_url import ImageUrl
from openapi_server import util


async def classify_image(request: web.Request, project_id, published_name, image_data, application=None) -> web.Response:
    """Classify an image and saves the result.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param published_name: Specifies the name of the model to evaluate against.
    :type published_name: str
    :param image_data: Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB.
    :type image_data: str
    :param application: Optional. Specifies the name of application using the endpoint.
    :type application: str

    """
    return web.Response(status=200)


async def classify_image_url(request: web.Request, project_id, published_name, body, application=None) -> web.Response:
    """Classify an image url and saves the result.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param published_name: Specifies the name of the model to evaluate against.
    :type published_name: str
    :param body: An ImageUrl that contains the url of the image to be evaluated.
    :type body: dict | bytes
    :param application: Optional. Specifies the name of application using the endpoint.
    :type application: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def classify_image_url_with_no_store(request: web.Request, project_id, published_name, body, application=None) -> web.Response:
    """Classify an image url without saving the result.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param published_name: Specifies the name of the model to evaluate against.
    :type published_name: str
    :param body: An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated.
    :type body: dict | bytes
    :param application: Optional. Specifies the name of application using the endpoint.
    :type application: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def classify_image_with_no_store(request: web.Request, project_id, published_name, image_data, application=None) -> web.Response:
    """Classify an image without saving the result.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param published_name: Specifies the name of the model to evaluate against.
    :type published_name: str
    :param image_data: Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB.
    :type image_data: str
    :param application: Optional. Specifies the name of application using the endpoint.
    :type application: str

    """
    return web.Response(status=200)


async def detect_image(request: web.Request, project_id, published_name, image_data, application=None) -> web.Response:
    """Detect objects in an image and saves the result.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param published_name: Specifies the name of the model to evaluate against.
    :type published_name: str
    :param image_data: Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 4MB.
    :type image_data: str
    :param application: Optional. Specifies the name of application using the endpoint.
    :type application: str

    """
    return web.Response(status=200)


async def detect_image_url(request: web.Request, project_id, published_name, body, application=None) -> web.Response:
    """Detect objects in an image url and saves the result.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param published_name: Specifies the name of the model to evaluate against.
    :type published_name: str
    :param body: An ImageUrl that contains the url of the image to be evaluated.
    :type body: dict | bytes
    :param application: Optional. Specifies the name of application using the endpoint.
    :type application: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def detect_image_url_with_no_store(request: web.Request, project_id, published_name, body, application=None) -> web.Response:
    """Detect objects in an image url without saving the result.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param published_name: Specifies the name of the model to evaluate against.
    :type published_name: str
    :param body: An {Iris.Web.Api.Models.ImageUrl} that contains the url of the image to be evaluated.
    :type body: dict | bytes
    :param application: Optional. Specifies the name of application using the endpoint.
    :type application: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def detect_image_with_no_store(request: web.Request, project_id, published_name, image_data, application=None) -> web.Response:
    """Detect objects in an image without saving the result.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param published_name: Specifies the name of the model to evaluate against.
    :type published_name: str
    :param image_data: Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 0MB.
    :type image_data: str
    :param application: Optional. Specifies the name of application using the endpoint.
    :type application: str

    """
    return web.Response(status=200)
