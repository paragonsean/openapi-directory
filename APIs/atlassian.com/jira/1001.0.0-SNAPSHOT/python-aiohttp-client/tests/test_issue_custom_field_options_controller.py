# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_custom_field_option_create_request import BulkCustomFieldOptionCreateRequest
from openapi_server.models.bulk_custom_field_option_update_request import BulkCustomFieldOptionUpdateRequest
from openapi_server.models.custom_field_created_context_options_list import CustomFieldCreatedContextOptionsList
from openapi_server.models.custom_field_option import CustomFieldOption
from openapi_server.models.custom_field_updated_context_options_list import CustomFieldUpdatedContextOptionsList
from openapi_server.models.order_of_custom_field_options import OrderOfCustomFieldOptions
from openapi_server.models.page_bean_custom_field_context_option import PageBeanCustomFieldContextOption


pytestmark = pytest.mark.asyncio

async def test_create_custom_field_option(client):
    """Test case for create_custom_field_option

    Create custom field options (context)
    """
    body = {"options":[{"disabled":True,"optionId":"optionId","value":"value"},{"disabled":True,"optionId":"optionId","value":"value"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field/{field_id}/context/{context_id}/option'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_field_option(client):
    """Test case for delete_custom_field_option

    Delete custom field options (context)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/field/{field_id}/context/{context_id}/option/{option_id}'.format(field_id='field_id_example', context_id=56, option_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_field_option(client):
    """Test case for get_custom_field_option

    Get custom field option
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/customFieldOption/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_options_for_context(client):
    """Test case for get_options_for_context

    Get custom field options (context)
    """
    params = [('optionId', 56),
                    ('onlyOptions', False),
                    ('startAt', 0),
                    ('maxResults', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_id}/context/{context_id}/option'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reorder_custom_field_options(client):
    """Test case for reorder_custom_field_options

    Reorder custom field options (context)
    """
    body = {"after":"after","position":"First","customFieldOptionIds":["customFieldOptionIds","customFieldOptionIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/field/{field_id}/context/{context_id}/option/move'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_field_option(client):
    """Test case for update_custom_field_option

    Update custom field options (context)
    """
    body = {"options":[{"disabled":True,"id":"id","value":"value"},{"disabled":True,"id":"id","value":"value"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/field/{field_id}/context/{context_id}/option'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

