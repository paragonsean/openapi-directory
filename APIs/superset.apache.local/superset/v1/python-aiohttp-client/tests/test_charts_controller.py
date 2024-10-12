# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.chart_cache_screenshot_response_schema import ChartCacheScreenshotResponseSchema
from openapi_server.models.chart_data_async_response_schema import ChartDataAsyncResponseSchema
from openapi_server.models.chart_data_query_context_schema import ChartDataQueryContextSchema
from openapi_server.models.chart_data_response_schema import ChartDataResponseSchema
from openapi_server.models.chart_get200_response import ChartGet200Response
from openapi_server.models.chart_pk_get200_response import ChartPkGet200Response
from openapi_server.models.chart_pk_put200_response import ChartPkPut200Response
from openapi_server.models.chart_post201_response import ChartPost201Response
from openapi_server.models.chart_rest_api_post import ChartRestApiPost
from openapi_server.models.chart_rest_api_put import ChartRestApiPut
from openapi_server.models.get_fav_star_ids_schema import GetFavStarIdsSchema
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server.models.screenshot_query_schema import ScreenshotQuerySchema


pytestmark = pytest.mark.asyncio

async def test_chart_data_cache_key_get(client):
    """Test case for chart_data_cache_key_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/data/{cache_key}'.format(cache_key='cache_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_data_post(client):
    """Test case for chart_data_post

    
    """
    body = {"result_type":"","datasource":{"id":0,"type":"druid"},"force":True,"result_format":"","queries":[{"is_timeseries":True,"columns":["columns","columns"],"having_filters":[{"val":["China","France","Japan"],"col":"country","op":"IN"},{"val":["China","France","Japan"],"col":"country","op":"IN"}],"apply_fetch_values_predicate":True,"timeseries_limit":5,"extras":"","timeseries_limit_metric":"","time_range":"Last week","time_offsets":["time_offsets","time_offsets"],"where":"where","post_processing":["",""],"time_shift":"time_shift","result_type":"","having":"having","is_rowcount":True,"orderby":[["my_col_1",False],["my_col_2",True]],"granularity_sqla":"granularity_sqla","filters":[{"val":["China","France","Japan"],"col":"country","op":"IN"},{"val":["China","France","Japan"],"col":"country","op":"IN"}],"groupby":["groupby","groupby"],"row_offset":0,"order_desc":True,"druid_time_origin":"druid_time_origin","annotation_layers":[{"color":"color","intervalEndColumn":"intervalEndColumn","show":True,"annotationType":"FORMULA","overrides":{"key":""},"timeColumn":"timeColumn","showMarkers":True,"titleColumn":"titleColumn","sourceType":"","hideLine":True,"name":"name","width":0.6027456,"style":"dashed","descriptionColumns":["descriptionColumns","descriptionColumns"],"opacity":"","value":""},{"color":"color","intervalEndColumn":"intervalEndColumn","show":True,"annotationType":"FORMULA","overrides":{"key":""},"timeColumn":"timeColumn","showMarkers":True,"titleColumn":"titleColumn","sourceType":"","hideLine":True,"name":"name","width":0.6027456,"style":"dashed","descriptionColumns":["descriptionColumns","descriptionColumns"],"opacity":"","value":""}],"url_params":{"key":"url_params"},"datasource":"","granularity":"granularity","row_limit":0,"metrics":["",""],"applied_time_extras":{"__time_range":"1 year ago : now"}},{"is_timeseries":True,"columns":["columns","columns"],"having_filters":[{"val":["China","France","Japan"],"col":"country","op":"IN"},{"val":["China","France","Japan"],"col":"country","op":"IN"}],"apply_fetch_values_predicate":True,"timeseries_limit":5,"extras":"","timeseries_limit_metric":"","time_range":"Last week","time_offsets":["time_offsets","time_offsets"],"where":"where","post_processing":["",""],"time_shift":"time_shift","result_type":"","having":"having","is_rowcount":True,"orderby":[["my_col_1",False],["my_col_2",True]],"granularity_sqla":"granularity_sqla","filters":[{"val":["China","France","Japan"],"col":"country","op":"IN"},{"val":["China","France","Japan"],"col":"country","op":"IN"}],"groupby":["groupby","groupby"],"row_offset":0,"order_desc":True,"druid_time_origin":"druid_time_origin","annotation_layers":[{"color":"color","intervalEndColumn":"intervalEndColumn","show":True,"annotationType":"FORMULA","overrides":{"key":""},"timeColumn":"timeColumn","showMarkers":True,"titleColumn":"titleColumn","sourceType":"","hideLine":True,"name":"name","width":0.6027456,"style":"dashed","descriptionColumns":["descriptionColumns","descriptionColumns"],"opacity":"","value":""},{"color":"color","intervalEndColumn":"intervalEndColumn","show":True,"annotationType":"FORMULA","overrides":{"key":""},"timeColumn":"timeColumn","showMarkers":True,"titleColumn":"titleColumn","sourceType":"","hideLine":True,"name":"name","width":0.6027456,"style":"dashed","descriptionColumns":["descriptionColumns","descriptionColumns"],"opacity":"","value":""}],"url_params":{"key":"url_params"},"datasource":"","granularity":"granularity","row_limit":0,"metrics":["",""],"applied_time_extras":{"__time_range":"1 year ago : now"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/chart/data',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_delete(client):
    """Test case for chart_delete

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/chart/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_export_get(client):
    """Test case for chart_export_get

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/export/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_favorite_status_get(client):
    """Test case for chart_favorite_status_get

    
    """
    params = [('q', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/favorite_status/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_get(client):
    """Test case for chart_get

    
    """
    params = [('q', openapi_server.GetListSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_chart_import_post(client):
    """Test case for chart_import_post

    
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
        path='/chart/import/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_info_get(client):
    """Test case for chart_info_get

    
    """
    params = [('q', openapi_server.GetInfoSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_pk_cache_screenshot_get(client):
    """Test case for chart_pk_cache_screenshot_get

    
    """
    params = [('q', openapi_server.ScreenshotQuerySchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/{pk}/cache_screenshot'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_pk_data_get(client):
    """Test case for chart_pk_data_get

    
    """
    params = [('format', 'format_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/{pk}/data'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_pk_delete(client):
    """Test case for chart_pk_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/chart/{pk}'.format(pk=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_pk_get(client):
    """Test case for chart_pk_get

    
    """
    params = [('q', openapi_server.GetItemSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/{pk}'.format(pk=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_pk_put(client):
    """Test case for chart_pk_put

    
    """
    body = openapi_server.ChartRestApiPut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/chart/{pk}'.format(pk=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_pk_screenshot_digest_get(client):
    """Test case for chart_pk_screenshot_digest_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/{pk}/screenshot/{digest}'.format(pk=56, digest='digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_pk_thumbnail_digest_get(client):
    """Test case for chart_pk_thumbnail_digest_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/{pk}/thumbnail/{digest}'.format(pk=56, digest='digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_post(client):
    """Test case for chart_post

    
    """
    body = openapi_server.ChartRestApiPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/chart/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_related_column_name_get(client):
    """Test case for chart_related_column_name_get

    
    """
    params = [('q', openapi_server.GetRelatedSchema())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/chart/related/{column_name}'.format(column_name='column_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

