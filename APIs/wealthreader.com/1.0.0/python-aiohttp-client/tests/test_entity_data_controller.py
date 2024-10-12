# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_data import EntityData
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_entities_get(client):
    """Test case for entities_get

    Obtiene el listado de entidades soportadas
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Wealth-Reader/api/1.0.0/entities',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_entities_post(client):
    """Test case for entities_post

    Obtiene los activos financieros y el detalle de su composición
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'otp': 'otp_example',
        'session': 'session_example',
        'api_key': 'api_key_example',
        'code': 'code_example',
        'contract_code': 'contract_code_example',
        'document_type': 'document_type_example',
        'password': 'password_example',
        'second_password': 'second_password_example',
        'token': 'token_example',
        'tokenize': False,
        'user': 'user_example'
        }
    response = await client.request(
        method='POST',
        path='/Wealth-Reader/api/1.0.0/entities',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_error_codes_get(client):
    """Test case for error_codes_get

    Listado de códigos de error
    """
    params = [('lang', es)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Wealth-Reader/api/1.0.0/error-codes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

