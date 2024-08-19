# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.facilities_ids_response import FacilitiesIdsResponse
from openapi_server.models.facilities_response import FacilitiesResponse
from openapi_server.models.facility_read_response import FacilityReadResponse
from openapi_server.models.generic_error import GenericError
from openapi_server.models.geo_facilities_response import GeoFacilitiesResponse
from openapi_server.models.geo_facility_read_response import GeoFacilityReadResponse
from openapi_server.models.nearby_response import NearbyResponse


pytestmark = pytest.mark.asyncio

async def test_get_all_facilities(client):
    """Test case for get_all_facilities

    Bulk download information for all facilities
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/geo+json',
    }
    response = await client.request(
        method='GET',
        path='/facilities/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_facilities_by_location(client):
    """Test case for get_facilities_by_location

    Query facilities by location or IDs, with optional filters
    """
    params = [('ids', ['[\"vha_688\",\"vha_644\"]']),
                    ('zip', '80301-1000'),
                    ('state', 'CO'),
                    ('lat', 56.7),
                    ('long', -123.4),
                    ('radius', 75),
                    ('bbox[]', [[-105.4,39.4,-104.5,40.1]]),
                    ('visn', 3.4),
                    ('type', 'type_example'),
                    ('services[]', ['services_example']),
                    ('mobile', True),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/facilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_facility_by_id(client):
    """Test case for get_facility_by_id

    Retrieve a specific facility by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/facilities/{id}'.format(id='vha_688'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_facility_ids(client):
    """Test case for get_facility_ids

    Bulk download of all facility IDs
    """
    params = [('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nearby_facilities(client):
    """Test case for get_nearby_facilities

    Retrieve all VA health facilities reachable by driving within the specified time period
    """
    params = [('lat', 56.7),
                    ('lng', -123.4),
                    ('street_address', '1350 I St. NW'),
                    ('city', 'Washington'),
                    ('state', 'DC'),
                    ('zip', '20005-3305'),
                    ('drive_time', 90),
                    ('services[]', ['services_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/nearby',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

