# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

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


pytestmark = pytest.mark.asyncio

async def test_dataset_delete(client):
    """Test case for dataset_delete

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/dataset/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_distinct_column_name_get(client):
    """Test case for dataset_distinct_column_name_get

    
    """
    params = [('q', openapi_server.GetRelatedSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dataset/distinct/{column_name}'.format(column_name='column_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_export_get(client):
    """Test case for dataset_export_get

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dataset/export/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_get(client):
    """Test case for dataset_get

    
    """
    params = [('q', openapi_server.GetListSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dataset/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_dataset_import_post(client):
    """Test case for dataset_import_post

    
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
        path='/dataset/import/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_info_get(client):
    """Test case for dataset_info_get

    
    """
    params = [('q', openapi_server.GetInfoSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dataset/_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_pk_column_column_id_delete(client):
    """Test case for dataset_pk_column_column_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/dataset/{pk}/column/{column_id}'.format(pk=56, column_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_pk_delete(client):
    """Test case for dataset_pk_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/dataset/{pk}'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_pk_get(client):
    """Test case for dataset_pk_get

    
    """
    params = [('q', openapi_server.GetItemSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dataset/{pk}'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_pk_metric_metric_id_delete(client):
    """Test case for dataset_pk_metric_metric_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/dataset/{pk}/metric/{metric_id}'.format(pk=56, metric_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_pk_put(client):
    """Test case for dataset_pk_put

    
    """
    body = openapi_server.DatasetRestApiPut()
    params = [('override_columns', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/dataset/{pk}'.format(pk=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_pk_refresh_put(client):
    """Test case for dataset_pk_refresh_put

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/dataset/{pk}/refresh'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_pk_related_objects_get(client):
    """Test case for dataset_pk_related_objects_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dataset/{pk}/related_objects'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_post(client):
    """Test case for dataset_post

    
    """
    body = openapi_server.DatasetRestApiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/dataset/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dataset_related_column_name_get(client):
    """Test case for dataset_related_column_name_get

    
    """
    params = [('q', openapi_server.GetRelatedSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dataset/related/{column_name}'.format(column_name='column_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

