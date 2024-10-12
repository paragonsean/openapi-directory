from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.database_available_get200_response_inner import DatabaseAvailableGet200ResponseInner
from openapi_server.models.database_function_names_response import DatabaseFunctionNamesResponse
from openapi_server.models.database_get200_response import DatabaseGet200Response
from openapi_server.models.database_pk_get200_response import DatabasePkGet200Response
from openapi_server.models.database_pk_put200_response import DatabasePkPut200Response
from openapi_server.models.database_post201_response import DatabasePost201Response
from openapi_server.models.database_related_objects_response import DatabaseRelatedObjectsResponse
from openapi_server.models.database_rest_api_post import DatabaseRestApiPost
from openapi_server.models.database_rest_api_put import DatabaseRestApiPut
from openapi_server.models.database_schemas_query_schema import DatabaseSchemasQuerySchema
from openapi_server.models.database_test_connection_schema import DatabaseTestConnectionSchema
from openapi_server.models.database_validate_parameters_schema import DatabaseValidateParametersSchema
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.schemas_response_schema import SchemasResponseSchema
from openapi_server.models.select_star_response_schema import SelectStarResponseSchema
from openapi_server.models.table_metadata_response_schema import TableMetadataResponseSchema
from openapi_server import util


async def database_available_get(request: web.Request, ) -> web.Response:
    """database_available_get

    Get names of databases currently available


    """
    return web.Response(status=200)


async def database_export_get(request: web.Request, q=None) -> web.Response:
    """database_export_get

    Download database(s) and associated dataset(s) as a zip file

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def database_get(request: web.Request, q=None) -> web.Response:
    """database_get

    Get a list of models

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def database_import_post(request: web.Request, form_data=None, overwrite=None, passwords=None) -> web.Response:
    """database_import_post

    

    :param form_data: upload file (ZIP)
    :type form_data: str
    :param overwrite: overwrite existing databases?
    :type overwrite: bool
    :param passwords: JSON map of passwords for each file
    :type passwords: str

    """
    return web.Response(status=200)


async def database_info_get(request: web.Request, q=None) -> web.Response:
    """database_info_get

    Get metadata information about this API resource

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def database_pk_delete(request: web.Request, pk) -> web.Response:
    """database_pk_delete

    Deletes a Database.

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def database_pk_function_names_get(request: web.Request, pk) -> web.Response:
    """database_pk_function_names_get

    Get function names supported by a database

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def database_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """database_pk_get

    Get an item model

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def database_pk_put(request: web.Request, pk, body) -> web.Response:
    """database_pk_put

    Changes a Database.

    :param pk: 
    :type pk: int
    :param body: Database schema
    :type body: dict | bytes

    """
    body = DatabaseRestApiPut.from_dict(body)
    return web.Response(status=200)


async def database_pk_related_objects_get(request: web.Request, pk) -> web.Response:
    """database_pk_related_objects_get

    Get charts and dashboards count associated to a database

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def database_pk_schemas_get(request: web.Request, pk, q=None) -> web.Response:
    """database_pk_schemas_get

    Get all schemas from a database

    :param pk: The database id
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def database_pk_select_star_table_name_get(request: web.Request, pk, table_name, schema_name) -> web.Response:
    """database_pk_select_star_table_name_get

    Get database select star for table

    :param pk: The database id
    :type pk: int
    :param table_name: Table name
    :type table_name: str
    :param schema_name: Table schema
    :type schema_name: str

    """
    return web.Response(status=200)


async def database_pk_select_star_table_name_schema_name_get(request: web.Request, pk, table_name, schema_name) -> web.Response:
    """database_pk_select_star_table_name_schema_name_get

    Get database select star for table

    :param pk: The database id
    :type pk: int
    :param table_name: Table name
    :type table_name: str
    :param schema_name: Table schema
    :type schema_name: str

    """
    return web.Response(status=200)


async def database_pk_table_table_name_schema_name_get(request: web.Request, pk, table_name, schema_name) -> web.Response:
    """database_pk_table_table_name_schema_name_get

    Get database table metadata

    :param pk: The database id
    :type pk: int
    :param table_name: Table name
    :type table_name: str
    :param schema_name: Table schema
    :type schema_name: str

    """
    return web.Response(status=200)


async def database_post(request: web.Request, body) -> web.Response:
    """database_post

    Create a new Database.

    :param body: Database schema
    :type body: dict | bytes

    """
    body = DatabaseRestApiPost.from_dict(body)
    return web.Response(status=200)


async def database_test_connection_post(request: web.Request, body) -> web.Response:
    """database_test_connection_post

    Tests a database connection

    :param body: Database schema
    :type body: dict | bytes

    """
    body = DatabaseTestConnectionSchema.from_dict(body)
    return web.Response(status=200)


async def database_validate_parameters_post(request: web.Request, body) -> web.Response:
    """database_validate_parameters_post

    Validates parameters used to connect to a database

    :param body: DB-specific parameters
    :type body: dict | bytes

    """
    body = DatabaseValidateParametersSchema.from_dict(body)
    return web.Response(status=200)
