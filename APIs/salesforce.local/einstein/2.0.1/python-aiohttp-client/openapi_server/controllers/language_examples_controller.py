from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.example import Example
from openapi_server.models.example_list import ExampleList
from openapi_server import util


async def get_examples(request: web.Request, dataset_id, offset=None, count=None, source=None) -> web.Response:
    """Get All Examples

    Returns all the examples for the specified dataset,

    :param dataset_id: Dataset Id
    :type dataset_id: str
    :param offset: Index of the example from which you want to start paging.
    :type offset: str
    :param count: Number of examples to return.
    :type count: str
    :param source: return examples that were created in the dataset as feedback
    :type source: str

    """
    return web.Response(status=200)


async def get_examples_by_label(request: web.Request, label_id=None, offset=None, count=None) -> web.Response:
    """Get All Examples for Label

    Returns all the examples for the specified label. Returns both uploaded examples and feedback examples.

    :param label_id: Label Id
    :type label_id: str
    :param offset: Index of the example from which you want to start paging.
    :type offset: str
    :param count: Number of examples to return.
    :type count: str

    """
    return web.Response(status=200)


async def provide_feedback(request: web.Request, document=None, expected_label=None, model_id=None, name=None) -> web.Response:
    """Create a Feedback Example

    Adds a feedback example to the dataset associated with the specified model.

    :param document: Intent or sentiment string to add to the dataset.
    :type document: str
    :param expected_label: Correct label for the example. Must be a label that exists in the dataset.
    :type expected_label: str
    :param model_id: ID of the model that misclassified the image. The feedback example is added to the dataset associated with this model.
    :type model_id: str
    :param name: Name of the example. Optional. Maximum length is 180 characters.
    :type name: str

    """
    return web.Response(status=200)


async def update_dataset_async(request: web.Request, dataset_id, data=None, type=None) -> web.Response:
    """Create Examples From a File

    Adds examples from a .csv, .tsv, or .json file to a dataset.

    :param dataset_id: Dataset Id
    :type dataset_id: str
    :param data: Path to the .csv, .tsv, or .json file on a local drive. 
    :type data: str
    :param type: URL of the .csv, .tsv, or .json file.
    :type type: str

    """
    return web.Response(status=200)
