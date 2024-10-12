from typing import List, Dict
from aiohttp import web

from openapi_server.models.analyze_result import AnalyzeResult
from openapi_server.models.analyze_with_custom_model_request import AnalyzeWithCustomModelRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.keys_result import KeysResult
from openapi_server.models.model_result import ModelResult
from openapi_server.models.models_result import ModelsResult
from openapi_server.models.train_request import TrainRequest
from openapi_server.models.train_result import TrainResult
from openapi_server import util


async def analyze_with_custom_model(request: web.Request, id, body, keys=None) -> web.Response:
    """Analyze Form

    Extract key-value pairs from a given document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39; or &#39;image/png&#39;. A success response is returned in JSON.

    :param id: Model Identifier to analyze the document with.
    :type id: str
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param keys: An optional list of known keys to extract the values for.
    :type keys: List[str]

    """
    body = AnalyzeWithCustomModelRequest.from_dict(body)
    return web.Response(status=200)


async def delete_custom_model(request: web.Request, id) -> web.Response:
    """Delete Model

    Delete model artifacts.

    :param id: The identifier of the model to delete.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_custom_model(request: web.Request, id) -> web.Response:
    """Get Model

    Get information about a model.

    :param id: Model identifier.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_custom_models(request: web.Request, ) -> web.Response:
    """Get Models

    Get information about all trained custom models


    """
    return web.Response(status=200)


async def get_extracted_keys(request: web.Request, id) -> web.Response:
    """Get Keys

    Retrieve the keys that were   extracted during the training of the specified model.

    :param id: Model identifier.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def train_custom_model(request: web.Request, train_request) -> web.Response:
    """Train Model

    Create and train a custom model. The train request must include a source parameter that is either an externally accessible Azure Storage blob container Uri (preferably a Shared Access Signature Uri) or valid path to a data folder in a locally mounted drive. When local paths are specified, they must follow the Linux/Unix path format and be an absolute path rooted to the input mount configuration   setting value e.g., if &#39;{Mounts:Input}&#39; configuration setting value is &#39;/input&#39; then a valid source path would be &#39;/input/contosodataset&#39;. All data to be trained is expected to be directly under the source folder. Subfolders are not supported. Models are trained using documents that are of the following content type - &#39;application/pdf&#39;, &#39;image/jpeg&#39; and &#39;image/png&#39;.\&quot;   Other type of content is ignored.

    :param train_request: Request object for training.
    :type train_request: dict | bytes

    """
    train_request = TrainRequest.from_dict(train_request)
    return web.Response(status=200)
