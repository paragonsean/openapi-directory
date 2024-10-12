from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_place import TflApiPresentationEntitiesPlace
from openapi_server.models.tfl_api_presentation_entities_place_category import TflApiPresentationEntitiesPlaceCategory
from openapi_server.models.tfl_api_presentation_entities_stop_point import TflApiPresentationEntitiesStopPoint
from openapi_server import util


async def place_get(request: web.Request, id, include_children=None) -> web.Response:
    """Gets the place with the given id.

    

    :param id: The id of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their ids
    :type id: str
    :param include_children: Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned
    :type include_children: bool

    """
    return web.Response(status=200)


async def place_get_at(request: web.Request, type, lat, lon, location_lat, location_lon, lat2, lon2) -> web.Response:
    """Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place              must be polygonal e.g. a BoroughBoundary.

    

    :param type: The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint)
    :type type: List[str]
    :param lat: 
    :type lat: str
    :param lon: 
    :type lon: str
    :param location_lat: 
    :type location_lat: float
    :param location_lon: 
    :type location_lon: float
    :param lat2: Automatically added
    :type lat2: str
    :param lon2: Automatically added
    :type lon2: str

    """
    return web.Response(status=200)


async def place_get_by_geo(request: web.Request, radius=None, categories=None, include_children=None, type=None, active_only=None, number_of_places_to_return=None, place_geo_sw_lat=None, place_geo_sw_lon=None, place_geo_ne_lat=None, place_geo_ne_lon=None, place_geo_lat=None, place_geo_lon=None) -> web.Response:
    """Gets the places that lie within a geographic region. The geographic region of interest can either be specified              by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of              its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.              Optionally filters on type and can strip properties for a smaller payload.

    

    :param radius: The radius of the bounding circle in metres when only lat/lon are specified.
    :type radius: float
    :param categories: An optional list of comma separated property categories to return in the Place&#39;s property bag. If null or empty, all categories of property are returned. Pass the keyword \&quot;none\&quot; to return no properties (a valid list of categories can be obtained from the /Place/Meta/categories endpoint)
    :type categories: List[str]
    :param include_children: Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned
    :type include_children: bool
    :param type: Place types to filter on, or null to return all types
    :type type: List[str]
    :param active_only: An optional parameter to limit the results to active records only (Currently only the &#39;VariableMessageSign&#39; place type is supported)
    :type active_only: bool
    :param number_of_places_to_return: If specified, limits the number of returned places equal to the given value
    :type number_of_places_to_return: int
    :param place_geo_sw_lat: 
    :type place_geo_sw_lat: float
    :param place_geo_sw_lon: 
    :type place_geo_sw_lon: float
    :param place_geo_ne_lat: 
    :type place_geo_ne_lat: float
    :param place_geo_ne_lon: 
    :type place_geo_ne_lon: float
    :param place_geo_lat: 
    :type place_geo_lat: float
    :param place_geo_lon: 
    :type place_geo_lon: float

    """
    return web.Response(status=200)


async def place_get_by_type(request: web.Request, types, active_only=None) -> web.Response:
    """Gets all places of a given type

    

    :param types: A comma-separated list of the types to return. Max. approx 12 types.              A valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint.
    :type types: List[str]
    :param active_only: An optional parameter to limit the results to active records only (Currently only the &#39;VariableMessageSign&#39; place type is supported)
    :type active_only: bool

    """
    return web.Response(status=200)


async def place_get_overlay(request: web.Request, z, type, width, height, lat, lon, location_lat, location_lon, lat2, lon2) -> web.Response:
    """Gets the place overlay for a given set of co-ordinates and a given width/height.

    

    :param z: The zoom level
    :type z: int
    :param type: The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint)
    :type type: List[str]
    :param width: The width of the requested overlay.
    :type width: int
    :param height: The height of the requested overlay.
    :type height: int
    :param lat: 
    :type lat: str
    :param lon: 
    :type lon: str
    :param location_lat: 
    :type location_lat: float
    :param location_lon: 
    :type location_lon: float
    :param lat2: Automatically added
    :type lat2: str
    :param lon2: Automatically added
    :type lon2: str

    """
    return web.Response(status=200)


async def place_get_streets_by_post_code(request: web.Request, postcode, postcode2, postcode_input_postcode=None) -> web.Response:
    """Gets the set of streets associated with a post code.

    

    :param postcode: 
    :type postcode: str
    :param postcode2: Automatically added
    :type postcode2: str
    :param postcode_input_postcode: 
    :type postcode_input_postcode: str

    """
    return web.Response(status=200)


async def place_meta_categories(request: web.Request, ) -> web.Response:
    """Gets a list of all of the available place property categories and keys.

    


    """
    return web.Response(status=200)


async def place_meta_place_types(request: web.Request, ) -> web.Response:
    """Gets a list of the available types of Place.

    


    """
    return web.Response(status=200)


async def place_search(request: web.Request, name, types=None) -> web.Response:
    """Gets all places that matches the given query

    

    :param name: The name of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their names.
    :type name: str
    :param types: A comma-separated list of the types to return. Max. approx 12 types.
    :type types: List[str]

    """
    return web.Response(status=200)
