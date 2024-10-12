# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cli_option import CliOption
from openapi_server.models.generator_input import GeneratorInput
from openapi_server.models.response_code import ResponseCode


pytestmark = pytest.mark.asyncio

async def test_download_file_0(client):
    """Test case for download_file_0

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

async def test_generate_server_for_language(client):
    """Test case for generate_server_for_language

    Generates a server library
    """
    body = {"options":{"key":"options"},"authorizationValue":{"urlMatcher":"{}","keyName":"keyName","type":"type","value":"value"},"openAPIUrl":"https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/modules/openapi-generator/src/test/resources/2_0/petstore.yaml","spec":"{}"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/gen/servers/{framework}'.format(framework='framework_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_options(client):
    """Test case for get_server_options

    Returns options for a server framework
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/gen/servers/{framework}'.format(framework='framework_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_options(client):
    """Test case for server_options

    Gets languages supported by the server generator
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/gen/servers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

