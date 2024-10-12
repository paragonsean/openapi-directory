# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cities_order import CitiesOrder
from openapi_server.models.countries_order import CountriesOrder
from openapi_server.models.date_from import DateFrom
from openapi_server.models.date_to import DateTo
from openapi_server.models.entity_types import EntityTypes
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.location_inner import LocationInner
from openapi_server.models.locations_order import LocationsOrder
from openapi_server.models.meas_order import MeasOrder
from openapi_server.models.open_aq_cities_result import OpenAQCitiesResult
from openapi_server.models.open_aq_countries_result import OpenAQCountriesResult
from openapi_server.models.open_aq_parameters_result import OpenAQParametersResult
from openapi_server.models.open_aq_result import OpenAQResult
from openapi_server.models.order_by import OrderBy
from openapi_server.models.parameter_inner import ParameterInner
from openapi_server.models.sensor_types import SensorTypes
from openapi_server.models.sort import Sort
from openapi_server.models.sources_v1_order import SourcesV1Order


pytestmark = pytest.mark.asyncio

async def test_cities_getv1_v1_cities_get(client):
    """Test case for cities_getv1_v1_cities_get

    Provides a simple listing of cities within the platform
    """
    params = [('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('city', ['city_example']),
                    ('order_by', openapi_server.CitiesOrder()),
                    ('entity', 'entity_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/cities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_v1_countries_country_id_get(client):
    """Test case for countries_get_v1_countries_country_id_get

    Countries Get
    """
    params = [('limit', 200),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('country', ['country_example']),
                    ('order_by', openapi_server.CountriesOrder())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries/{country_id}'.format(country_id='country_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_getv1_v1_countries_get(client):
    """Test case for countries_getv1_v1_countries_get

    Countries Getv1
    """
    params = [('limit', 200),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('order_by', openapi_server.CountriesOrder())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_latest_v1_get_v1_latest_get(client):
    """Test case for latest_v1_get_v1_latest_get

    Latest V1 Get
    """
    params = [('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('has_geo', True),
                    ('parameter_id', 56),
                    ('parameter', [openapi_server.ParameterInner()]),
                    ('unit', ['unit_example']),
                    ('coordinates', 'coordinates_example'),
                    ('radius', 1000),
                    ('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('city', ['city_example']),
                    ('location_id', 56),
                    ('location', [openapi_server.LocationInner()]),
                    ('order_by', openapi_server.LocationsOrder()),
                    ('isMobile', True),
                    ('isAnalysis', True),
                    ('sourceName', ['source_name_example']),
                    ('entity', openapi_server.EntityTypes()),
                    ('sensorType', openapi_server.SensorTypes()),
                    ('modelName', ['model_name_example']),
                    ('manufacturerName', ['manufacturer_name_example']),
                    ('dumpRaw', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_latest_v1_get_v1_latest_location_id_get(client):
    """Test case for latest_v1_get_v1_latest_location_id_get

    Latest V1 Get
    """
    params = [('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('has_geo', True),
                    ('parameter_id', 56),
                    ('parameter', [openapi_server.ParameterInner()]),
                    ('unit', ['unit_example']),
                    ('coordinates', 'coordinates_example'),
                    ('radius', 1000),
                    ('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('city', ['city_example']),
                    ('location', [openapi_server.LocationInner()]),
                    ('order_by', openapi_server.LocationsOrder()),
                    ('isMobile', True),
                    ('isAnalysis', True),
                    ('sourceName', ['source_name_example']),
                    ('entity', openapi_server.EntityTypes()),
                    ('sensorType', openapi_server.SensorTypes()),
                    ('modelName', ['model_name_example']),
                    ('manufacturerName', ['manufacturer_name_example']),
                    ('dumpRaw', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/latest/{location_id}'.format(location_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locationsv1_get_v1_locations_get(client):
    """Test case for locationsv1_get_v1_locations_get

    Locationsv1 Get
    """
    params = [('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('has_geo', True),
                    ('parameter_id', 56),
                    ('parameter', [openapi_server.ParameterInner()]),
                    ('unit', ['unit_example']),
                    ('coordinates', 'coordinates_example'),
                    ('radius', 1000),
                    ('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('city', ['city_example']),
                    ('location_id', 56),
                    ('location', [openapi_server.LocationInner()]),
                    ('order_by', openapi_server.LocationsOrder()),
                    ('isMobile', True),
                    ('isAnalysis', True),
                    ('sourceName', ['source_name_example']),
                    ('entity', openapi_server.EntityTypes()),
                    ('sensorType', openapi_server.SensorTypes()),
                    ('modelName', ['model_name_example']),
                    ('manufacturerName', ['manufacturer_name_example']),
                    ('dumpRaw', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locationsv1_get_v1_locations_location_id_get(client):
    """Test case for locationsv1_get_v1_locations_location_id_get

    Locationsv1 Get
    """
    params = [('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('has_geo', True),
                    ('parameter_id', 56),
                    ('parameter', [openapi_server.ParameterInner()]),
                    ('unit', ['unit_example']),
                    ('coordinates', 'coordinates_example'),
                    ('radius', 1000),
                    ('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('city', ['city_example']),
                    ('location', [openapi_server.LocationInner()]),
                    ('order_by', openapi_server.LocationsOrder()),
                    ('isMobile', True),
                    ('isAnalysis', True),
                    ('sourceName', ['source_name_example']),
                    ('entity', openapi_server.EntityTypes()),
                    ('sensorType', openapi_server.SensorTypes()),
                    ('modelName', ['model_name_example']),
                    ('manufacturerName', ['manufacturer_name_example']),
                    ('dumpRaw', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/locations/{location_id}'.format(location_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_measurements_get_v1_v1_measurements_get(client):
    """Test case for measurements_get_v1_v1_measurements_get

    Measurements Get V1
    """
    params = [('format', 'format_example'),
                    ('date_from', openapi_server.DateFrom()),
                    ('date_to', openapi_server.DateTo()),
                    ('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('has_geo', True),
                    ('parameter_id', 56),
                    ('parameter', [openapi_server.ParameterInner()]),
                    ('unit', ['unit_example']),
                    ('coordinates', 'coordinates_example'),
                    ('radius', 1000),
                    ('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('city', ['city_example']),
                    ('location_id', 56),
                    ('location', [openapi_server.LocationInner()]),
                    ('order_by', openapi_server.MeasOrder()),
                    ('isMobile', True),
                    ('isAnalysis', True),
                    ('project', 56),
                    ('entity', openapi_server.EntityTypes()),
                    ('sensorType', openapi_server.SensorTypes()),
                    ('value_from', 3.4),
                    ('value_to', 3.4),
                    ('include_fields', 'include_fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/measurements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parameters_getv1_v1_parameters_get(client):
    """Test case for parameters_getv1_v1_parameters_get

    Parameters Getv1
    """
    params = [('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('sourceName', ['source_name_example']),
                    ('sourceId', [56]),
                    ('sourceSlug', ['source_slug_example']),
                    ('order_by', openapi_server.OrderBy())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/parameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_v1_get_v1_sources_get(client):
    """Test case for sources_v1_get_v1_sources_get

    Sources V1 Get
    """
    params = [('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('name', 'name_example'),
                    ('order_by', openapi_server.SourcesV1Order())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/sources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

