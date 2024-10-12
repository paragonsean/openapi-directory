# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_response_public_action_function_identifier_no_paging import CollectionResponsePublicActionFunctionIdentifierNoPaging
from openapi_server.models.error import Error
from openapi_server.models.public_action_function import PublicActionFunction
from openapi_server.models.public_action_function_identifier import PublicActionFunctionIdentifier


pytestmark = pytest.mark.asyncio

async def test_delete_automation_v4_actions_app_id_definition_id_functions_function_type_archive_by_function_type(client):
    """Test case for delete_automation_v4_actions_app_id_definition_id_functions_function_type_archive_by_function_type

    Delete a function for a definition
    """
    headers = { 
        'Accept': '*/*',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}'.format(definition_id='definition_id_example', function_type='function_type_example', app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_archive(client):
    """Test case for delete_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_archive

    Archive a function for a definition
    """
    headers = { 
        'Accept': '*/*',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}'.format(definition_id='definition_id_example', function_type='function_type_example', function_id='function_id_example', app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_get_by_id(client):
    """Test case for get_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_get_by_id

    Get a function for a given definition
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}'.format(definition_id='definition_id_example', function_type='function_type_example', function_id='function_id_example', app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automation_v4_actions_app_id_definition_id_functions_function_type_get_by_function_type(client):
    """Test case for get_automation_v4_actions_app_id_definition_id_functions_function_type_get_by_function_type

    Get all functions by a type for a given definition
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}'.format(definition_id='definition_id_example', function_type='function_type_example', app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automation_v4_actions_app_id_definition_id_functions_get_page(client):
    """Test case for get_automation_v4_actions_app_id_definition_id_functions_get_page

    Get all functions for a given definition
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/automation/v4/actions/{app_id}/{definition_id}/functions'.format(definition_id='definition_id_example', app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_put_automation_v4_actions_app_id_definition_id_functions_function_type_create_or_replace_by_function_type(client):
    """Test case for put_automation_v4_actions_app_id_definition_id_functions_function_type_create_or_replace_by_function_type

    Insert a function for a definition
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}'.format(definition_id='definition_id_example', function_type='function_type_example', app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_put_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_create_or_replace(client):
    """Test case for put_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_create_or_replace

    Insert a function for a definition
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}'.format(definition_id='definition_id_example', function_type='function_type_example', function_id='function_id_example', app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

