# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.house import House
from openapi_server.models.lords_by_type_members_service_search_result import LordsByTypeMembersServiceSearchResult
from openapi_server.models.party_members_service_search_result import PartyMembersServiceSearchResult
from openapi_server.models.party_seat_count_members_service_search_result import PartySeatCountMembersServiceSearchResult


pytestmark = pytest.mark.asyncio

async def test_api_parties_get_active_house_get(client):
    """Test case for api_parties_get_active_house_get

    Returns a list of current parties with at least one active member.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Parties/GetActive/{house}'.format(house=openapi_server.House()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_parties_lords_by_type_for_date_get(client):
    """Test case for api_parties_lords_by_type_for_date_get

    Returns the composition of the House of Lords by peerage type.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Parties/LordsByType/{for_date}'.format(for_date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_parties_state_of_the_parties_house_for_date_get(client):
    """Test case for api_parties_state_of_the_parties_house_for_date_get

    Returns current state of parties
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Parties/StateOfTheParties/{house}/{for_date}'.format(house=openapi_server.House(), for_date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

