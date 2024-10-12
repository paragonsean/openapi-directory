from typing import List, Dict
from aiohttp import web

from openapi_server.models.image_classification_request import ImageClassificationRequest
from openapi_server.models.image_classification_response import ImageClassificationResponse
from openapi_server.models.ocr_predict_response import OCRPredictResponse
from openapi_server.models.object_detection_request import ObjectDetectionRequest
from openapi_server.models.object_detection_response import ObjectDetectionResponse
from openapi_server import util


async def detect_multipart(request: web.Request, body=None) -> web.Response:
    """Detection with Image File

    Returns labels, probabilities, and bounding box coordinates for items detected in the specified local image file.

    :param body: 
    :type body: dict | bytes

    """
    body = ObjectDetectionRequest.from_dict(body)
    return web.Response(status=200)


async def ocr_multipart(request: web.Request, model_id=None, sample_content=None, sample_id=None, sample_location=None, task=None) -> web.Response:
    """Detect Text

    Returns a prediction from an OCR model for the specified image URL or local image file.

    :param model_id: ID of the model that makes the prediction. Valid values are OCRModel and tabulatev2.
    :type model_id: str
    :param sample_content: Binary content of image file uploaded as multipart/form-data. Optional.
    :type sample_content: str
    :param sample_id: String that you can pass in to tag the prediction. Optional. Can be any value, and is returned in the response.
    :type sample_id: str
    :param sample_location: URL of the image file. Use this parameter when sending in a file from a web location. Optional.
    :type sample_location: str
    :param task: Optional. Designates the type of data in the image. Default is text. Valid values: contact, table, and text.
    :type task: str

    """
    return web.Response(status=200)


async def predict_multipart(request: web.Request, body=None) -> web.Response:
    """Make Prediction

    Returns a prediction from an image or multi-label model for the specified image.

    :param body: 
    :type body: dict | bytes

    """
    body = ImageClassificationRequest.from_dict(body)
    return web.Response(status=200)
