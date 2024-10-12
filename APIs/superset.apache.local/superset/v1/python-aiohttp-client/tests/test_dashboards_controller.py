# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.dashboard_get200_response import DashboardGet200Response
from openapi_server.models.dashboard_id_or_slug_charts_get200_response import DashboardIdOrSlugChartsGet200Response
from openapi_server.models.dashboard_id_or_slug_datasets_get200_response import DashboardIdOrSlugDatasetsGet200Response
from openapi_server.models.dashboard_id_or_slug_get200_response import DashboardIdOrSlugGet200Response
from openapi_server.models.dashboard_pk_put200_response import DashboardPkPut200Response
from openapi_server.models.dashboard_post201_response import DashboardPost201Response
from openapi_server.models.dashboard_rest_api_post import DashboardRestApiPost
from openapi_server.models.dashboard_rest_api_put import DashboardRestApiPut
from openapi_server.models.get_fav_star_ids_schema import GetFavStarIdsSchema
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server.models.thumbnail_query_schema import ThumbnailQuerySchema


pytestmark = pytest.mark.asyncio

async def test_dashboard_delete(client):
    """Test case for dashboard_delete

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/dashboard/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_export_get(client):
    """Test case for dashboard_export_get

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/export/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_favorite_status_get(client):
    """Test case for dashboard_favorite_status_get

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/favorite_status/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_get(client):
    """Test case for dashboard_get

    
    """
    params = [('q', openapi_server.GetListSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_id_or_slug_charts_get(client):
    """Test case for dashboard_id_or_slug_charts_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/{id_or_slug}/charts'.format(id_or_slug='id_or_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_id_or_slug_datasets_get(client):
    """Test case for dashboard_id_or_slug_datasets_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/{id_or_slug}/datasets'.format(id_or_slug='id_or_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_id_or_slug_get(client):
    """Test case for dashboard_id_or_slug_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/{id_or_slug}'.format(id_or_slug='id_or_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_dashboard_import_post(client):
    """Test case for dashboard_import_post

    
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
        path='/dashboard/import/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_info_get(client):
    """Test case for dashboard_info_get

    
    """
    params = [('q', openapi_server.GetInfoSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_pk_delete(client):
    """Test case for dashboard_pk_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/dashboard/{pk}'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_pk_put(client):
    """Test case for dashboard_pk_put

    
    """
    body = openapi_server.DashboardRestApiPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/dashboard/{pk}'.format(pk=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_pk_thumbnail_digest_get(client):
    """Test case for dashboard_pk_thumbnail_digest_get

    
    """
    params = [('q', openapi_server.ThumbnailQuerySchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/{pk}/thumbnail/{digest}'.format(pk=56, digest='digest_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_post(client):
    """Test case for dashboard_post

    
    """
    body = openapi_server.DashboardRestApiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/dashboard/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboard_related_column_name_get(client):
    """Test case for dashboard_related_column_name_get

    
    """
    params = [('q', openapi_server.GetRelatedSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dashboard/related/{column_name}'.format(column_name='column_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

