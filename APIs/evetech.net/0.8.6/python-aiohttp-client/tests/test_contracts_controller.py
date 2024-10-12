# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_contracts200_ok import GetCharactersCharacterIdContracts200Ok
from openapi_server.models.get_characters_character_id_contracts_contract_id_bids200_ok import GetCharactersCharacterIdContractsContractIdBids200Ok
from openapi_server.models.get_characters_character_id_contracts_contract_id_bids_not_found import GetCharactersCharacterIdContractsContractIdBidsNotFound
from openapi_server.models.get_characters_character_id_contracts_contract_id_items200_ok import GetCharactersCharacterIdContractsContractIdItems200Ok
from openapi_server.models.get_characters_character_id_contracts_contract_id_items_not_found import GetCharactersCharacterIdContractsContractIdItemsNotFound
from openapi_server.models.get_contracts_public_bids_contract_id200_ok import GetContractsPublicBidsContractId200Ok
from openapi_server.models.get_contracts_public_bids_contract_id_forbidden import GetContractsPublicBidsContractIdForbidden
from openapi_server.models.get_contracts_public_bids_contract_id_not_found import GetContractsPublicBidsContractIdNotFound
from openapi_server.models.get_contracts_public_items_contract_id200_ok import GetContractsPublicItemsContractId200Ok
from openapi_server.models.get_contracts_public_items_contract_id_forbidden import GetContractsPublicItemsContractIdForbidden
from openapi_server.models.get_contracts_public_items_contract_id_not_found import GetContractsPublicItemsContractIdNotFound
from openapi_server.models.get_contracts_public_region_id200_ok import GetContractsPublicRegionId200Ok
from openapi_server.models.get_contracts_public_region_id_not_found import GetContractsPublicRegionIdNotFound
from openapi_server.models.get_corporations_corporation_id_contracts200_ok import GetCorporationsCorporationIdContracts200Ok
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_bids200_ok import GetCorporationsCorporationIdContractsContractIdBids200Ok
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_bids_not_found import GetCorporationsCorporationIdContractsContractIdBidsNotFound
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_items200_ok import GetCorporationsCorporationIdContractsContractIdItems200Ok
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_items_error520 import GetCorporationsCorporationIdContractsContractIdItemsError520
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_items_not_found import GetCorporationsCorporationIdContractsContractIdItemsNotFound
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_contracts(client):
    """Test case for get_characters_character_id_contracts

    Get contracts
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
        path='/latest/characters/{character_id}/contracts'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_contracts_contract_id_bids(client):
    """Test case for get_characters_character_id_contracts_contract_id_bids

    Get contract bids
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
        path='/latest/characters/{character_id}/contracts/{contract_id}/bids'.format(character_id=56, contract_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_contracts_contract_id_items(client):
    """Test case for get_characters_character_id_contracts_contract_id_items

    Get contract items
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
        path='/latest/characters/{character_id}/contracts/{contract_id}/items'.format(character_id=56, contract_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contracts_public_bids_contract_id(client):
    """Test case for get_contracts_public_bids_contract_id

    Get public contract bids
    """
    params = [('datasource', tranquility),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/contracts/public/bids/{contract_id}'.format(contract_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contracts_public_items_contract_id(client):
    """Test case for get_contracts_public_items_contract_id

    Get public contract items
    """
    params = [('datasource', tranquility),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/contracts/public/items/{contract_id}'.format(contract_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contracts_public_region_id(client):
    """Test case for get_contracts_public_region_id

    Get public contracts
    """
    params = [('datasource', tranquility),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/contracts/public/{region_id}'.format(region_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_contracts(client):
    """Test case for get_corporations_corporation_id_contracts

    Get corporation contracts
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
        path='/latest/corporations/{corporation_id}/contracts'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_contracts_contract_id_bids(client):
    """Test case for get_corporations_corporation_id_contracts_contract_id_bids

    Get corporation contract bids
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
        path='/latest/corporations/{corporation_id}/contracts/{contract_id}/bids'.format(contract_id=56, corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_contracts_contract_id_items(client):
    """Test case for get_corporations_corporation_id_contracts_contract_id_items

    Get corporation contract items
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
        path='/latest/corporations/{corporation_id}/contracts/{contract_id}/items'.format(contract_id=56, corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

