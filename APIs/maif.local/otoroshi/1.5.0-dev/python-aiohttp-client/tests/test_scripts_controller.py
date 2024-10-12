# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted import Deleted
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.script import Script
from openapi_server.models.script_compilation_result import ScriptCompilationResult


pytestmark = pytest.mark.asyncio

async def test_compile_script(client):
    """Test case for compile_script

    Compile a script
    """
    body = {"code":{"key":"value"},"name":"a string value","id":"a string value","desc":{"key":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/scripts/_compile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_script(client):
    """Test case for create_script

    Create a new script
    """
    body = {"code":{"key":"value"},"name":"a string value","id":"a string value","desc":{"key":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/scripts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_script(client):
    """Test case for delete_script

    Delete a script
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/scripts/{script_id}'.format(script_id='script_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_all_scripts(client):
    """Test case for find_all_scripts

    Get all scripts
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/scripts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_script_by_id(client):
    """Test case for find_script_by_id

    Get a script
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/scripts/{script_id}'.format(script_id='script_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_script(client):
    """Test case for patch_script

    Update a script with a diff
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/scripts/{script_id}'.format(script_id='script_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_script(client):
    """Test case for update_script

    Update a script
    """
    body = {"code":{"key":"value"},"name":"a string value","id":"a string value","desc":{"key":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/scripts/{script_id}'.format(script_id='script_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

