# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_model_body import CreateModelBody
from openapi_server.models.model import Model
from openapi_server.models.model_quote import ModelQuote


pytestmark = pytest.mark.asyncio

async def test_model_get(client):
    """Test case for model_get

    Retrieve the models you've created. 
    """
    headers = { 
        'Accept': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/2/model',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_model_id_get(client):
    """Test case for model_model_id_get

    Retrieve a previously created model by its id. 
    """
    headers = { 
        'Accept': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/2/model/{model_id}'.format(model_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_model_post(client):
    """Test case for model_post

    Models represent 3D design files that you'd like to produce. Creating models is generally the first step in creating an order. 
    """
    body = openapi_server.CreateModelBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/2/model',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_quote_attrs_get(client):
    """Test case for model_quote_attrs_get

    Get a quote for a model with the given attributes. 
    """
    params = [('x', 3.4),
                    ('y', 3.4),
                    ('z', 3.4),
                    ('volume', 3.4),
                    ('surface_area', 3.4),
                    ('material_id', 3.4),
                    ('quantity', 3.4),
                    ('units', 'units_example'),
                    ('options[orientation]', True)]
    headers = { 
        'Accept': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/2/model/quote_attrs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_quote_get(client):
    """Test case for model_quote_get

    Get a quote a given model id. 
    """
    params = [('model_id', 56),
                    ('material_id', 3.4),
                    ('quantity', 3.4),
                    ('units', 'units_example'),
                    ('options[orientation]', True)]
    headers = { 
        'Accept': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/2/model/quote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

