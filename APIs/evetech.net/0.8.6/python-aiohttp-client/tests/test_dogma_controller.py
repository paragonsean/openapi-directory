# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_dogma_attributes_attribute_id_not_found import GetDogmaAttributesAttributeIdNotFound
from openapi_server.models.get_dogma_attributes_attribute_id_ok import GetDogmaAttributesAttributeIdOk
from openapi_server.models.get_dogma_dynamic_items_type_id_item_id_not_found import GetDogmaDynamicItemsTypeIdItemIdNotFound
from openapi_server.models.get_dogma_dynamic_items_type_id_item_id_ok import GetDogmaDynamicItemsTypeIdItemIdOk
from openapi_server.models.get_dogma_effects_effect_id_not_found import GetDogmaEffectsEffectIdNotFound
from openapi_server.models.get_dogma_effects_effect_id_ok import GetDogmaEffectsEffectIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable


pytestmark = pytest.mark.asyncio

async def test_get_dogma_attributes(client):
    """Test case for get_dogma_attributes

    Get attributes
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/dogma/attributes/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dogma_attributes_attribute_id(client):
    """Test case for get_dogma_attributes_attribute_id

    Get attribute information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/dogma/attributes/{attribute_id}'.format(attribute_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dogma_dynamic_items_type_id_item_id(client):
    """Test case for get_dogma_dynamic_items_type_id_item_id

    Get dynamic item information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/dogma/dynamic/items/{type_id}/{item_id}'.format(item_id=56, type_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dogma_effects(client):
    """Test case for get_dogma_effects

    Get effects
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/dogma/effects/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dogma_effects_effect_id(client):
    """Test case for get_dogma_effects_effect_id

    Get effect information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/dogma/effects/{effect_id}'.format(effect_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

