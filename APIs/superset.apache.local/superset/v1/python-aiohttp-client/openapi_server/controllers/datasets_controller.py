from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.dataset_get200_response import DatasetGet200Response
from openapi_server.models.dataset_pk_get200_response import DatasetPkGet200Response
from openapi_server.models.dataset_pk_put200_response import DatasetPkPut200Response
from openapi_server.models.dataset_post201_response import DatasetPost201Response
from openapi_server.models.dataset_related_objects_response import DatasetRelatedObjectsResponse
from openapi_server.models.dataset_rest_api_post import DatasetRestApiPost
from openapi_server.models.dataset_rest_api_put import DatasetRestApiPut
from openapi_server.models.distinc_response_schema import DistincResponseSchema
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server import util


async def dataset_delete(request: web.Request, q=None) -> web.Response:
    """dataset_delete

    Deletes multiple Datasets in a bulk operation.

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def dataset_distinct_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """dataset_distinct_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def dataset_export_get(request: web.Request, q=None) -> web.Response:
    """dataset_export_get

    Exports multiple datasets and downloads them as YAML files

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def dataset_get(request: web.Request, q=None) -> web.Response:
    """dataset_get

    Get a list of models

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def dataset_import_post(request: web.Request, form_data=None, overwrite=None, passwords=None) -> web.Response:
    """dataset_import_post

    

    :param form_data: upload file (ZIP or YAML)
    :type form_data: str
    :param overwrite: overwrite existing datasets?
    :type overwrite: bool
    :param passwords: JSON map of passwords for each file
    :type passwords: str

    """
    return web.Response(status=200)


async def dataset_info_get(request: web.Request, q=None) -> web.Response:
    """dataset_info_get

    Get metadata information about this API resource

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def dataset_pk_column_column_id_delete(request: web.Request, pk, column_id) -> web.Response:
    """dataset_pk_column_column_id_delete

    Delete a Dataset column

    :param pk: The dataset pk for this column
    :type pk: int
    :param column_id: The column id for this dataset
    :type column_id: int

    """
    return web.Response(status=200)


async def dataset_pk_delete(request: web.Request, pk) -> web.Response:
    """dataset_pk_delete

    Deletes a Dataset

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def dataset_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """dataset_pk_get

    Get an item model

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def dataset_pk_metric_metric_id_delete(request: web.Request, pk, metric_id) -> web.Response:
    """dataset_pk_metric_metric_id_delete

    Delete a Dataset metric

    :param pk: The dataset pk for this column
    :type pk: int
    :param metric_id: The metric id for this dataset
    :type metric_id: int

    """
    return web.Response(status=200)


async def dataset_pk_put(request: web.Request, pk, body, override_columns=None) -> web.Response:
    """dataset_pk_put

    Changes a Dataset

    :param pk: 
    :type pk: int
    :param body: Dataset schema
    :type body: dict | bytes
    :param override_columns: 
    :type override_columns: bool

    """
    body = DatasetRestApiPut.from_dict(body)
    return web.Response(status=200)


async def dataset_pk_refresh_put(request: web.Request, pk) -> web.Response:
    """dataset_pk_refresh_put

    Refreshes and updates columns of a dataset

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def dataset_pk_related_objects_get(request: web.Request, pk) -> web.Response:
    """dataset_pk_related_objects_get

    Get charts and dashboards count associated to a dataset

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def dataset_post(request: web.Request, body) -> web.Response:
    """dataset_post

    Create a new Dataset

    :param body: Dataset schema
    :type body: dict | bytes

    """
    body = DatasetRestApiPost.from_dict(body)
    return web.Response(status=200)


async def dataset_related_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """dataset_related_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)
