# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_media_math_check_type_post(client):
    """Test case for media_math_check_type_post

    Check and normalize a TeX formula.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('q', 'q_example')
    response = await client.request(
        method='POST',
        path='/api/rest_v1/media/math/check/{type}'.format(type='type_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_math_formula_hash_get(client):
    """Test case for media_math_formula_hash_get

    Get a previously-stored formula
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/media/math/formula/{hash}'.format(hash='hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_math_render_format_hash_get(client):
    """Test case for media_math_render_format_hash_get

    Get rendered formula in the given format.
    """
    headers = { 
        'Accept': 'application/problem+json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/media/math/render/{format}/{hash}'.format(format='format_example', hash='hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

