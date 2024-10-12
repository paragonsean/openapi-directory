# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_assets200_ok import GetCharactersCharacterIdAssets200Ok
from openapi_server.models.get_corporations_corporation_id_assets200_ok import GetCorporationsCorporationIdAssets200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_character_id_assets_locations200_ok import PostCharactersCharacterIdAssetsLocations200Ok
from openapi_server.models.post_characters_character_id_assets_names200_ok import PostCharactersCharacterIdAssetsNames200Ok
from openapi_server.models.post_corporations_corporation_id_assets_locations200_ok import PostCorporationsCorporationIdAssetsLocations200Ok
from openapi_server.models.post_corporations_corporation_id_assets_locations_not_found import PostCorporationsCorporationIdAssetsLocationsNotFound
from openapi_server.models.post_corporations_corporation_id_assets_names200_ok import PostCorporationsCorporationIdAssetsNames200Ok
from openapi_server.models.post_corporations_corporation_id_assets_names_not_found import PostCorporationsCorporationIdAssetsNamesNotFound
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_assets(client):
    """Test case for get_characters_character_id_assets

    Get character assets
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
        path='/latest/characters/{character_id}/assets'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_assets(client):
    """Test case for get_corporations_corporation_id_assets

    Get corporation assets
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
        path='/latest/corporations/{corporation_id}/assets'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_characters_character_id_assets_locations(client):
    """Test case for post_characters_character_id_assets_locations

    Get character asset locations
    """
    item_ids = [56]
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/characters/{character_id}/assets/locations'.format(character_id=56),
        headers=headers,
        json=item_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_characters_character_id_assets_names(client):
    """Test case for post_characters_character_id_assets_names

    Get character asset names
    """
    item_ids = [56]
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/characters/{character_id}/assets/names'.format(character_id=56),
        headers=headers,
        json=item_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_corporations_corporation_id_assets_locations(client):
    """Test case for post_corporations_corporation_id_assets_locations

    Get corporation asset locations
    """
    item_ids = [56]
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/corporations/{corporation_id}/assets/locations'.format(corporation_id=56),
        headers=headers,
        json=item_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_corporations_corporation_id_assets_names(client):
    """Test case for post_corporations_corporation_id_assets_names

    Get corporation asset names
    """
    item_ids = [56]
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/latest/corporations/{corporation_id}/assets/names'.format(corporation_id=56),
        headers=headers,
        json=item_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

