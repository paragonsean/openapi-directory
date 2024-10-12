from typing import List, Dict
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
from openapi_server import util


async def averages_v2_get_v2_averages_get(request: web.Request, spatial, temporal, date_from=None, date_to=None, parameter_id=None, parameter=None, unit=None, project_id=None, project=None, country_id=None, country=None, limit=None, page=None, offset=None, sort=None, location=None, group=None) -> web.Response:
    """Averages V2 Get

    

    :param spatial: 
    :type spatial: dict | bytes
    :param temporal: 
    :type temporal: dict | bytes
    :param date_from: 
    :type date_from: dict | bytes
    :param date_to: 
    :type date_to: dict | bytes
    :param parameter_id: 
    :type parameter_id: int
    :param parameter: 
    :type parameter: list | bytes
    :param unit: 
    :type unit: List[str]
    :param project_id: 
    :type project_id: int
    :param project: 
    :type project: list | bytes
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Define sort order.
    :type sort: dict | bytes
    :param location: 
    :type location: List[str]
    :param group: 
    :type group: bool

    """
    spatial = .from_dict(spatial)
    temporal = .from_dict(temporal)
    date_from = .from_dict(date_from)
    date_to = .from_dict(date_to)
    parameter = [ParameterInner.from_dict(d) for d in parameter]
    project = [ParameterInner.from_dict(d) for d in project]
    sort = .from_dict(sort)
    return web.Response(status=200)


async def cities_get_v2_cities_get(request: web.Request, limit=None, page=None, offset=None, sort=None, country_id=None, country=None, city=None, order_by=None, entity=None) -> web.Response:
    """Provides a simple listing of cities within the platform

    

    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Define sort order.
    :type sort: dict | bytes
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param city:          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)         
    :type city: List[str]
    :param order_by: Order by a field
    :type order_by: dict | bytes
    :param entity: 
    :type entity: str

    """
    sort = .from_dict(sort)
    order_by = .from_dict(order_by)
    return web.Response(status=200)


async def countries_get_v2_countries_country_id_get(request: web.Request, country_id, limit=None, page=None, offset=None, sort=None, country=None, order_by=None) -> web.Response:
    """Countries Get

    

    :param country_id: 
    :type country_id: str
    :param limit: 
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Define sort order.
    :type sort: dict | bytes
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param order_by: 
    :type order_by: dict | bytes

    """
    sort = .from_dict(sort)
    order_by = .from_dict(order_by)
    return web.Response(status=200)


async def countries_get_v2_countries_get(request: web.Request, limit=None, page=None, offset=None, sort=None, country_id=None, country=None, order_by=None) -> web.Response:
    """Countries Get

    

    :param limit: 
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Define sort order.
    :type sort: dict | bytes
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param order_by: 
    :type order_by: dict | bytes

    """
    sort = .from_dict(sort)
    order_by = .from_dict(order_by)
    return web.Response(status=200)


async def demo_v2_locations_tiles_viewer_get(request: web.Request, ) -> web.Response:
    """Demo

    


    """
    return web.Response(status=200)


async def get_mobilegentile_v2_locations_tiles_mobile_generalized_zxy_pbf_get(request: web.Request, z, x, y, parameter=None, location=None, last_updated_from=None, last_updated_to=None, is_mobile=None, project=None, is_analysis=None) -> web.Response:
    """Get Mobilegentile

    

    :param z: 
    :type z: int
    :param x: 
    :type x: int
    :param y: 
    :type y: int
    :param parameter: 
    :type parameter: dict | bytes
    :param location: limit data to location id
    :type location: List[int]
    :param last_updated_from: 
    :type last_updated_from: dict | bytes
    :param last_updated_to: 
    :type last_updated_to: dict | bytes
    :param is_mobile: 
    :type is_mobile: bool
    :param project: 
    :type project: int
    :param is_analysis: 
    :type is_analysis: bool

    """
    parameter = .from_dict(parameter)
    last_updated_from = .from_dict(last_updated_from)
    last_updated_to = .from_dict(last_updated_to)
    return web.Response(status=200)


async def get_mobiletile_v2_locations_tiles_mobile_zxy_pbf_get(request: web.Request, z, x, y, date_from, date_to, parameter=None, location=None, last_updated_from=None, last_updated_to=None, is_mobile=None, project=None, is_analysis=None) -> web.Response:
    """Get Mobiletile

    

    :param z: 
    :type z: int
    :param x: 
    :type x: int
    :param y: 
    :type y: int
    :param date_from: 
    :type date_from: dict | bytes
    :param date_to: 
    :type date_to: dict | bytes
    :param parameter: 
    :type parameter: dict | bytes
    :param location: limit data to location id
    :type location: List[int]
    :param last_updated_from: 
    :type last_updated_from: dict | bytes
    :param last_updated_to: 
    :type last_updated_to: dict | bytes
    :param is_mobile: 
    :type is_mobile: bool
    :param project: 
    :type project: int
    :param is_analysis: 
    :type is_analysis: bool

    """
    date_from = .from_dict(date_from)
    date_to = .from_dict(date_to)
    parameter = .from_dict(parameter)
    last_updated_from = .from_dict(last_updated_from)
    last_updated_to = .from_dict(last_updated_to)
    return web.Response(status=200)


async def get_tile_v2_locations_tiles_zxy_pbf_get(request: web.Request, z, x, y, parameter=None, location=None, last_updated_from=None, last_updated_to=None, is_mobile=None, project=None, is_analysis=None) -> web.Response:
    """Get Tile

    

    :param z: 
    :type z: int
    :param x: 
    :type x: int
    :param y: 
    :type y: int
    :param parameter: 
    :type parameter: dict | bytes
    :param location: limit data to location id
    :type location: List[int]
    :param last_updated_from: 
    :type last_updated_from: dict | bytes
    :param last_updated_to: 
    :type last_updated_to: dict | bytes
    :param is_mobile: 
    :type is_mobile: bool
    :param project: 
    :type project: int
    :param is_analysis: 
    :type is_analysis: bool

    """
    parameter = .from_dict(parameter)
    last_updated_from = .from_dict(last_updated_from)
    last_updated_to = .from_dict(last_updated_to)
    return web.Response(status=200)


async def latest_get_v2_latest_get(request: web.Request, limit=None, page=None, offset=None, sort=None, has_geo=None, parameter_id=None, parameter=None, unit=None, coordinates=None, radius=None, country_id=None, country=None, city=None, location_id=None, location=None, order_by=None, is_mobile=None, is_analysis=None, source_name=None, entity=None, sensor_type=None, model_name=None, manufacturer_name=None, dump_raw=None) -> web.Response:
    """Latest Get

    

    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Sort Direction
    :type sort: dict | bytes
    :param has_geo: 
    :type has_geo: bool
    :param parameter_id: 
    :type parameter_id: int
    :param parameter: 
    :type parameter: list | bytes
    :param unit: 
    :type unit: List[str]
    :param coordinates: 
    :type coordinates: str
    :param radius: 
    :type radius: int
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param city:          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)         
    :type city: List[str]
    :param location_id: 
    :type location_id: int
    :param location: 
    :type location: list | bytes
    :param order_by: Order by a field
    :type order_by: dict | bytes
    :param is_mobile: Location is mobile
    :type is_mobile: bool
    :param is_analysis: Data is the product of a previous analysis/aggregation and not raw measurements
    :type is_analysis: bool
    :param source_name: Name of the data source
    :type source_name: List[str]
    :param entity: Source entity type.
    :type entity: dict | bytes
    :param sensor_type: Type of Sensor
    :type sensor_type: dict | bytes
    :param model_name: Model Name of Sensor
    :type model_name: List[str]
    :param manufacturer_name: Manufacturer of Sensor
    :type manufacturer_name: List[str]
    :param dump_raw: 
    :type dump_raw: bool

    """
    sort = .from_dict(sort)
    parameter = [ParameterInner.from_dict(d) for d in parameter]
    location = [LocationInner.from_dict(d) for d in location]
    order_by = .from_dict(order_by)
    entity = .from_dict(entity)
    sensor_type = .from_dict(sensor_type)
    return web.Response(status=200)


async def latest_get_v2_latest_location_id_get(request: web.Request, location_id, limit=None, page=None, offset=None, sort=None, has_geo=None, parameter_id=None, parameter=None, unit=None, coordinates=None, radius=None, country_id=None, country=None, city=None, location=None, order_by=None, is_mobile=None, is_analysis=None, source_name=None, entity=None, sensor_type=None, model_name=None, manufacturer_name=None, dump_raw=None) -> web.Response:
    """Latest Get

    

    :param location_id: 
    :type location_id: int
    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Sort Direction
    :type sort: dict | bytes
    :param has_geo: 
    :type has_geo: bool
    :param parameter_id: 
    :type parameter_id: int
    :param parameter: 
    :type parameter: list | bytes
    :param unit: 
    :type unit: List[str]
    :param coordinates: 
    :type coordinates: str
    :param radius: 
    :type radius: int
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param city:          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)         
    :type city: List[str]
    :param location: 
    :type location: list | bytes
    :param order_by: Order by a field
    :type order_by: dict | bytes
    :param is_mobile: Location is mobile
    :type is_mobile: bool
    :param is_analysis: Data is the product of a previous analysis/aggregation and not raw measurements
    :type is_analysis: bool
    :param source_name: Name of the data source
    :type source_name: List[str]
    :param entity: Source entity type.
    :type entity: dict | bytes
    :param sensor_type: Type of Sensor
    :type sensor_type: dict | bytes
    :param model_name: Model Name of Sensor
    :type model_name: List[str]
    :param manufacturer_name: Manufacturer of Sensor
    :type manufacturer_name: List[str]
    :param dump_raw: 
    :type dump_raw: bool

    """
    sort = .from_dict(sort)
    parameter = [ParameterInner.from_dict(d) for d in parameter]
    location = [LocationInner.from_dict(d) for d in location]
    order_by = .from_dict(order_by)
    entity = .from_dict(entity)
    sensor_type = .from_dict(sensor_type)
    return web.Response(status=200)


async def locations_get_v2_locations_get(request: web.Request, limit=None, page=None, offset=None, sort=None, has_geo=None, parameter_id=None, parameter=None, unit=None, coordinates=None, radius=None, country_id=None, country=None, city=None, location_id=None, location=None, order_by=None, is_mobile=None, is_analysis=None, source_name=None, entity=None, sensor_type=None, model_name=None, manufacturer_name=None, dump_raw=None) -> web.Response:
    """Locations Get

    

    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Sort Direction
    :type sort: dict | bytes
    :param has_geo: 
    :type has_geo: bool
    :param parameter_id: 
    :type parameter_id: int
    :param parameter: 
    :type parameter: list | bytes
    :param unit: 
    :type unit: List[str]
    :param coordinates: 
    :type coordinates: str
    :param radius: 
    :type radius: int
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param city:          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)         
    :type city: List[str]
    :param location_id: 
    :type location_id: int
    :param location: 
    :type location: list | bytes
    :param order_by: Order by a field
    :type order_by: dict | bytes
    :param is_mobile: Location is mobile
    :type is_mobile: bool
    :param is_analysis: Data is the product of a previous analysis/aggregation and not raw measurements
    :type is_analysis: bool
    :param source_name: Name of the data source
    :type source_name: List[str]
    :param entity: Source entity type.
    :type entity: dict | bytes
    :param sensor_type: Type of Sensor
    :type sensor_type: dict | bytes
    :param model_name: Model Name of Sensor
    :type model_name: List[str]
    :param manufacturer_name: Manufacturer of Sensor
    :type manufacturer_name: List[str]
    :param dump_raw: 
    :type dump_raw: bool

    """
    sort = .from_dict(sort)
    parameter = [ParameterInner.from_dict(d) for d in parameter]
    location = [LocationInner.from_dict(d) for d in location]
    order_by = .from_dict(order_by)
    entity = .from_dict(entity)
    sensor_type = .from_dict(sensor_type)
    return web.Response(status=200)


async def locations_get_v2_locations_location_id_get(request: web.Request, location_id, limit=None, page=None, offset=None, sort=None, has_geo=None, parameter_id=None, parameter=None, unit=None, coordinates=None, radius=None, country_id=None, country=None, city=None, location=None, order_by=None, is_mobile=None, is_analysis=None, source_name=None, entity=None, sensor_type=None, model_name=None, manufacturer_name=None, dump_raw=None) -> web.Response:
    """Locations Get

    

    :param location_id: 
    :type location_id: int
    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Sort Direction
    :type sort: dict | bytes
    :param has_geo: 
    :type has_geo: bool
    :param parameter_id: 
    :type parameter_id: int
    :param parameter: 
    :type parameter: list | bytes
    :param unit: 
    :type unit: List[str]
    :param coordinates: 
    :type coordinates: str
    :param radius: 
    :type radius: int
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param city:          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)         
    :type city: List[str]
    :param location: 
    :type location: list | bytes
    :param order_by: Order by a field
    :type order_by: dict | bytes
    :param is_mobile: Location is mobile
    :type is_mobile: bool
    :param is_analysis: Data is the product of a previous analysis/aggregation and not raw measurements
    :type is_analysis: bool
    :param source_name: Name of the data source
    :type source_name: List[str]
    :param entity: Source entity type.
    :type entity: dict | bytes
    :param sensor_type: Type of Sensor
    :type sensor_type: dict | bytes
    :param model_name: Model Name of Sensor
    :type model_name: List[str]
    :param manufacturer_name: Manufacturer of Sensor
    :type manufacturer_name: List[str]
    :param dump_raw: 
    :type dump_raw: bool

    """
    sort = .from_dict(sort)
    parameter = [ParameterInner.from_dict(d) for d in parameter]
    location = [LocationInner.from_dict(d) for d in location]
    order_by = .from_dict(order_by)
    entity = .from_dict(entity)
    sensor_type = .from_dict(sensor_type)
    return web.Response(status=200)


async def measurements_get_v2_measurements_get(request: web.Request, format=None, date_from=None, date_to=None, limit=None, page=None, offset=None, sort=None, has_geo=None, parameter_id=None, parameter=None, unit=None, coordinates=None, radius=None, country_id=None, country=None, city=None, location_id=None, location=None, order_by=None, is_mobile=None, is_analysis=None, project=None, entity=None, sensor_type=None, value_from=None, value_to=None, include_fields=None) -> web.Response:
    """Measurements Get

    

    :param format: 
    :type format: str
    :param date_from: 
    :type date_from: dict | bytes
    :param date_to: 
    :type date_to: dict | bytes
    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: 
    :type sort: dict | bytes
    :param has_geo: 
    :type has_geo: bool
    :param parameter_id: 
    :type parameter_id: int
    :param parameter: 
    :type parameter: list | bytes
    :param unit: 
    :type unit: List[str]
    :param coordinates: 
    :type coordinates: str
    :param radius: 
    :type radius: int
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param city:          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)         
    :type city: List[str]
    :param location_id: 
    :type location_id: int
    :param location: 
    :type location: list | bytes
    :param order_by: 
    :type order_by: dict | bytes
    :param is_mobile: 
    :type is_mobile: bool
    :param is_analysis: 
    :type is_analysis: bool
    :param project: 
    :type project: int
    :param entity: 
    :type entity: dict | bytes
    :param sensor_type: 
    :type sensor_type: dict | bytes
    :param value_from: 
    :type value_from: 
    :param value_to: 
    :type value_to: 
    :param include_fields: 
    :type include_fields: str

    """
    date_from = .from_dict(date_from)
    date_to = .from_dict(date_to)
    sort = .from_dict(sort)
    parameter = [ParameterInner.from_dict(d) for d in parameter]
    location = [LocationInner.from_dict(d) for d in location]
    order_by = .from_dict(order_by)
    entity = .from_dict(entity)
    sensor_type = .from_dict(sensor_type)
    return web.Response(status=200)


async def mfr_get_v2_manufacturers_get(request: web.Request, ) -> web.Response:
    """Mfr Get

    


    """
    return web.Response(status=200)


async def mobilegentilejson_v2_locations_tiles_mobile_generalized_tiles_json_get(request: web.Request, ) -> web.Response:
    """Mobilegentilejson

    


    """
    return web.Response(status=200)


async def mobiletilejson_v2_locations_tiles_mobile_tiles_json_get(request: web.Request, ) -> web.Response:
    """Mobiletilejson

    


    """
    return web.Response(status=200)


async def model_get_v2_models_get(request: web.Request, ) -> web.Response:
    """Model Get

    


    """
    return web.Response(status=200)


async def parameters_get_v2_parameters_get(request: web.Request, limit=None, page=None, offset=None, sort=None, source_name=None, source_id=None, source_slug=None, order_by=None) -> web.Response:
    """Parameters Get

    

    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Define sort order.
    :type sort: dict | bytes
    :param source_name: 
    :type source_name: List[str]
    :param source_id: 
    :type source_id: List[int]
    :param source_slug: 
    :type source_slug: List[str]
    :param order_by: 
    :type order_by: dict | bytes

    """
    sort = .from_dict(sort)
    order_by = .from_dict(order_by)
    return web.Response(status=200)


async def projects_get_v2_projects_get(request: web.Request, country_id=None, country=None, limit=None, page=None, offset=None, sort=None, parameter_id=None, parameter=None, unit=None, project_id=None, project=None, order_by=None, is_mobile=None, is_analysis=None, entity=None, sensor_type=None, source_name=None) -> web.Response:
    """Projects Get

    

    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Define sort order.
    :type sort: dict | bytes
    :param parameter_id: 
    :type parameter_id: int
    :param parameter: 
    :type parameter: list | bytes
    :param unit: 
    :type unit: List[str]
    :param project_id: 
    :type project_id: int
    :param project: 
    :type project: list | bytes
    :param order_by: 
    :type order_by: dict | bytes
    :param is_mobile: 
    :type is_mobile: bool
    :param is_analysis: 
    :type is_analysis: bool
    :param entity: 
    :type entity: str
    :param sensor_type: 
    :type sensor_type: str
    :param source_name: 
    :type source_name: List[str]

    """
    sort = .from_dict(sort)
    parameter = [ParameterInner.from_dict(d) for d in parameter]
    project = [ParameterInner.from_dict(d) for d in project]
    order_by = .from_dict(order_by)
    return web.Response(status=200)


async def projects_get_v2_projects_project_id_get(request: web.Request, project_id, country_id=None, country=None, limit=None, page=None, offset=None, sort=None, parameter_id=None, parameter=None, unit=None, project=None, order_by=None, is_mobile=None, is_analysis=None, entity=None, sensor_type=None, source_name=None) -> web.Response:
    """Projects Get

    

    :param project_id: 
    :type project_id: int
    :param country_id:          Limit results by a certain country using two letter country code.         (ex. /US)         
    :type country_id: str
    :param country:          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)         
    :type country: List[str]
    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Define sort order.
    :type sort: dict | bytes
    :param parameter_id: 
    :type parameter_id: int
    :param parameter: 
    :type parameter: list | bytes
    :param unit: 
    :type unit: List[str]
    :param project: 
    :type project: list | bytes
    :param order_by: 
    :type order_by: dict | bytes
    :param is_mobile: 
    :type is_mobile: bool
    :param is_analysis: 
    :type is_analysis: bool
    :param entity: 
    :type entity: str
    :param sensor_type: 
    :type sensor_type: str
    :param source_name: 
    :type source_name: List[str]

    """
    sort = .from_dict(sort)
    parameter = [ParameterInner.from_dict(d) for d in parameter]
    project = [ParameterInner.from_dict(d) for d in project]
    order_by = .from_dict(order_by)
    return web.Response(status=200)


async def readme_get_v2_sources_readme_slug_get(request: web.Request, slug) -> web.Response:
    """Readme Get

    

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_get_v2_sources_get(request: web.Request, limit=None, page=None, offset=None, sort=None, source_name=None, source_id=None, source_slug=None, order_by=None) -> web.Response:
    """Sources Get

    

    :param limit: Change the number of results returned.
    :type limit: int
    :param page: Paginate through results.
    :type page: int
    :param offset: 
    :type offset: int
    :param sort: Define sort order.
    :type sort: dict | bytes
    :param source_name: 
    :type source_name: List[str]
    :param source_id: 
    :type source_id: List[int]
    :param source_slug: 
    :type source_slug: List[str]
    :param order_by: 
    :type order_by: dict | bytes

    """
    sort = .from_dict(sort)
    order_by = .from_dict(order_by)
    return web.Response(status=200)


async def summary_get_v2_summary_get(request: web.Request, ) -> web.Response:
    """Summary Get

    


    """
    return web.Response(status=200)


async def tilejson_v2_locations_tiles_tiles_json_get(request: web.Request, ) -> web.Response:
    """Tilejson

    


    """
    return web.Response(status=200)
