# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_industry_jobs200_ok import GetCharactersCharacterIdIndustryJobs200Ok
from openapi_server.models.get_characters_character_id_mining200_ok import GetCharactersCharacterIdMining200Ok
from openapi_server.models.get_corporation_corporation_id_mining_extractions200_ok import GetCorporationCorporationIdMiningExtractions200Ok
from openapi_server.models.get_corporation_corporation_id_mining_observers200_ok import GetCorporationCorporationIdMiningObservers200Ok
from openapi_server.models.get_corporation_corporation_id_mining_observers_observer_id200_ok import GetCorporationCorporationIdMiningObserversObserverId200Ok
from openapi_server.models.get_corporations_corporation_id_industry_jobs200_ok import GetCorporationsCorporationIdIndustryJobs200Ok
from openapi_server.models.get_industry_facilities200_ok import GetIndustryFacilities200Ok
from openapi_server.models.get_industry_systems200_ok import GetIndustrySystems200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_industry_jobs(client):
    """Test case for get_characters_character_id_industry_jobs

    List character industry jobs
    """
    params = [('datasource', tranquility),
                    ('include_completed', True),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/characters/{character_id}/industry/jobs'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_characters_character_id_mining(client):
    """Test case for get_characters_character_id_mining

    Character mining ledger
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
        path='/latest/characters/{character_id}/mining'.format(character_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporation_corporation_id_mining_extractions(client):
    """Test case for get_corporation_corporation_id_mining_extractions

    Moon extraction timers
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
        path='/latest/corporation/{corporation_id}/mining/extractions'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporation_corporation_id_mining_observers(client):
    """Test case for get_corporation_corporation_id_mining_observers

    Corporation mining observers
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
        path='/latest/corporation/{corporation_id}/mining/observers'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporation_corporation_id_mining_observers_observer_id(client):
    """Test case for get_corporation_corporation_id_mining_observers_observer_id

    Observed corporation mining
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
        path='/latest/corporation/{corporation_id}/mining/observers/{observer_id}'.format(corporation_id=56, observer_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporations_corporation_id_industry_jobs(client):
    """Test case for get_corporations_corporation_id_industry_jobs

    List corporation industry jobs
    """
    params = [('datasource', tranquility),
                    ('include_completed', False),
                    ('page', 1),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/corporations/{corporation_id}/industry/jobs'.format(corporation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_industry_facilities(client):
    """Test case for get_industry_facilities

    List industry facilities
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/industry/facilities/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_industry_systems(client):
    """Test case for get_industry_systems

    List solar system cost indices
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/industry/systems/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

