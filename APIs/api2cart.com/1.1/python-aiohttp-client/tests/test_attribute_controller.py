# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_add200_response import AttributeAdd200Response
from openapi_server.models.attribute_assign_group200_response import AttributeAssignGroup200Response
from openapi_server.models.attribute_attributeset_list200_response import AttributeAttributesetList200Response
from openapi_server.models.attribute_count200_response import AttributeCount200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.attribute_info200_response import AttributeInfo200Response
from openapi_server.models.attribute_type_list200_response import AttributeTypeList200Response
from openapi_server.models.attribute_unassign_group200_response import AttributeUnassignGroup200Response
from openapi_server.models.attribute_update200_response import AttributeUpdate200Response
from openapi_server.models.model_response_attribute_list import ModelResponseAttributeList


pytestmark = pytest.mark.asyncio

async def test_attribute_add(client):
    """Test case for attribute_add

    
    """
    params = [('type', 'type_example'),
                    ('code', 'code_example'),
                    ('name', 'name_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('visible', False),
                    ('required', False),
                    ('position', 0),
                    ('attribute_group_id', 'attribute_group_id_example'),
                    ('is_global', 'Store'),
                    ('is_searchable', False),
                    ('is_filterable', 'false'),
                    ('is_comparable', False),
                    ('is_html_allowed_on_front', False),
                    ('is_filterable_in_search', False),
                    ('is_configurable', False),
                    ('is_visible_in_advanced_search', False),
                    ('is_used_for_promo_rules', False),
                    ('used_in_product_listing', False),
                    ('used_for_sort_by', False),
                    ('apply_to', 'all_types')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/attribute.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_assign_group(client):
    """Test case for attribute_assign_group

    
    """
    params = [('id', 'id_example'),
                    ('group_id', 'group_id_example'),
                    ('attribute_set_id', 'attribute_set_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/attribute.assign.group.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_assign_set(client):
    """Test case for attribute_assign_set

    
    """
    params = [('id', 'id_example'),
                    ('group_id', 'group_id_example'),
                    ('attribute_set_id', 'attribute_set_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/attribute.assign.set.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_attributeset_list(client):
    """Test case for attribute_attributeset_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('params', 'id,name'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/attribute.attributeset.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_count(client):
    """Test case for attribute_count

    
    """
    params = [('type', 'type_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('visible', True),
                    ('required', True),
                    ('system', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/attribute.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_delete(client):
    """Test case for attribute_delete

    
    """
    params = [('store_id', 'store_id_example'),
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/attribute.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_group_list(client):
    """Test case for attribute_group_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('lang_id', 'lang_id_example'),
                    ('params', 'id,name'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example'),
                    ('attribute_set_id', 'attribute_set_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/attribute.group.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_info(client):
    """Test case for attribute_info

    
    """
    params = [('id', 'id_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('params', 'force_all'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/attribute.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_list(client):
    """Test case for attribute_list

    
    """
    params = [('start', 0),
                    ('count', 10),
                    ('type', 'type_example'),
                    ('attribute_ids', 'attribute_ids_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('params', 'id,name,code,type'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example'),
                    ('visible', True),
                    ('required', True),
                    ('system', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/attribute.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_type_list(client):
    """Test case for attribute_type_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/attribute.type.list.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_unassign_group(client):
    """Test case for attribute_unassign_group

    
    """
    params = [('id', 'id_example'),
                    ('group_id', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/attribute.unassign.group.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_unassign_set(client):
    """Test case for attribute_unassign_set

    
    """
    params = [('id', 'id_example'),
                    ('attribute_set_id', 'attribute_set_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/attribute.unassign.set.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_update(client):
    """Test case for attribute_update

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/attribute.update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

