# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

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


pytestmark = pytest.mark.asyncio

async def test_database_available_get(client):
    """Test case for database_available_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/available/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_export_get(client):
    """Test case for database_export_get

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/export/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_get(client):
    """Test case for database_get

    
    """
    params = [('q', openapi_server.GetListSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_database_import_post(client):
    """Test case for database_import_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('form_data', '/path/to/file')
    data.add_field('overwrite', True)
    data.add_field('passwords', 'passwords_example')
    response = await client.request(
        method='POST',
        path='/database/import/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_info_get(client):
    """Test case for database_info_get

    
    """
    params = [('q', openapi_server.GetInfoSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_delete(client):
    """Test case for database_pk_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/database/{pk}'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_function_names_get(client):
    """Test case for database_pk_function_names_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/{pk}/function_names'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_get(client):
    """Test case for database_pk_get

    
    """
    params = [('q', openapi_server.GetItemSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/{pk}'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_put(client):
    """Test case for database_pk_put

    
    """
    body = openapi_server.DatabaseRestApiPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/database/{pk}'.format(pk=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_related_objects_get(client):
    """Test case for database_pk_related_objects_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/{pk}/related_objects'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_schemas_get(client):
    """Test case for database_pk_schemas_get

    
    """
    params = [('q', openapi_server.DatabaseSchemasQuerySchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/{pk}/schemas'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_select_star_table_name_get(client):
    """Test case for database_pk_select_star_table_name_get

    
    """
    params = [('schema_name', 'schema_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/{pk}/select_star/{table_name}'.format(pk=56, table_name='table_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_select_star_table_name_schema_name_get(client):
    """Test case for database_pk_select_star_table_name_schema_name_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/{pk}/select_star/{table_name}/{schema_name}'.format(pk=56, table_name='table_name_example', schema_name='schema_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_pk_table_table_name_schema_name_get(client):
    """Test case for database_pk_table_table_name_schema_name_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/database/{pk}/table/{table_name}/{schema_name}'.format(pk=56, table_name='table_name_example', schema_name='schema_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_post(client):
    """Test case for database_post

    
    """
    body = openapi_server.DatabaseRestApiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/database/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_test_connection_post(client):
    """Test case for database_test_connection_post

    
    """
    body = {"impersonate_user":True,"server_cert":"server_cert","configuration_method":"","database_name":"database_name","engine":"engine","extra":"extra","sqlalchemy_uri":"sqlalchemy_uri","parameters":{"key":""},"encrypted_extra":"encrypted_extra"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/database/test_connection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_validate_parameters_post(client):
    """Test case for database_validate_parameters_post

    
    """
    body = {"impersonate_user":True,"server_cert":"server_cert","configuration_method":"","database_name":"database_name","engine":"engine","extra":"extra","parameters":{"key":""},"encrypted_extra":"encrypted_extra"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/database/validate_parameters',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

