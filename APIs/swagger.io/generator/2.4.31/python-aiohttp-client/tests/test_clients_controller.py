# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cli_option import CliOption
from openapi_server.models.generator_input import GeneratorInput
from openapi_server.models.response_code import ResponseCode


pytestmark = pytest.mark.asyncio

async def test_client_options(client):
    """Test case for client_options

    Gets languages supported by the client generator
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/gen/clients',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_file(client):
    """Test case for download_file

    Downloads a pre-generated file
    """
    headers = { 
        'Accept': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/gen/download/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_generate_client(client):
    """Test case for generate_client

    Generates a client library
    """
    body = openapi_server.GeneratorInput()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/gen/clients/{language}'.format(language='language_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_client_options(client):
    """Test case for get_client_options

    Returns options for a client library
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/gen/clients/{language}'.format(language='language_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

