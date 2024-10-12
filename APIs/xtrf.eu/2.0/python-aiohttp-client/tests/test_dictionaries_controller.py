# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dictionary_entity import DictionaryEntity
from openapi_server.models.many_values_per_type_dto import ManyValuesPerTypeDTO
from openapi_server.models.service_dto import ServiceDTO


pytestmark = pytest.mark.asyncio

async def test_get_active(client):
    """Test case for get_active

    Returns active dictionary entities for all types.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/dictionaries/active',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_active_by_type(client):
    """Test case for get_active_by_type

    Returns active values from a given dictionary.
    """
    params = [('nameEquals', 'name_equals_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/dictionaries/{type}/active'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all1(client):
    """Test case for get_all1

    Returns dictionary entities for all types. Both active and not active ones.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/dictionaries/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all3(client):
    """Test case for get_all3

    Returns services list
    """
    params = [('nameEquals', 'name_equals_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/services/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_active(client):
    """Test case for get_all_active

    Returns active services list
    """
    params = [('nameEquals', 'name_equals_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/services/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_by_type(client):
    """Test case for get_all_by_type

    Returns all values (both active and not active) from a given dictionary.
    """
    params = [('nameEquals', 'name_equals_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/dictionaries/{type}/all'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_type_and_id(client):
    """Test case for get_by_type_and_id

    Returns specific value from a given dictionary.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/dictionaries/{type}/{id}'.format(type='type_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

