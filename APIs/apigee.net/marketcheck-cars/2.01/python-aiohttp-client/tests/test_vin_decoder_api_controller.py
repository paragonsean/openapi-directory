# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build import Build
from openapi_server.models.error import Error
from openapi_server.models.neo_vin import NeoVIN
from openapi_server.models.specs_auto_complete_response import SpecsAutoCompleteResponse


pytestmark = pytest.mark.asyncio

async def test_decode(client):
    """Test case for decode

    VIN Decoder
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/decode/car/{vin}/specs'.format(vin='vin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_decode_via_epi(client):
    """Test case for decode_via_epi

    EPI VIN Decoder
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/decode/car/epi/{vin}/specs'.format(vin='vin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_decode_via_neo_vin(client):
    """Test case for decode_via_neo_vin

    NeoVIN Decoder
    """
    params = [('api_key', 'api_key_example'),
                    ('include_generic', False),
                    ('force_decode', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/decode/car/neovin/{vin}/specs'.format(vin='vin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_taxonomy_terms(client):
    """Test case for get_taxonomy_terms

    API for getting terms from taxonomy
    """
    params = [('api_key', 'api_key_example'),
                    ('field', '_field_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('transmission', 'transmission_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_block', 'engine_block_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/specs/car/terms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specs_car_auto_complete_get(client):
    """Test case for specs_car_auto_complete_get

    API for auto-completion of inputs based on taxonomy
    """
    params = [('api_key', 'api_key_example'),
                    ('field', '_field_example'),
                    ('input', 'input_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('transmission', 'transmission_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_block', 'engine_block_example'),
                    ('ignore_case', True),
                    ('facet_min_count', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/specs/car/auto-complete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

