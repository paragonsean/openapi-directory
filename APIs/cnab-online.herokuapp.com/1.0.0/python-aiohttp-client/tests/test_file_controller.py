# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.error import Error
from openapi_server.models.file_file_id_lines_get200_response import FileFileIdLinesGet200Response
from openapi_server.models.file_file_id_occurrences_get200_response import FileFileIdOccurrencesGet200Response
from openapi_server.models.file_post200_response import FilePost200Response


pytestmark = pytest.mark.asyncio

async def test_file_file_id_get(client):
    """Test case for file_file_id_get

    Retorna as informações básicas de um arquivo previamente processado
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/file/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_file_id_lines_get(client):
    """Test case for file_file_id_lines_get

    Retorna todas as linhas e seus respectivos campos (de forma não processada, apenas indicando os campos reconhecidos)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/file/{file_id}/lines'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_file_id_occurrences_get(client):
    """Test case for file_file_id_occurrences_get

    Retorna as informações de baixa de boletos e outros tipos de ocorrências
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/file/{file_id}/occurrences'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_file_post(client):
    """Test case for file_post

    Faz o upload de um arquivo
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/file',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

