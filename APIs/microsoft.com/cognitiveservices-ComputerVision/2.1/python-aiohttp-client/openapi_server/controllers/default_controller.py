from typing import List, Dict
from aiohttp import web

from openapi_server.models.area_of_interest_result import AreaOfInterestResult
from openapi_server.models.computer_vision_error import ComputerVisionError
from openapi_server.models.detect_result import DetectResult
from openapi_server.models.domain_model_results import DomainModelResults
from openapi_server.models.image_analysis import ImageAnalysis
from openapi_server.models.image_description import ImageDescription
from openapi_server.models.image_url import ImageUrl
from openapi_server.models.list_models_result import ListModelsResult
from openapi_server.models.ocr_result import OcrResult
from openapi_server.models.tag_result import TagResult
from openapi_server import util


async def analyze_image(request: web.Request, body, visual_features=None, details=None, language=None, description_exclude=None) -> web.Response:
    """analyze_image

    This operation extracts a rich set of visual features based on the image content.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL. Within your request, there is an optional parameter to allow you to choose which features to return. By default, image categories are returned in the response.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes
    :param visual_features: A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include: Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&amp;white. Adult - detects if the image is pornographic in nature (depicts nudity or a sex act), or is gory (depicts extreme violence or blood). Sexually suggestive content (aka racy content) is also detected. Objects - detects various objects within an image, including the approximate location. The Objects argument is only available in English. Brands - detects various brands within an image, including the approximate location. The Brands argument is only available in English.
    :type visual_features: List[str]
    :param details: A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include: Celebrities - identifies celebrities if detected in the image, Landmarks - identifies notable landmarks in the image.
    :type details: List[str]
    :param language: The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    :type language: str
    :param description_exclude: Turn off specified domain models when generating the description.
    :type description_exclude: List[str]

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def analyze_image_by_domain(request: web.Request, model, body, language=None) -> web.Response:
    """analyze_image_by_domain

    This operation recognizes content within an image by applying a domain-specific model. The list of domain-specific models that are supported by the Computer Vision API can be retrieved using the /models GET request. Currently, the API provides following domain-specific models: celebrities, landmarks.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

    :param model: The domain-specific content to recognize.
    :type model: str
    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes
    :param language: The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    :type language: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def describe_image(request: web.Request, body, max_candidates=None, language=None, description_exclude=None) -> web.Response:
    """describe_image

    This operation generates a description of an image in human readable language with complete sentences. The description is based on a collection of content tags, which are also returned by the operation. More than one description can be generated for each image. Descriptions are ordered by their confidence score. Descriptions may include results from celebrity and landmark domain models, if applicable.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes
    :param max_candidates: Maximum number of candidate descriptions to be returned.  The default is 1.
    :type max_candidates: int
    :param language: The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    :type language: str
    :param description_exclude: Turn off specified domain models when generating the description.
    :type description_exclude: List[str]

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def detect_objects(request: web.Request, body) -> web.Response:
    """detect_objects

    Performs object detection on the specified image.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def generate_thumbnail(request: web.Request, width, height, body, smart_cropping=None) -> web.Response:
    """generate_thumbnail

    This operation generates a thumbnail image with the user-specified width and height. By default, the service analyzes the image, identifies the region of interest (ROI), and generates smart cropping coordinates based on the ROI. Smart cropping helps when you specify an aspect ratio that differs from that of the input image.  A successful response contains the thumbnail image binary. If the request failed, the response contains an error code and a message to help determine what went wrong.  Upon failure, the error code and an error message are returned. The error code could be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, InvalidThumbnailSize, NotSupportedImage, FailedToProcess, Timeout, or InternalServerError.

    :param width: Width of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50.
    :type width: int
    :param height: Height of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50.
    :type height: int
    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes
    :param smart_cropping: Boolean flag for enabling smart cropping.
    :type smart_cropping: bool

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def get_area_of_interest(request: web.Request, body) -> web.Response:
    """get_area_of_interest

    This operation returns a bounding box around the most important area of the image.  A successful response will be returned in JSON. If the request failed, the response contains an error code and a message to help determine what went wrong.  Upon failure, the error code and an error message are returned. The error code could be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage, FailedToProcess, Timeout, or InternalServerError.

    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def list_models(request: web.Request, ) -> web.Response:
    """list_models

    This operation returns the list of domain-specific models that are supported by the Computer Vision API. Currently, the API supports following domain-specific models: celebrity recognizer, landmark recognizer.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.


    """
    return web.Response(status=200)


async def recognize_printed_text(request: web.Request, detect_orientation, body, language=None) -> web.Response:
    """recognize_printed_text

    Optical Character Recognition (OCR) detects text in an image and extracts the recognized characters into a machine-usable character stream.  Upon success, the OCR results will be returned.  Upon failure, the error code together with an error message will be returned. The error code can be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage, NotSupportedLanguage, or InternalServerError.

    :param detect_orientation: Whether detect the text orientation in the image. With detectOrientation&#x3D;true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it&#39;s upside-down).
    :type detect_orientation: bool
    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes
    :param language: The BCP-47 language code of the text to be detected in the image. The default value is &#39;unk&#39;.
    :type language: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def tag_image(request: web.Request, body, language=None) -> web.Response:
    """tag_image

    This operation generates a list of words, or tags, that are relevant to the content of the supplied image. The Computer Vision API can return tags based on objects, living beings, scenery or actions found in images. Unlike categories, tags are not organized according to a hierarchical classification system, but correspond to image content. Tags may contain hints to avoid ambiguity or provide context, for example the tag \&quot;ascomycete\&quot; may be accompanied by the hint \&quot;fungus\&quot;.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes
    :param language: The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    :type language: str

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)
