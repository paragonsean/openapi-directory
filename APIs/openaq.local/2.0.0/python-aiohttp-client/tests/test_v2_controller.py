# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cities_order import CitiesOrder
from openapi_server.models.countries_order import CountriesOrder
from openapi_server.models.date_from import DateFrom
from openapi_server.models.date_to import DateTo
from openapi_server.models.datefrom import Datefrom
from openapi_server.models.dateto import Dateto
from openapi_server.models.entity_types import EntityTypes
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.lastupdatedfrom import Lastupdatedfrom
from openapi_server.models.lastupdatedto import Lastupdatedto
from openapi_server.models.location_inner import LocationInner
from openapi_server.models.locations_order import LocationsOrder
from openapi_server.models.meas_order import MeasOrder
from openapi_server.models.open_aq_cities_result import OpenAQCitiesResult
from openapi_server.models.open_aq_countries_result import OpenAQCountriesResult
from openapi_server.models.open_aq_parameters_result import OpenAQParametersResult
from openapi_server.models.open_aq_projects_result import OpenAQProjectsResult
from openapi_server.models.open_aq_result import OpenAQResult
from openapi_server.models.order_by import OrderBy
from openapi_server.models.parameter import Parameter
from openapi_server.models.parameter_inner import ParameterInner
from openapi_server.models.projects_order import ProjectsOrder
from openapi_server.models.sensor_types import SensorTypes
from openapi_server.models.sort import Sort
from openapi_server.models.sources_order import SourcesOrder
from openapi_server.models.spatial import Spatial
from openapi_server.models.temporal import Temporal
from openapi_server.models.tile_json import TileJSON


pytestmark = pytest.mark.asyncio

async def test_averages_v2_get_v2_averages_get(client):
    """Test case for averages_v2_get_v2_averages_get

    Averages V2 Get
    """
    params = [('date_from', openapi_server.DateFrom()),
                    ('date_to', openapi_server.DateTo()),
                    ('parameter_id', 56),
                    ('parameter', [openapi_server.ParameterInner()]),
                    ('unit', ['unit_example']),
                    ('project_id', 56),
                    ('project', [openapi_server.ParameterInner()]),
                    ('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('spatial', openapi_server.Spatial()),
                    ('temporal', openapi_server.Temporal()),
                    ('location', ['location_example']),
                    ('group', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/averages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cities_get_v2_cities_get(client):
    """Test case for cities_get_v2_cities_get

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
        path='/v2/cities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_v2_countries_country_id_get(client):
    """Test case for countries_get_v2_countries_country_id_get

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
        path='/v2/countries/{country_id}'.format(country_id='country_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get_v2_countries_get(client):
    """Test case for countries_get_v2_countries_get

    Countries Get
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
        path='/v2/countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_demo_v2_locations_tiles_viewer_get(client):
    """Test case for demo_v2_locations_tiles_viewer_get

    Demo
    """
    headers = { 
        'Accept': 'text/html',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/tiles/viewer',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mobilegentile_v2_locations_tiles_mobile_generalized_zxy_pbf_get(client):
    """Test case for get_mobilegentile_v2_locations_tiles_mobile_generalized_zxy_pbf_get

    Get Mobilegentile
    """
    params = [('parameter', openapi_server.Parameter()),
                    ('location', [56]),
                    ('lastUpdatedFrom', openapi_server.Lastupdatedfrom()),
                    ('lastUpdatedTo', openapi_server.Lastupdatedto()),
                    ('isMobile', True),
                    ('project', 56),
                    ('isAnalysis', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/tiles/mobile-generalized/{z}/{x}/{y_pb}'.format(z=56, x=56, y=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mobiletile_v2_locations_tiles_mobile_zxy_pbf_get(client):
    """Test case for get_mobiletile_v2_locations_tiles_mobile_zxy_pbf_get

    Get Mobiletile
    """
    params = [('dateFrom', openapi_server.Datefrom()),
                    ('dateTo', openapi_server.Dateto()),
                    ('parameter', openapi_server.Parameter()),
                    ('location', [56]),
                    ('lastUpdatedFrom', openapi_server.Lastupdatedfrom()),
                    ('lastUpdatedTo', openapi_server.Lastupdatedto()),
                    ('isMobile', True),
                    ('project', 56),
                    ('isAnalysis', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/tiles/mobile/{z}/{x}/{y_pb}'.format(z=56, x=56, y=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tile_v2_locations_tiles_zxy_pbf_get(client):
    """Test case for get_tile_v2_locations_tiles_zxy_pbf_get

    Get Tile
    """
    params = [('parameter', openapi_server.Parameter()),
                    ('location', [56]),
                    ('lastUpdatedFrom', openapi_server.Lastupdatedfrom()),
                    ('lastUpdatedTo', openapi_server.Lastupdatedto()),
                    ('isMobile', True),
                    ('project', 56),
                    ('isAnalysis', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/tiles/{z}/{x}/{y_pb}'.format(z=56, x=56, y=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_latest_get_v2_latest_get(client):
    """Test case for latest_get_v2_latest_get

    Latest Get
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
        path='/v2/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_latest_get_v2_latest_location_id_get(client):
    """Test case for latest_get_v2_latest_location_id_get

    Latest Get
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
        path='/v2/latest/{location_id}'.format(location_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_get_v2_locations_get(client):
    """Test case for locations_get_v2_locations_get

    Locations Get
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
        path='/v2/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_get_v2_locations_location_id_get(client):
    """Test case for locations_get_v2_locations_location_id_get

    Locations Get
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
        path='/v2/locations/{location_id}'.format(location_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_measurements_get_v2_measurements_get(client):
    """Test case for measurements_get_v2_measurements_get

    Measurements Get
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
        path='/v2/measurements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mfr_get_v2_manufacturers_get(client):
    """Test case for mfr_get_v2_manufacturers_get

    Mfr Get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/manufacturers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mobilegentilejson_v2_locations_tiles_mobile_generalized_tiles_json_get(client):
    """Test case for mobilegentilejson_v2_locations_tiles_mobile_generalized_tiles_json_get

    Mobilegentilejson
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/tiles/mobile-generalized/tiles.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mobiletilejson_v2_locations_tiles_mobile_tiles_json_get(client):
    """Test case for mobiletilejson_v2_locations_tiles_mobile_tiles_json_get

    Mobiletilejson
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/tiles/mobile/tiles.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_get_v2_models_get(client):
    """Test case for model_get_v2_models_get

    Model Get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/models',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parameters_get_v2_parameters_get(client):
    """Test case for parameters_get_v2_parameters_get

    Parameters Get
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
        path='/v2/parameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_v2_projects_get(client):
    """Test case for projects_get_v2_projects_get

    Projects Get
    """
    params = [('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('parameter_id', 56),
                    ('parameter', [openapi_server.ParameterInner()]),
                    ('unit', ['unit_example']),
                    ('project_id', 56),
                    ('project', [openapi_server.ParameterInner()]),
                    ('order_by', openapi_server.ProjectsOrder()),
                    ('isMobile', True),
                    ('isAnalysis', True),
                    ('entity', 'entity_example'),
                    ('sensorType', 'sensor_type_example'),
                    ('sourceName', ['source_name_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_v2_projects_project_id_get(client):
    """Test case for projects_get_v2_projects_project_id_get

    Projects Get
    """
    params = [('country_id', 'country_id_example'),
                    ('country', ['country_example']),
                    ('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('parameter_id', 56),
                    ('parameter', [openapi_server.ParameterInner()]),
                    ('unit', ['unit_example']),
                    ('project', [openapi_server.ParameterInner()]),
                    ('order_by', openapi_server.ProjectsOrder()),
                    ('isMobile', True),
                    ('isAnalysis', True),
                    ('entity', 'entity_example'),
                    ('sensorType', 'sensor_type_example'),
                    ('sourceName', ['source_name_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/projects/{project_id}'.format(project_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_readme_get_v2_sources_readme_slug_get(client):
    """Test case for readme_get_v2_sources_readme_slug_get

    Readme Get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/sources/readme/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_get_v2_sources_get(client):
    """Test case for sources_get_v2_sources_get

    Sources Get
    """
    params = [('limit', 100),
                    ('page', 1),
                    ('offset', 0),
                    ('sort', openapi_server.Sort()),
                    ('sourceName', ['source_name_example']),
                    ('sourceId', [56]),
                    ('sourceSlug', ['source_slug_example']),
                    ('order_by', openapi_server.SourcesOrder())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/sources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_summary_get_v2_summary_get(client):
    """Test case for summary_get_v2_summary_get

    Summary Get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/summary',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tilejson_v2_locations_tiles_tiles_json_get(client):
    """Test case for tilejson_v2_locations_tiles_tiles_json_get

    Tilejson
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/tiles/tiles.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

