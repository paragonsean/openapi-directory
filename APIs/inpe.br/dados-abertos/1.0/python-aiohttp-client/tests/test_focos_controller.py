# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_focos_count_resource(client):
    """Test case for get_focos_count_resource

    Endpoint para retorno da contagem dos focos de calor
    """
    params = [('pais_id', 56),
                    ('estado_id', 56),
                    ('municipio_id', 56),
                    ('satelite', ['satelite_example'])]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/focos/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_focos_resource(client):
    """Test case for get_focos_resource

    Endpoint para retorno dos dados de focos de calor
    """
    params = [('pais_id', 56),
                    ('estado_id', 56),
                    ('municipio_id', 56),
                    ('satelite', ['satelite_example'])]
    headers = { 
        'x_fields': 'x_fields_example',
    }
    response = await client.request(
        method='GET',
        path='/api/focos/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

