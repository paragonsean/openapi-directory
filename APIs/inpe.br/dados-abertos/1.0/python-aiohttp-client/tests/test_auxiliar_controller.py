# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_estados_auxiliar_resource(client):
    """Test case for get_estados_auxiliar_resource

    Endpoint para retorno dos dados de estados utilizados na filtragem de focos
    """
    params = [('pais_id', [56])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/auxiliar/estados',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_municipios_auxiliar_resource(client):
    """Test case for get_municipios_auxiliar_resource

    Endpoint para retorno dos dados de municípios utilizados na filtragem de focos
    """
    params = [('pais_id', 56),
                    ('estado_id', [56])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/auxiliar/municipios',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_paises_auxiliar_resource(client):
    """Test case for get_paises_auxiliar_resource

    Endpoint para retorno dos dados de países utilizados na filtragem de focos
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/auxiliar/paises',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_satelite_auxiliar_resource(client):
    """Test case for get_satelite_auxiliar_resource

    Endpoint para retorno dos dados de satélites utilizados na filtragem de focos
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/auxiliar/satelites',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

