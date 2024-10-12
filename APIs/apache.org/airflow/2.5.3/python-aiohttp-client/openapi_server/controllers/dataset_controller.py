from typing import List, Dict
from aiohttp import web

from openapi_server.models.dataset import Dataset
from openapi_server.models.dataset_collection import DatasetCollection
from openapi_server.models.dataset_event_collection import DatasetEventCollection
from openapi_server.models.error import Error
from openapi_server import util


async def get_dataset(request: web.Request, uri) -> web.Response:
    """Get a dataset

    Get a dataset by uri.

    :param uri: The encoded Dataset URI
    :type uri: str

    """
    return web.Response(status=200)


async def get_dataset_events(request: web.Request, limit=None, offset=None, order_by=None, dataset_id=None, source_dag_id=None, source_task_id=None, source_run_id=None, source_map_index=None) -> web.Response:
    """Get dataset events

    Get dataset events

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str
    :param dataset_id: The Dataset ID that updated the dataset.
    :type dataset_id: int
    :param source_dag_id: The DAG ID that updated the dataset.
    :type source_dag_id: str
    :param source_task_id: The task ID that updated the dataset.
    :type source_task_id: str
    :param source_run_id: The DAG run ID that updated the dataset.
    :type source_run_id: str
    :param source_map_index: The map index that updated the dataset.
    :type source_map_index: int

    """
    return web.Response(status=200)


async def get_datasets(request: web.Request, limit=None, offset=None, order_by=None, uri_pattern=None) -> web.Response:
    """List datasets

    

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str
    :param uri_pattern: If set, only return datasets with uris matching this pattern. 
    :type uri_pattern: str

    """
    return web.Response(status=200)


async def get_upstream_dataset_events_0(request: web.Request, dag_id, dag_run_id) -> web.Response:
    """Get dataset events for a DAG run

    Get datasets for a dag run.  *New in version 2.4.0* 

    :param dag_id: The DAG ID.
    :type dag_id: str
    :param dag_run_id: The DAG run ID.
    :type dag_run_id: str

    """
    return web.Response(status=200)
