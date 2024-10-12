from typing import List, Dict
from aiohttp import web

from openapi_server.models.find_places_model import FindPlacesModel
from openapi_server.models.general_request_error import GeneralRequestError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.language import Language
from openapi_server import util


async def find_places_find_places_get(request: web.Request, text, language=None, key=None) -> web.Response:
    """Search for places. Complete words required.

    ## Search for places  You can use this endpoint to obtain &#x60;place_id&#x60; of the location you want, to be used in &#x60;point&#x60; endpoint. The response also contains detailed information about the location, such as coordinates, timezone and the country the place belongs to.  Unlike the &#x60;/find_place_prefix&#x60; endpoint, complete words are required here. You can search for cities, mountains, lakes, countries, ZIP codes, etc. The response can contain multiple places, sorted by relevance. You can then identify the one you want by coordinates, country, or the administrative area.

    :param text: Place name or ZIP code
    :type text: str
    :param language: The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech 
    :type language: dict | bytes
    :param key: Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header.
    :type key: str

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def find_places_prefix_find_places_prefix_get(request: web.Request, text, language=None, key=None) -> web.Response:
    """Prefix search for places. Useful for autocomplete forms.

    ## Search for places by prefix  You can use this endpoint to obtain &#x60;place_id&#x60; of the location you want, to be used in &#x60;point&#x60; endpoint. The response also contains detailed information about the location, such as coordinates, timezone and the country the place belongs to.  Unlike the &#x60;/find_places&#x60; endpoint, you should only specify the prefix of the place you are looking for. This is particularly useful for autocomplete forms. You can search for cities, mountains, lakes, countries, ZIP codes, etc. The response can contain multiple places, sorted by relevance. You can then identify the one you want by coordinates, country, or the administrative area.

    :param text: Place name or ZIP code
    :type text: str
    :param language: The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech 
    :type language: dict | bytes
    :param key: Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header.
    :type key: str

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def nearest_place_nearest_place_get(request: web.Request, lat, lon, language=None, key=None) -> web.Response:
    """Returns the nearest named location for a given GPS coordinates.

    ## Search for nearest place by coordinates  You can use this endpoint to find the nearest place from given coordinates.  *Note: If you specify coordinates of a secluded place (e.g. middle of the ocean), the nearest point can be very far from the coordinates.*

    :param lat: Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
    :type lat: str
    :param lon: Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
    :type lon: str
    :param language: The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech 
    :type language: dict | bytes
    :param key: Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header.
    :type key: str

    """
    language = .from_dict(language)
    return web.Response(status=200)
