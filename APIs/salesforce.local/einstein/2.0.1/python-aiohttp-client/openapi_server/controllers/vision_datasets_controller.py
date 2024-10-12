from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.dataset_list import DatasetList
from openapi_server.models.deletion_response import DeletionResponse
from openapi_server import util


async def create_dataset(request: web.Request, labels=None, name=None, type=None) -> web.Response:
    """Create a Dataset

    Creates a dataset and labels, if they&#39;re specified.

    :param labels: Optional comma-separated list of labels. If specified, creates the labels in the dataset. Maximum number of labels per dataset is 250.
    :type labels: str
    :param name: Name of the dataset. Maximum length is 180 characters.
    :type name: str
    :param type: Type of dataset data
    :type type: str

    """
    return web.Response(status=200)


async def delete_dataset1(request: web.Request, dataset_id) -> web.Response:
    """Delete a Dataset

    Deletes the specified dataset and associated labels and examples.

    :param dataset_id: Dataset Id
    :type dataset_id: str

    """
    return web.Response(status=200)


async def get1(request: web.Request, id) -> web.Response:
    """Get Deletion Status

    Returns the status of an image dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.

    :param id: Deletion Id
    :type id: str

    """
    return web.Response(status=200)


async def get_dataset1(request: web.Request, dataset_id) -> web.Response:
    """Get a Dataset

    Returns a single dataset.

    :param dataset_id: Dataset Id
    :type dataset_id: str

    """
    return web.Response(status=200)


async def list_datasets1(request: web.Request, offset=None, count=None, _global=None) -> web.Response:
    """Get All Datasets

    Returns a list of datasets and their labels that were created by the current user. The response is sorted by dataset ID.

    :param offset: Index of the dataset from which you want to start paging
    :type offset: str
    :param count: Number of datsets to return. Maximum valid value is 25. If you specify a number greater than 25, the call returns 25 datasets.
    :type count: str
    :param _global: If true, returns all global datasets. Global datasets are public datasets that Salesforce provides.
    :type _global: bool

    """
    return web.Response(status=200)


async def upload_dataset_async1(request: web.Request, data=None, name=None, path=None, type=None) -> web.Response:
    """Create a Dataset From a Zip File Asynchronously

    Creates a dataset, labels, and examples from the specified .zip file. The call returns immediately and continues to upload the images in the background.

    :param data: Path to the .zip file on the local drive (FilePart).
    :type data: str
    :param name: Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name.
    :type name: str
    :param path: URL of the .zip file.
    :type path: str
    :param type: Type of dataset data.
    :type type: str

    """
    return web.Response(status=200)


async def upload_dataset_sync1(request: web.Request, data=None, name=None, path=None, type=None) -> web.Response:
    """Create a Dataset From a Zip File Synchronously

    Creates a dataset, labels, and examples from the specified .zip file. The call returns after the dataset is created and all of the images are uploaded.

    :param data: Path to the .zip file on the local drive (FilePart).
    :type data: str
    :param name: Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name.
    :type name: str
    :param path: URL of the .zip file.
    :type path: str
    :param type: Type of dataset data.
    :type type: str

    """
    return web.Response(status=200)
