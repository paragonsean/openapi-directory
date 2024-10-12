# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_config_update200_response import AccountConfigUpdate200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.bridge_delete200_response import BridgeDelete200Response
from openapi_server.models.cart_config_update200_response import CartConfigUpdate200Response
from openapi_server.models.category_add200_response import CategoryAdd200Response
from openapi_server.models.category_count200_response import CategoryCount200Response
from openapi_server.models.category_find200_response import CategoryFind200Response
from openapi_server.models.category_image_add200_response import CategoryImageAdd200Response
from openapi_server.models.category_info200_response import CategoryInfo200Response
from openapi_server.models.model_response_category_list import ModelResponseCategoryList


pytestmark = pytest.mark.asyncio

async def test_category_add(client):
    """Test case for category_add

    
    """
    params = [('name', 'name_example'),
                    ('parent_id', 'parent_id_example'),
                    ('stores_ids', '0'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('avail', True),
                    ('sort_order', 0),
                    ('created_time', 'created_time_example'),
                    ('modified_time', 'modified_time_example'),
                    ('description', 'description_example'),
                    ('meta_title', 'meta_title_example'),
                    ('meta_description', 'meta_description_example'),
                    ('meta_keywords', 'meta_keywords_example'),
                    ('seo_url', 'seo_url_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/category.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_assign(client):
    """Test case for category_assign

    
    """
    params = [('product_id', 'product_id_example'),
                    ('category_id', 'category_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/category.assign.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_count(client):
    """Test case for category_count

    
    """
    params = [('parent_id', 'parent_id_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('avail', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/category.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_delete(client):
    """Test case for category_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/category.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_find(client):
    """Test case for category_find

    
    """
    params = [('find_value', 'find_value_example'),
                    ('find_where', 'name'),
                    ('find_params', 'whole_words'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/category.find.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_image_add(client):
    """Test case for category_image_add

    
    """
    params = [('category_id', 'category_id_example'),
                    ('image_name', 'image_name_example'),
                    ('url', 'url_example'),
                    ('label', 'label_example'),
                    ('mime', 'mime_example'),
                    ('type', 'type_example'),
                    ('position', 0),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/category.image.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_image_delete(client):
    """Test case for category_image_delete

    
    """
    params = [('category_id', 'category_id_example'),
                    ('image_id', 'image_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/category.image.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_info(client):
    """Test case for category_info

    
    """
    params = [('id', 'id_example'),
                    ('params', 'id,parent_id,name,description'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/category.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_list(client):
    """Test case for category_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('page_cursor', 'page_cursor_example'),
                    ('parent_id', 'parent_id_example'),
                    ('params', 'id,parent_id,name,description'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('avail', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/category.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_unassign(client):
    """Test case for category_unassign

    
    """
    params = [('category_id', 'category_id_example'),
                    ('product_id', 'product_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/category.unassign.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_category_update(client):
    """Test case for category_update

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('parent_id', 'parent_id_example'),
                    ('stores_ids', '0'),
                    ('avail', True),
                    ('sort_order', 56),
                    ('modified_time', 'modified_time_example'),
                    ('description', 'description_example'),
                    ('meta_title', 'meta_title_example'),
                    ('meta_description', 'meta_description_example'),
                    ('meta_keywords', 'meta_keywords_example'),
                    ('seo_url', 'seo_url_example'),
                    ('lang_id', 'lang_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/category.update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

