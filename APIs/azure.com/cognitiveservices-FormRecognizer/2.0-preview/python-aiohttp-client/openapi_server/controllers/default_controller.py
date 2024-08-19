from typing import List, Dict
from aiohttp import web

from openapi_server.models.analyze_operation_result import AnalyzeOperationResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.model import Model
from openapi_server.models.models import Models
from openapi_server.models.train_request import TrainRequest
from openapi_server import util


async def analyze_layout_async(request: web.Request, file_stream=None) -> web.Response:
    """Analyze Layout

    Extract text and layout information from a given document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

    :param file_stream: .json, .pdf, .jpg, .png or .tiff type file stream.
    :type file_stream: 

    """
    return web.Response(status=200)


async def analyze_receipt_async(request: web.Request, include_text_details=None, file_stream=None) -> web.Response:
    """Analyze Receipt

    Extract field text and semantic values from a given receipt document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

    :param include_text_details: Include text lines and element references in the result.
    :type include_text_details: bool
    :param file_stream: .json, .pdf, .jpg, .png or .tiff type file stream.
    :type file_stream: 

    """
    return web.Response(status=200)


async def analyze_with_custom_model(request: web.Request, model_id, include_text_details=None, file_stream=None) -> web.Response:
    """Analyze Form

    Extract key-value pairs, tables, and semantic values from a given document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

    :param model_id: Model identifier.
    :type model_id: str
    :type model_id: str
    :param include_text_details: Include text lines and element references in the result.
    :type include_text_details: bool
    :param file_stream: .json, .pdf, .jpg, .png or .tiff type file stream.
    :type file_stream: 

    """
    return web.Response(status=200)


async def delete_custom_model(request: web.Request, model_id) -> web.Response:
    """Delete Custom Model

    Mark model for deletion. Model artifacts will be permanently removed within a predetermined period.

    :param model_id: Model identifier.
    :type model_id: str
    :type model_id: str

    """
    return web.Response(status=200)


async def get_analyze_form_result(request: web.Request, model_id, result_id) -> web.Response:
    """Get Analyze Form Result

    Obtain current status and the result of the analyze form operation.

    :param model_id: Model identifier.
    :type model_id: str
    :type model_id: str
    :param result_id: Analyze operation result identifier.
    :type result_id: str
    :type result_id: str

    """
    return web.Response(status=200)


async def get_analyze_layout_result(request: web.Request, result_id) -> web.Response:
    """Get Analyze Layout Result

    Track the progress and obtain the result of the analyze layout operation

    :param result_id: Analyze operation result identifier.
    :type result_id: str
    :type result_id: str

    """
    return web.Response(status=200)


async def get_analyze_receipt_result(request: web.Request, result_id) -> web.Response:
    """Get Analyze Receipt Result

    Track the progress and obtain the result of the analyze receipt operation.

    :param result_id: Analyze operation result identifier.
    :type result_id: str
    :type result_id: str

    """
    return web.Response(status=200)


async def get_custom_model(request: web.Request, model_id, include_keys=None) -> web.Response:
    """Get Custom Model

    Get detailed information about a custom model.

    :param model_id: Model identifier.
    :type model_id: str
    :type model_id: str
    :param include_keys: Include list of extracted keys in model information.
    :type include_keys: bool

    """
    return web.Response(status=200)


async def get_custom_models(request: web.Request, op=None) -> web.Response:
    """List Custom Models

    Get information about all custom models

    :param op: Specify whether to return summary or full list of models.
    :type op: str

    """
    return web.Response(status=200)


async def train_custom_model_async(request: web.Request, train_request) -> web.Response:
    """Train Custom Model

    Create and train a custom model. The request must include a source parameter that is either an externally accessible Azure storage blob container Uri (preferably a Shared Access Signature Uri) or valid path to a data folder in a locally mounted drive. When local paths are specified, they must follow the Linux/Unix path format and be an absolute path rooted to the input mount configuration setting value e.g., if &#39;{Mounts:Input}&#39; configuration setting value is &#39;/input&#39; then a valid source path would be &#39;/input/contosodataset&#39;. All data to be trained is expected to be under the source folder or sub folders under it. Models are trained using documents that are of the following content type - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39;, &#39;image/tiff&#39;. Other type of content is ignored.

    :param train_request: Training request parameters.
    :type train_request: dict | bytes

    """
    train_request = TrainRequest.from_dict(train_request)
    return web.Response(status=200)
