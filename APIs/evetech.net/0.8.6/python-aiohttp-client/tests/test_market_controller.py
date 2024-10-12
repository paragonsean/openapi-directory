# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_orders200_ok import GetCharactersCharacterIdOrders200Ok
from openapi_server.models.get_characters_character_id_orders_history200_ok import GetCharactersCharacterIdOrdersHistory200Ok
from openapi_server.models.get_corporations_corporation_id_orders200_ok import GetCorporationsCorporationIdOrders200Ok
from openapi_server.models.get_corporations_corporation_id_orders_history200_ok import GetCorporationsCorporationIdOrdersHistory200Ok
from openapi_server.models.get_markets_groups_market_group_id_not_found import GetMarketsGroupsMarketGroupIdNotFound
from openapi_server.models.get_markets_groups_market_group_id_ok import GetMarketsGroupsMarketGroupIdOk
from openapi_server.models.get_markets_prices200_ok import GetMarketsPrices200Ok
from openapi_server.models.get_markets_region_id_history200_ok import GetMarketsRegionIdHistory200Ok
from openapi_server.models.get_markets_region_id_history_error520 import GetMarketsRegionIdHistoryError520
from openapi_server.models.get_markets_region_id_history_not_found import GetMarketsRegionIdHistoryNotFound
from openapi_server.models.get_markets_region_id_history_unprocessable_entity import GetMarketsRegionIdHistoryUnprocessableEntity
from openapi_server.models.get_markets_region_id_orders200_ok import GetMarketsRegionIdOrders200Ok
from openapi_server.models.get_markets_region_id_orders_not_found import GetMarketsRegionIdOrdersNotFound
from openapi_server.models.get_markets_region_id_orders_unprocessable_entity import GetMarketsRegionIdOrdersUnprocessableEntity
from openapi_server.models.get_markets_structures_structure_id200_ok import GetMarketsStructuresStructureId200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_orders(client):
    """Test case for get_characters_character_id_orders

    List open orders from a character
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/orders'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_orders_history(client):
    """Test case for get_characters_character_id_orders_history

    List historical orders by a character
    """
    params = [('datasource', tranquility),
                    ('page', 1),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/orders/history'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_orders(client):
    """Test case for get_corporations_corporation_id_orders

    List open orders from a corporation
    """
    params = [('datasource', tranquility),
                    ('page', 1),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/corporations/{corporation_id}/orders'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_orders_history(client):
    """Test case for get_corporations_corporation_id_orders_history

    List historical orders from a corporation
    """
    params = [('datasource', tranquility),
                    ('page', 1),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/corporations/{corporation_id}/orders/history'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets_groups(client):
    """Test case for get_markets_groups

    Get item groups
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/markets/groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets_groups_market_group_id(client):
    """Test case for get_markets_groups_market_group_id

    Get item group information
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/markets/groups/{market_group_id}'.format(market_group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets_prices(client):
    """Test case for get_markets_prices

    List market prices
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/markets/prices/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets_region_id_history(client):
    """Test case for get_markets_region_id_history

    List historical market statistics in a region
    """
    params = [('datasource', tranquility),
                    ('type_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/markets/{region_id}/history'.format(region_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets_region_id_orders(client):
    """Test case for get_markets_region_id_orders

    List orders in a region
    """
    params = [('datasource', tranquility),
                    ('order_type', all),
                    ('page', 1),
                    ('type_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/markets/{region_id}/orders'.format(region_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets_region_id_types(client):
    """Test case for get_markets_region_id_types

    List type IDs relevant to a market
    """
    params = [('datasource', tranquility),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/markets/{region_id}/types'.format(region_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_markets_structures_structure_id(client):
    """Test case for get_markets_structures_structure_id

    List orders in a structure
    """
    params = [('datasource', tranquility),
                    ('page', 1),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/markets/structures/{structure_id}'.format(structure_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

