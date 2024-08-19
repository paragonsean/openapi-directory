# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_name_geo_in import BatchNameGeoIn
from openapi_server.models.batch_name_in import BatchNameIn
from openapi_server.models.batch_proper_noun_categorized_out import BatchProperNounCategorizedOut
from openapi_server.models.proper_noun_categorized_out import ProperNounCategorizedOut


pytestmark = pytest.mark.asyncio

async def test_name_type(client):
    """Test case for name_type

    Infer the likely type of a proper noun (personal name, brand name, place name etc.)
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/nameType/{proper_noun}'.format(proper_noun='proper_noun_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_name_type_batch(client):
    """Test case for name_type_batch

    Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)
    """
    body = {"properNouns":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/nameTypeBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_name_type_geo(client):
    """Test case for name_type_geo

    Infer the likely type of a proper noun (personal name, brand name, place name etc.)
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/nameTypeGeo/{proper_noun}/{country_iso2}'.format(proper_noun='proper_noun_example', country_iso2='country_iso2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_name_type_geo_batch(client):
    """Test case for name_type_geo_batch

    Infer the likely common type of up to 100 proper nouns (personal name, brand name, place name etc.)
    """
    body = {"properNouns":[{"name":"name","countryIso2":"countryIso2","id":"id"},{"name":"name","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/nameTypeGeoBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

