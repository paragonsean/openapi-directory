# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v20_database_assemblies_barcode_get_request import ApiV20DatabaseAssembliesBarcodeGetRequest


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_assemblies_barcode_get(client):
    """Test case for api_v20_database_assemblies_barcode_get

    
    """
    body = openapi_server.ApiV20DatabaseAssembliesBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/assemblies/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_assemblies_barcode_post(client):
    """Test case for api_v20_database_assemblies_barcode_post

    
    """
    body = openapi_server.ApiV20DatabaseAssembliesBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2.0/{database}/assemblies/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_assemblies_barcode_put(client):
    """Test case for api_v20_database_assemblies_barcode_put

    
    """
    body = openapi_server.ApiV20DatabaseAssembliesBarcodeGetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2.0/{database}/assemblies/{barcode}'.format(database='database_example', barcode='barcode_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v20_database_assemblies_get(client):
    """Test case for api_v20_database_assemblies_get

    
    """
    params = [('n50', 56),
                    ('barcode', ['barcode_example']),
                    ('orderby', 'barcode'),
                    ('offset', 0),
                    ('assembly_status', 'assembly_status_example'),
                    ('uberstrain', 'uberstrain_example'),
                    ('top_species', 'top_species_example'),
                    ('only_fields', ['only_fields_example']),
                    ('reldate', 56),
                    ('sortorder', 'asc'),
                    ('limit', 50),
                    ('version', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/{database}/assemblies'.format(database='database_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

