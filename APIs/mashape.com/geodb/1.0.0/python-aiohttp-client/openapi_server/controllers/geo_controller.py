from typing import List, Dict
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
from openapi_server import util


async def find_admin_divisions_using_get(request: web.Request, location=None, radius=None, distance_unit=None, country_ids=None, excluded_country_ids=None, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find administrative divisions

    Find administrative divisions, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

    :param location: Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    :type location: str
    :param radius: The location radius within which to find places
    :type radius: int
    :param distance_unit: The unit of distance: MI | KM
    :type distance_unit: str
    :param country_ids: Only places in these countries (comma-delimited country codes or WikiData ids)
    :type country_ids: str
    :param excluded_country_ids: Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    :type excluded_country_ids: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def find_cities_near_admin_division_using_get(request: web.Request, division_id, radius=None, distance_unit=None, country_ids=None, excluded_country_ids=None, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, types=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find cities near division

    Find cities near the given administrative division, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

    :param division_id: An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type division_id: str
    :param radius: The location radius within which to find places
    :type radius: int
    :param distance_unit: The unit of distance: MI | KM
    :type distance_unit: str
    :param country_ids: Only places in these countries (comma-delimited country codes or WikiData ids)
    :type country_ids: str
    :param excluded_country_ids: Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    :type excluded_country_ids: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param types: Only places for these types (comma-delimited): CITY | ADM2
    :type types: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def find_cities_near_city_using_get(request: web.Request, city_id, radius=None, distance_unit=None, country_ids=None, excluded_country_ids=None, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, types=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find cities near city

    Find cities near the given origin city, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

    :param city_id: A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type city_id: str
    :param radius: The location radius within which to find places
    :type radius: int
    :param distance_unit: The unit of distance: MI | KM
    :type distance_unit: str
    :param country_ids: Only places in these countries (comma-delimited country codes or WikiData ids)
    :type country_ids: str
    :param excluded_country_ids: Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    :type excluded_country_ids: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param types: Only places for these types (comma-delimited): CITY | ADM2
    :type types: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def find_cities_near_location_using_get(request: web.Request, location_id, radius=None, distance_unit=None, country_ids=None, excluded_country_ids=None, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, types=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find cities near location

    Find cities near the given location, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

    :param location_id: A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    :type location_id: str
    :param radius: The location radius within which to find places
    :type radius: int
    :param distance_unit: The unit of distance: MI | KM
    :type distance_unit: str
    :param country_ids: Only places in these countries (comma-delimited country codes or WikiData ids)
    :type country_ids: str
    :param excluded_country_ids: Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    :type excluded_country_ids: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param types: Only places for these types (comma-delimited): CITY | ADM2
    :type types: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def find_cities_using_get(request: web.Request, location=None, radius=None, distance_unit=None, country_ids=None, excluded_country_ids=None, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, types=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find cities

    Find cities, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

    :param location: Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    :type location: str
    :param radius: The location radius within which to find places
    :type radius: int
    :param distance_unit: The unit of distance: MI | KM
    :type distance_unit: str
    :param country_ids: Only places in these countries (comma-delimited country codes or WikiData ids)
    :type country_ids: str
    :param excluded_country_ids: Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    :type excluded_country_ids: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param types: Only places for these types (comma-delimited): CITY | ADM2
    :type types: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def find_divisions_near_admin_division_using_get(request: web.Request, division_id, radius=None, distance_unit=None, country_ids=None, excluded_country_ids=None, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find divisions near division

    Find administrative divisions near the given origin division, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

    :param division_id: An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type division_id: str
    :param radius: The location radius within which to find places
    :type radius: int
    :param distance_unit: The unit of distance: MI | KM
    :type distance_unit: str
    :param country_ids: Only places in these countries (comma-delimited country codes or WikiData ids)
    :type country_ids: str
    :param excluded_country_ids: Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    :type excluded_country_ids: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def find_divisions_near_location_using_get(request: web.Request, location_id, radius=None, distance_unit=None, country_ids=None, excluded_country_ids=None, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find divisions near location

    Find administrative divisions near the given location, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

    :param location_id: A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    :type location_id: str
    :param radius: The location radius within which to find places
    :type radius: int
    :param distance_unit: The unit of distance: MI | KM
    :type distance_unit: str
    :param country_ids: Only places in these countries (comma-delimited country codes or WikiData ids)
    :type country_ids: str
    :param excluded_country_ids: Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    :type excluded_country_ids: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def find_region_cities_using_get(request: web.Request, country_id, region_code, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, types=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find country region cities

    Get the cities in a specific country region. The country and region info is omitted in the response. 

    :param country_id: An ISO-3166 country code or WikiData id
    :type country_id: str
    :param region_code: An ISO-3166 or FIPS region code
    :type region_code: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param types: Only places for these types (comma-delimited): CITY | ADM2
    :type types: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort place results.  &#39;Format: ±SORT_FIELD,±SORT_FIELD&#39;  where SORT_FIELD &#x3D; elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def find_region_divisions_using_get(request: web.Request, country_id, region_code, min_population=None, max_population=None, name_prefix=None, name_prefix_default_lang_results=None, time_zone_ids=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None, include_deleted=None) -> web.Response:
    """Find country region administrative divisions

    Get the administrative divisions in a specific country region. The country and region info is omitted in the response. 

    :param country_id: An ISO-3166 country code or WikiData id
    :type country_id: str
    :param region_code: An ISO-3166 or FIPS region code
    :type region_code: str
    :param min_population: Only places having at least this population
    :type min_population: int
    :param max_population: Only places having no more than this population
    :type max_population: int
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param time_zone_ids: Only places in these time-zones (comma-delimited)
    :type time_zone_ids: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort place results.  &#39;Format: ±SORT_FIELD,±SORT_FIELD&#39;  where SORT_FIELD &#x3D; elevation | name | population 
    :type sort: str
    :param include_deleted: Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    :type include_deleted: str

    """
    return web.Response(status=200)


async def get_admin_division_using_get(request: web.Request, division_id, ascii_mode=None, language_code=None) -> web.Response:
    """Get administrative division details

    Get the details for a specific administrative division, including location coordinates, population, and elevation above sea-level (if available). 

    :param division_id: An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type division_id: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param language_code: Display results in this language
    :type language_code: str

    """
    return web.Response(status=200)


async def get_city_date_time_using_get(request: web.Request, city_id) -> web.Response:
    """Get city date-time

    Get city date-time

    :param city_id: A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type city_id: str

    """
    return web.Response(status=200)


async def get_city_distance_using_get(request: web.Request, city_id, to_city_id, distance_unit=None) -> web.Response:
    """Get city distance

    Get distance from the given city

    :param city_id: A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type city_id: str
    :param to_city_id: Distance to this city
    :type to_city_id: str
    :param distance_unit: The unit of distance: MI | KM
    :type distance_unit: str

    """
    return web.Response(status=200)


async def get_city_located_in_using_get(request: web.Request, city_id, ascii_mode=None, language_code=None) -> web.Response:
    """Get city admin region

    Get the details for the containing populated place (e.g., its county or other administrative division), including location coordinates, population, and elevation above sea-level (if available). 

    :param city_id: A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type city_id: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param language_code: Display results in this language
    :type language_code: str

    """
    return web.Response(status=200)


async def get_city_time_using_get(request: web.Request, city_id) -> web.Response:
    """Get city time

    Get city time

    :param city_id: A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type city_id: str

    """
    return web.Response(status=200)


async def get_city_using_get(request: web.Request, city_id, ascii_mode=None, language_code=None) -> web.Response:
    """Get city details

    Get the details for a specific city, including location coordinates, population, and elevation above sea-level (if available). 

    :param city_id: A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;)
    :type city_id: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param language_code: Display results in this language
    :type language_code: str

    """
    return web.Response(status=200)


async def get_countries_using_get(request: web.Request, currency_code=None, name_prefix=None, name_prefix_default_lang_results=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None) -> web.Response:
    """Find countries

    Find countries, filtering by optional criteria. If no criteria are set, you will get back all known countries. 

    :param currency_code: Only countries supporting this currency
    :type currency_code: str
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort countries.  Format: ±SORT_FIELD  where SORT_FIELD &#x3D; code | name
    :type sort: str

    """
    return web.Response(status=200)


async def get_country_using_get(request: web.Request, country_id, ascii_mode=None, language_code=None) -> web.Response:
    """Get country details

    Get the details for a specific country, including number of regions.

    :param country_id: An ISO-3166 country code or WikiData id
    :type country_id: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param language_code: Display results in this language
    :type language_code: str

    """
    return web.Response(status=200)


async def get_region_using_get(request: web.Request, country_id, region_code, ascii_mode=None, language_code=None) -> web.Response:
    """Get region details

    Get the details of a specific country region, including number of cities.

    :param country_id: An ISO-3166 country code or WikiData id
    :type country_id: str
    :param region_code: An ISO-3166 or FIPS region code
    :type region_code: str
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param language_code: Display results in this language
    :type language_code: str

    """
    return web.Response(status=200)


async def get_regions_using_get(request: web.Request, country_id, name_prefix=None, name_prefix_default_lang_results=None, ascii_mode=None, hateoas_mode=None, language_code=None, limit=None, offset=None, sort=None) -> web.Response:
    """Find country regions

    Get all regions in a specific country. These could be states, provinces, districts, or otherwise major political divisions. 

    :param country_id: An ISO-3166 country code or WikiData id
    :type country_id: str
    :param name_prefix: Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    :type name_prefix: str
    :param name_prefix_default_lang_results: When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    :type name_prefix_default_lang_results: bool
    :param ascii_mode: Display results using ASCII characters
    :type ascii_mode: bool
    :param hateoas_mode: Include HATEOAS-style links in results
    :type hateoas_mode: bool
    :param language_code: Display results in this language
    :type language_code: str
    :param limit: The maximum number of results to retrieve
    :type limit: int
    :param offset: The zero-ary offset index into the results
    :type offset: int
    :param sort: How to sort regions.  Format: ±SORT_FIELD  where SORT_FIELD &#x3D; fipsCode | isoCode | name
    :type sort: str

    """
    return web.Response(status=200)
