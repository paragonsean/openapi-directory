# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.constituency_item import ConstituencyItem
from openapi_server.models.constituency_members_service_search_result import ConstituencyMembersServiceSearchResult
from openapi_server.models.constituency_representation_list_item import ConstituencyRepresentationListItem
from openapi_server.models.election_result_item import ElectionResultItem
from openapi_server.models.election_result_list_item import ElectionResultListItem
from openapi_server.models.location_item import LocationItem
from openapi_server.models.location_type import LocationType
from openapi_server.models.string_item import StringItem


pytestmark = pytest.mark.asyncio

async def test_api_location_browse_location_type_location_name_get(client):
    """Test case for api_location_browse_location_type_location_name_get

    Returns a list of locations, both parent and child
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Browse/{location_type}/{location_name}'.format(location_type=openapi_server.LocationType(), location_name='location_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_location_constituency_id_election_result_election_id_get(client):
    """Test case for api_location_constituency_id_election_result_election_id_get

    Returns an election result by constituency and election id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Constituency/{id}/ElectionResult/{election_id}'.format(id=56, election_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_location_constituency_id_election_result_latest_get(client):
    """Test case for api_location_constituency_id_election_result_latest_get

    Returns latest election result by constituency id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Constituency/{id}/ElectionResult/Latest'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_location_constituency_id_election_results_get(client):
    """Test case for api_location_constituency_id_election_results_get

    Returns a list of election results by constituency ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Constituency/{id}/ElectionResults'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_location_constituency_id_geometry_get(client):
    """Test case for api_location_constituency_id_geometry_get

    Returns geometry by constituency ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Constituency/{id}/Geometry'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_location_constituency_id_get(client):
    """Test case for api_location_constituency_id_get

    Returns a constituency by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Constituency/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_location_constituency_id_representations_get(client):
    """Test case for api_location_constituency_id_representations_get

    Returns a list of representations by constituency ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Constituency/{id}/Representations'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_location_constituency_id_synopsis_get(client):
    """Test case for api_location_constituency_id_synopsis_get

    Returns a synopsis by constituency ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Constituency/{id}/Synopsis'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_location_constituency_search_get(client):
    """Test case for api_location_constituency_search_get

    Returns a list of constituencies
    """
    params = [('searchText', 'search_text_example'),
                    ('skip', 0),
                    ('take', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Location/Constituency/Search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

