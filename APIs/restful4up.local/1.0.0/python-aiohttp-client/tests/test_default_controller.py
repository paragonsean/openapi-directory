# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.apply_yara_rules200_response import ApplyYaraRules200Response
from openapi_server.models.emulation_output200_response import EmulationOutput200Response
from openapi_server.models.error import Error
from openapi_server.models.generate_partial_yara_rule200_response import GeneratePartialYaraRule200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_apply_yara_rules(client):
    """Test case for apply_yara_rules

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('is_unpacking_required', 'is_unpacking_required_example')
    data.add_field('rules', ['rules_example'])
    response = await client.request(
        method='POST',
        path='/apply-yara-rules',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clean(client):
    """Test case for clean

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='HEAD',
        path='/clean',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_emulation_output(client):
    """Test case for emulation_output

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/emulation-output',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_generate_partial_yara_rule(client):
    """Test case for generate_partial_yara_rule

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('is_unpacking_required', 'is_unpacking_required_example')
    data.add_field('minimum_string_length', 'minimum_string_length_example')
    data.add_field('strings_to_ignore', ['strings_to_ignore_example'])
    response = await client.request(
        method='POST',
        path='/generate-partial-yara-rules',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_unpack(client):
    """Test case for unpack

    
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/unpack',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

