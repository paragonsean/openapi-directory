from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.place_detail import PlaceDetail
from openapi_server.models.places_search_response import PlacesSearchResponse
from openapi_server import util


async def places_get(request: web.Request, fieldset, category=None, function=None, ambience=None, tag=None, type=None, name=None, exact=None, capacity_min=None, capacity_max=None, street=None, locality=None, region=None, postal_code=None, country=None, center=None, radius=None, bbox=None, polygon=None, within=None, offset=None, limit=None) -> web.Response:
    """Venues, landmarks, regions, these are all places to search.

    

    :param fieldset: Return results starting at specified offset (summary, context, detail)
    :type fieldset: str
    :param category: List of required PlaceCategory ids (Tier 1)
    :type category: List[str]
    :param function: List of required PlaceFunction ids (Tier 2)
    :type function: List[str]
    :param ambience: List of required ambience ids
    :type ambience: List[str]
    :param tag: List of required tags
    :type tag: List[str]
    :param type: Specific PlaceType to return
    :type type: str
    :param name: Match on place names
    :type name: str
    :param exact: Require an exact name match
    :type exact: bool
    :param capacity_min: Min capacity at location
    :type capacity_min: 
    :param capacity_max: Min capacity at location
    :type capacity_max: 
    :param street: Address of the place or street component of the address
    :type street: str
    :param locality: city, town, or neighborhood of the place
    :type locality: str
    :param region: region or state
    :type region: str
    :param postal_code: Postal or zip code
    :type postal_code: str
    :param country: country component of the address
    :type country: str
    :param center: latitude,longitude of the origin point
    :type center: str
    :param radius: Distance from origin in meters
    :type radius: int
    :param bbox: Corner of a bounding box (lat,lng). Requires 0 or 2 pairs
    :type bbox: List[str]
    :param polygon: Closed custom polygon. Ordered list of lat,lng pairs
    :type polygon: List[str]
    :param within: Search within specified geopolitical place id
    :type within: str
    :param offset: Return results starting at specified offset
    :type offset: int
    :param limit: Max results to return
    :type limit: int

    """
    return web.Response(status=200)


async def places_id_get(request: web.Request, id, fieldset=None) -> web.Response:
    """Get specific place details

    

    :param id: place @id
    :type id: str
    :param fieldset: 
    :type fieldset: str

    """
    return web.Response(status=200)
