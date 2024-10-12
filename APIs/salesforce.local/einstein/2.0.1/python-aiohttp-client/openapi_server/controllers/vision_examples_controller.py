from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.example import Example
from openapi_server.models.example_list import ExampleList
from openapi_server import util


async def add_example(request: web.Request, dataset_id, data=None, label_id=None, name=None) -> web.Response:
    """Create an Example

    Adds an example with the specified label to a dataset.

    :param dataset_id: Dataset Id
    :type dataset_id: str
    :param data: Location of the local image file to upload.
    :type data: str
    :param label_id: ID of the label to add to the example.
    :type label_id: int
    :param name: Name of the example. Maximum length is 180 characters.
    :type name: str

    """
    return web.Response(status=200)


async def get_examples1(request: web.Request, dataset_id, offset=None, count=None, source=None) -> web.Response:
    """Get All Examples

    Returns all the examples for the specified dataset. By default, returns examples created by uploading them from a .zip file.

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


async def get_examples_by_label1(request: web.Request, label_id=None, offset=None, count=None) -> web.Response:
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


async def provide_feedback1(request: web.Request, data=None, expected_label=None, model_id=None, name=None) -> web.Response:
    """Create a Feedback Example

    Adds a feedback example to the dataset associated with the specified model.

    :param data: Local image file to upload.
    :type data: str
    :param expected_label: Correct label for the example. Must be a label that exists in the dataset.
    :type expected_label: str
    :param model_id: ID of the model that misclassified the image. The feedback example is added to the dataset associated with this model.
    :type model_id: str
    :param name: Name of the example. Optional. Maximum length is 180 characters.
    :type name: str

    """
    return web.Response(status=200)


async def update_dataset_async1(request: web.Request, data=None, model_id=None) -> web.Response:
    """Create Feedback Examples From a Zip File

    Adds feedback examples to the dataset associated with the specified object detection model.

    :param data: Local .zip file to upload. The maximum .zip file size you can upload from a local drive is 50 MB.
    :type data: str
    :param model_id: ID of the model that misclassified the images. The feedback examples are added to the dataset associated with this model.
    :type model_id: str

    """
    return web.Response(status=200)


async def update_dataset_async2(request: web.Request, dataset_id, data=None, path=None) -> web.Response:
    """Create Examples From a Zip File

    Adds examples from a .zip file to a dataset. You can use this call only with a dataset that was created from a .zip file.

    :param dataset_id: Dataset Id
    :type dataset_id: str
    :param data: Location of the local image file to upload.
    :type data: str
    :param path: URL of the .zip file.
    :type path: str

    """
    return web.Response(status=200)
