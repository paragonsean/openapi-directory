# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.country_response import CountryResponse
from openapi_server.models.date_time_response import DateTimeResponse
from openapi_server.models.distance_response import DistanceResponse
from openapi_server.models.forbidden_response import ForbiddenResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.populated_place_response import PopulatedPlaceResponse
from openapi_server.models.populated_places_response import PopulatedPlacesResponse
from openapi_server.models.region_response import RegionResponse
from openapi_server.models.regions_response import RegionsResponse
from openapi_server.models.time_response import TimeResponse


pytestmark = pytest.mark.asyncio

async def test_find_admin_divisions_using_get(client):
    """Test case for find_admin_divisions_using_get

    Find administrative divisions
    """
    params = [('location', 'location_example'),
                    ('radius', 56),
                    ('distanceUnit', 'MI'),
                    ('countryIds', 'country_ids_example'),
                    ('excludedCountryIds', 'excluded_country_ids_example'),
                    ('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/adminDivisions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_cities_near_admin_division_using_get(client):
    """Test case for find_cities_near_admin_division_using_get

    Find cities near division
    """
    params = [('radius', 56),
                    ('distanceUnit', 'MI'),
                    ('countryIds', 'country_ids_example'),
                    ('excludedCountryIds', 'excluded_country_ids_example'),
                    ('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('types', 'types_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/adminDivisions/{division_id}/nearbyCities'.format(division_id='division_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_cities_near_city_using_get(client):
    """Test case for find_cities_near_city_using_get

    Find cities near city
    """
    params = [('radius', 56),
                    ('distanceUnit', 'MI'),
                    ('countryIds', 'country_ids_example'),
                    ('excludedCountryIds', 'excluded_country_ids_example'),
                    ('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('types', 'types_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/cities/{city_id}/nearbyCities'.format(city_id='city_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_cities_near_location_using_get(client):
    """Test case for find_cities_near_location_using_get

    Find cities near location
    """
    params = [('radius', 56),
                    ('distanceUnit', 'MI'),
                    ('countryIds', 'country_ids_example'),
                    ('excludedCountryIds', 'excluded_country_ids_example'),
                    ('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('types', 'types_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/locations/{location_id}/nearbyCities'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_cities_using_get(client):
    """Test case for find_cities_using_get

    Find cities
    """
    params = [('location', 'location_example'),
                    ('radius', 56),
                    ('distanceUnit', 'MI'),
                    ('countryIds', 'country_ids_example'),
                    ('excludedCountryIds', 'excluded_country_ids_example'),
                    ('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('types', 'types_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/cities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_divisions_near_admin_division_using_get(client):
    """Test case for find_divisions_near_admin_division_using_get

    Find divisions near division
    """
    params = [('radius', 56),
                    ('distanceUnit', 'MI'),
                    ('countryIds', 'country_ids_example'),
                    ('excludedCountryIds', 'excluded_country_ids_example'),
                    ('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/adminDivisions/{division_id}/nearbyDivisions'.format(division_id='division_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_divisions_near_location_using_get(client):
    """Test case for find_divisions_near_location_using_get

    Find divisions near location
    """
    params = [('radius', 56),
                    ('distanceUnit', 'MI'),
                    ('countryIds', 'country_ids_example'),
                    ('excludedCountryIds', 'excluded_country_ids_example'),
                    ('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/locations/{location_id}/nearbyDivisions'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_region_cities_using_get(client):
    """Test case for find_region_cities_using_get

    Find country region cities
    """
    params = [('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('types', 'types_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/countries/{country_id}/regions/{region_code}/cities'.format(country_id='country_id_example', region_code='region_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_region_divisions_using_get(client):
    """Test case for find_region_divisions_using_get

    Find country region administrative divisions
    """
    params = [('minPopulation', 56),
                    ('maxPopulation', 56),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('timeZoneIds', 'time_zone_ids_example'),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example'),
                    ('includeDeleted', 'NONE')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/countries/{country_id}/regions/{region_code}/adminDivisions'.format(country_id='country_id_example', region_code='region_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_admin_division_using_get(client):
    """Test case for get_admin_division_using_get

    Get administrative division details
    """
    params = [('asciiMode', False),
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/adminDivisions/{division_id}'.format(division_id='division_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_city_date_time_using_get(client):
    """Test case for get_city_date_time_using_get

    Get city date-time
    """
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/cities/{city_id}/dateTime'.format(city_id='city_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_city_distance_using_get(client):
    """Test case for get_city_distance_using_get

    Get city distance
    """
    params = [('toCityId', 'to_city_id_example'),
                    ('distanceUnit', 'MI')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/cities/{city_id}/distance'.format(city_id='city_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_city_located_in_using_get(client):
    """Test case for get_city_located_in_using_get

    Get city admin region
    """
    params = [('asciiMode', False),
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/cities/{city_id}/locatedIn'.format(city_id='city_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_city_time_using_get(client):
    """Test case for get_city_time_using_get

    Get city time
    """
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/cities/{city_id}/time'.format(city_id='city_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_city_using_get(client):
    """Test case for get_city_using_get

    Get city details
    """
    params = [('asciiMode', False),
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/cities/{city_id}'.format(city_id='city_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_countries_using_get(client):
    """Test case for get_countries_using_get

    Find countries
    """
    params = [('currencyCode', 'currency_code_example'),
                    ('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_country_using_get(client):
    """Test case for get_country_using_get

    Get country details
    """
    params = [('asciiMode', False),
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/countries/{country_id}'.format(country_id='country_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_region_using_get(client):
    """Test case for get_region_using_get

    Get region details
    """
    params = [('asciiMode', False),
                    ('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/countries/{country_id}/regions/{region_code}'.format(country_id='country_id_example', region_code='region_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_regions_using_get(client):
    """Test case for get_regions_using_get

    Find country regions
    """
    params = [('namePrefix', 'name_prefix_example'),
                    ('namePrefixDefaultLangResults', True),
                    ('asciiMode', False),
                    ('hateoasMode', True),
                    ('languageCode', 'language_code_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/countries/{country_id}/regions'.format(country_id='country_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

