# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_delete(client):
    """Test case for annotation_layer_delete

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/annotation_layer/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_get(client):
    """Test case for annotation_layer_get

    
    """
    params = [('q', openapi_server.GetListSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/annotation_layer/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_info_get(client):
    """Test case for annotation_layer_info_get

    
    """
    params = [('q', openapi_server.GetInfoSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/annotation_layer/_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_annotation_annotation_id_delete(client):
    """Test case for annotation_layer_pk_annotation_annotation_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/annotation_layer/{pk}/annotation/{annotation_id}'.format(pk=56, annotation_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_annotation_annotation_id_get(client):
    """Test case for annotation_layer_pk_annotation_annotation_id_get

    
    """
    params = [('q', openapi_server.GetItemSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/annotation_layer/{pk}/annotation/{annotation_id}'.format(pk=56, annotation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_annotation_annotation_id_put(client):
    """Test case for annotation_layer_pk_annotation_annotation_id_put

    
    """
    body = openapi_server.AnnotationRestApiPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/annotation_layer/{pk}/annotation/{annotation_id}'.format(pk=56, annotation_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_annotation_delete(client):
    """Test case for annotation_layer_pk_annotation_delete

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/annotation_layer/{pk}/annotation'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_annotation_get(client):
    """Test case for annotation_layer_pk_annotation_get

    
    """
    params = [('q', openapi_server.GetListSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/annotation_layer/{pk}/annotation'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_annotation_post(client):
    """Test case for annotation_layer_pk_annotation_post

    
    """
    body = openapi_server.AnnotationRestApiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/annotation_layer/{pk}/annotation'.format(pk=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_delete(client):
    """Test case for annotation_layer_pk_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/annotation_layer/{pk}'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_get(client):
    """Test case for annotation_layer_pk_get

    
    """
    params = [('q', openapi_server.GetItemSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/annotation_layer/{pk}'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_pk_put(client):
    """Test case for annotation_layer_pk_put

    
    """
    body = openapi_server.AnnotationLayerRestApiPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/annotation_layer/{pk}'.format(pk=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_post(client):
    """Test case for annotation_layer_post

    
    """
    body = openapi_server.AnnotationLayerRestApiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/annotation_layer/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotation_layer_related_column_name_get(client):
    """Test case for annotation_layer_related_column_name_get

    
    """
    params = [('q', openapi_server.GetRelatedSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/annotation_layer/related/{column_name}'.format(column_name='column_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

