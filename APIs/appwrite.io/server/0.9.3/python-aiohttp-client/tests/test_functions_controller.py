# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.execution import Execution
from openapi_server.models.execution_list import ExecutionList
from openapi_server.models.function import Function
from openapi_server.models.function_list import FunctionList
from openapi_server.models.functions_create_execution_request import FunctionsCreateExecutionRequest
from openapi_server.models.functions_create_request import FunctionsCreateRequest
from openapi_server.models.functions_update_request import FunctionsUpdateRequest
from openapi_server.models.functions_update_tag_request import FunctionsUpdateTagRequest
from openapi_server.models.tag import Tag
from openapi_server.models.tag_list import TagList


pytestmark = pytest.mark.asyncio

async def test_functions_create(client):
    """Test case for functions_create

    Create Function
    """
    body = openapi_server.FunctionsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/functions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_create_execution(client):
    """Test case for functions_create_execution

    Create Execution
    """
    body = openapi_server.FunctionsCreateExecutionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/functions/{function_id}/executions'.format(function_id='function_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_functions_create_tag(client):
    """Test case for functions_create_tag

    Create Tag
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    data = FormData()
    data.add_field('code', 'code_example')
    data.add_field('command', 'command_example')
    response = await client.request(
        method='POST',
        path='/v1/functions/{function_id}/tags'.format(function_id='function_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_delete(client):
    """Test case for functions_delete

    Delete Function
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/functions/{function_id}'.format(function_id='function_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_delete_tag(client):
    """Test case for functions_delete_tag

    Delete Tag
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/functions/{function_id}/tags/{tag_id}'.format(function_id='function_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_get(client):
    """Test case for functions_get

    Get Function
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/functions/{function_id}'.format(function_id='function_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_get_execution(client):
    """Test case for functions_get_execution

    Get Execution
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/functions/{function_id}/executions/{execution_id}'.format(function_id='function_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_get_tag(client):
    """Test case for functions_get_tag

    Get Tag
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/functions/{function_id}/tags/{tag_id}'.format(function_id='function_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_list(client):
    """Test case for functions_list

    List Functions
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/functions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_list_executions(client):
    """Test case for functions_list_executions

    List Executions
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/functions/{function_id}/executions'.format(function_id='function_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_list_tags(client):
    """Test case for functions_list_tags

    List Tags
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/functions/{function_id}/tags'.format(function_id='function_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_update(client):
    """Test case for functions_update

    Update Function
    """
    body = openapi_server.FunctionsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/functions/{function_id}'.format(function_id='function_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_update_tag(client):
    """Test case for functions_update_tag

    Update Function Tag
    """
    body = openapi_server.FunctionsUpdateTagRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/functions/{function_id}/tag'.format(function_id='function_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

