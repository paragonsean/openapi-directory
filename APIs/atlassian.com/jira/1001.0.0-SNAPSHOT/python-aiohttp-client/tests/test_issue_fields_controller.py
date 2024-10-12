# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field_definition_json_bean import CustomFieldDefinitionJsonBean
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.field_details import FieldDetails
from openapi_server.models.page_bean_context import PageBeanContext
from openapi_server.models.page_bean_field import PageBeanField
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.update_custom_field_details import UpdateCustomFieldDetails


pytestmark = pytest.mark.asyncio

async def test_create_custom_field(client):
    """Test case for create_custom_field

    Create custom field
    """
    body = {"searcherKey":"com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher","name":"name","description":"description","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_field(client):
    """Test case for delete_custom_field

    Delete custom field
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/field/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contexts_for_field_deprecated(client):
    """Test case for get_contexts_for_field_deprecated

    Get contexts for a field
    """
    params = [('startAt', 0),
                    ('maxResults', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_id}/contexts'.format(field_id='field_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fields(client):
    """Test case for get_fields

    Get fields
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fields_paginated(client):
    """Test case for get_fields_paginated

    Get fields paginated
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('type', ['type_example']),
                    ('id', ['id_example']),
                    ('query', 'query_example'),
                    ('orderBy', 'order_by_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trashed_fields_paginated(client):
    """Test case for get_trashed_fields_paginated

    Get fields in trash paginated
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('id', ['id_example']),
                    ('query', 'query_example'),
                    ('expand', 'expand_example'),
                    ('orderBy', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/search/trashed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_custom_field(client):
    """Test case for restore_custom_field

    Restore custom field from trash
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field/{id}/restore'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trash_custom_field(client):
    """Test case for trash_custom_field

    Move custom field to trash
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field/{id}/trash'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_field(client):
    """Test case for update_custom_field

    Update custom field
    """
    body = {"searcherKey":"com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/field/{field_id}'.format(field_id='field_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

