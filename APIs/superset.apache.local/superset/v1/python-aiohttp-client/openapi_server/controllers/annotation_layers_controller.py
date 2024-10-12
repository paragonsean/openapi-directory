from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get200_response import AnnotationLayerGet200Response
from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.annotation_layer_pk_annotation_annotation_id_get200_response import AnnotationLayerPkAnnotationAnnotationIdGet200Response
from openapi_server.models.annotation_layer_pk_annotation_annotation_id_put200_response import AnnotationLayerPkAnnotationAnnotationIdPut200Response
from openapi_server.models.annotation_layer_pk_annotation_get200_response import AnnotationLayerPkAnnotationGet200Response
from openapi_server.models.annotation_layer_pk_annotation_post201_response import AnnotationLayerPkAnnotationPost201Response
from openapi_server.models.annotation_layer_pk_get200_response import AnnotationLayerPkGet200Response
from openapi_server.models.annotation_layer_pk_put200_response import AnnotationLayerPkPut200Response
from openapi_server.models.annotation_layer_post201_response import AnnotationLayerPost201Response
from openapi_server.models.annotation_layer_rest_api_post import AnnotationLayerRestApiPost
from openapi_server.models.annotation_layer_rest_api_put import AnnotationLayerRestApiPut
from openapi_server.models.annotation_rest_api_post import AnnotationRestApiPost
from openapi_server.models.annotation_rest_api_put import AnnotationRestApiPut
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server import util


async def annotation_layer_delete(request: web.Request, q=None) -> web.Response:
    """annotation_layer_delete

    Deletes multiple annotation layers in a bulk operation.

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def annotation_layer_get(request: web.Request, q=None) -> web.Response:
    """annotation_layer_get

    Get a list of Annotation layers, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def annotation_layer_info_get(request: web.Request, q=None) -> web.Response:
    """annotation_layer_info_get

    Get metadata information about this API resource

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def annotation_layer_pk_annotation_annotation_id_delete(request: web.Request, pk, annotation_id) -> web.Response:
    """annotation_layer_pk_annotation_annotation_id_delete

    Delete Annotation layer

    :param pk: The annotation layer pk for this annotation
    :type pk: int
    :param annotation_id: The annotation pk for this annotation
    :type annotation_id: int

    """
    return web.Response(status=200)


async def annotation_layer_pk_annotation_annotation_id_get(request: web.Request, pk, annotation_id, q=None) -> web.Response:
    """annotation_layer_pk_annotation_annotation_id_get

    Get an Annotation layer

    :param pk: The annotation layer pk for this annotation
    :type pk: int
    :param annotation_id: The annotation pk
    :type annotation_id: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def annotation_layer_pk_annotation_annotation_id_put(request: web.Request, pk, annotation_id, body) -> web.Response:
    """annotation_layer_pk_annotation_annotation_id_put

    Update an Annotation layer

    :param pk: The annotation layer pk for this annotation
    :type pk: int
    :param annotation_id: The annotation pk for this annotation
    :type annotation_id: int
    :param body: Annotation schema
    :type body: dict | bytes

    """
    body = AnnotationRestApiPut.from_dict(body)
    return web.Response(status=200)


async def annotation_layer_pk_annotation_delete(request: web.Request, pk, q=None) -> web.Response:
    """annotation_layer_pk_annotation_delete

    Deletes multiple annotation in a bulk operation.

    :param pk: The annotation layer pk for this annotation
    :type pk: int
    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def annotation_layer_pk_annotation_get(request: web.Request, pk, q=None) -> web.Response:
    """annotation_layer_pk_annotation_get

    Get a list of Annotation layers, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

    :param pk: The annotation layer id for this annotation
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def annotation_layer_pk_annotation_post(request: web.Request, pk, body) -> web.Response:
    """annotation_layer_pk_annotation_post

    Create an Annotation layer

    :param pk: The annotation layer pk for this annotation
    :type pk: int
    :param body: Annotation schema
    :type body: dict | bytes

    """
    body = AnnotationRestApiPost.from_dict(body)
    return web.Response(status=200)


async def annotation_layer_pk_delete(request: web.Request, pk) -> web.Response:
    """annotation_layer_pk_delete

    Delete Annotation layer

    :param pk: The annotation layer pk for this annotation
    :type pk: int

    """
    return web.Response(status=200)


async def annotation_layer_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """annotation_layer_pk_get

    Get an Annotation layer

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def annotation_layer_pk_put(request: web.Request, pk, body) -> web.Response:
    """annotation_layer_pk_put

    Update an Annotation layer

    :param pk: The annotation layer pk for this annotation
    :type pk: int
    :param body: Annotation schema
    :type body: dict | bytes

    """
    body = AnnotationLayerRestApiPut.from_dict(body)
    return web.Response(status=200)


async def annotation_layer_post(request: web.Request, body) -> web.Response:
    """annotation_layer_post

    Create an Annotation layer

    :param body: Annotation Layer schema
    :type body: dict | bytes

    """
    body = AnnotationLayerRestApiPost.from_dict(body)
    return web.Response(status=200)


async def annotation_layer_related_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """annotation_layer_related_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)
