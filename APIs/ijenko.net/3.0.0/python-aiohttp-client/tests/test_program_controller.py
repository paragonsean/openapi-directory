# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.program import Program
from openapi_server.models.program_created import ProgramCreated
from openapi_server.models.program_item import ProgramItem
from openapi_server.models.program_log import ProgramLog
from openapi_server.models.program_new import ProgramNew
from openapi_server.models.program_patch import ProgramPatch


pytestmark = pytest.mark.asyncio

async def test_place_new_program(client):
    """Test case for place_new_program

    Create a Program
    """
    program_info = {"code":[],"enabled":False,"name":"NOOP"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/places/{place_id}/programs'.format(place_id='place_id_example'),
        headers=headers,
        json=program_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_programs(client):
    """Test case for place_programs

    List Programs
    """
    params = [('embed-metadata', ['embed_metadata_example'])]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/programs'.format(place_id='place_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_program_delete(client):
    """Test case for program_delete

    Delete a Program
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/programs/{program_id}'.format(program_id='program_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_program_get_metadata(client):
    """Test case for program_get_metadata

    List metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/programs/{program_id}/metadata'.format(program_id='program_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_program_log(client):
    """Test case for program_log

    History of executions of a Program
    """
    params = [('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/programs/{program_id}/log'.format(program_id='program_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_program_patch(client):
    """Test case for program_patch

    Modify a Program
    """
    program_patch = {"code":"{}","name":"name","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/programs/{program_id}'.format(program_id='program_id_example'),
        headers=headers,
        json=program_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_program_patch_metadata(client):
    """Test case for program_patch_metadata

    Modify metadata of a Program
    """
    metadata_patch = {"add":{},"remove":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/programs/{program_id}/metadata'.format(program_id='program_id_example'),
        headers=headers,
        json=metadata_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_program_run(client):
    """Test case for program_run

    Run the Program
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/programs/{program_id}/run'.format(program_id='program_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_programs_get(client):
    """Test case for programs_get

    Information about a Program
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/programs/{program_id}'.format(program_id='program_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

