from typing import List, Dict
from aiohttp import web

from openapi_server.models.airports_search_response import AirportsSearchResponse
from openapi_server.models.cities_response import CitiesResponse
from openapi_server.models.continents_response import ContinentsResponse
from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def get_airport(request: web.Request, language, location=None, radius=None, countrycode=None, top_airports=None) -> web.Response:
    """Search airports by country / Search nearby airports / Search an airport

    This webservice is providing you the ability to retrieve a list of airports matching your search criterias.&lt;br /&gt;The 3 mains search criterias are&lt;br /&gt;- by country code, this will list all airports for a given country.&lt;br /&gt;- by latitude/longitude with a radius in km. You can actually combine those 2 criterias, and search for example the closest airport in the USA of Vancoucer, Canada.&lt;br /&gt;- The last way to use the API is by searching directly with a IATA CODE in the location parameter, this will only return one result in the array of data results

    :param language: the language code of the language you want the content to be returned
    :type language: str
    :param location: The location you want to search for. Either a latitude/longitude point or a letter airport IATA CODE ( ex. LHR ) if you want the detail for only one single airport.
    :type location: str
    :param radius: Radius in km for a lat/long search, will be ignore if a IATA is passed in location parameter code is passed
    :type radius: int
    :param countrycode: Filter - The country ISO code 2 letters, provided by the GET /countries. If passed the results will be filtered to this country only, regardless if you passed a lat/long and a large radius
    :type countrycode: str
    :param top_airports: Filter the results to only the top and large airports airports.
    :type top_airports: bool

    """
    return web.Response(status=200)


async def get_autocomplete(request: web.Request, q, language, sort, countrycode=None) -> web.Response:
    """Retrieve cities informations from a string / build an autocomplete

    Search cities from a string parameters.

    :param q: the string you want to search
    :type q: str
    :param language: the language code of the language you want the content to be returned
    :type language: str
    :param sort: The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
    :type sort: str
    :param countrycode: if you want to limit the result to one country
    :type countrycode: str

    """
    return web.Response(status=200)


async def get_cities(request: web.Request, language, sort, countrycode=None, location=None, radius=None, limit=None, offset=None) -> web.Response:
    """Search all cities from lat/long or countrycode

    Search cities according to given criterias. Either lat/long + radius or country code. A limit can be given but cannot exceed 50 results.&lt;br /&gt; A significant city will be defined according to the pourcent of population within a country.

    :param language: the language code of the language you want the content to be returned
    :type language: str
    :param sort: The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
    :type sort: str
    :param countrycode: if you want to limit the result to one country
    :type countrycode: str
    :param location: The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456)
    :type location: str
    :param radius: Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed
    :type radius: int
    :param limit: Limit of the result. Default is 20 rows, and maximum is 50.
    :type limit: int
    :param offset: offset of the result set
    :type offset: int

    """
    return web.Response(status=200)


async def get_continents(request: web.Request, language, continentcode=None) -> web.Response:
    """Search all continents or one specific continent

    This webservice is providing you the ability to retrieve all informations about continents

    :param language: The language code of the language you want the content to be returned
    :type language: str
    :param continentcode: The code of the continent you want to retrieve, this parameter is not required if you want ot retrieve all continents at once
    :type continentcode: str

    """
    return web.Response(status=200)


async def get_countries(request: web.Request, language, countrycode=None) -> web.Response:
    """Search all countries or one specific country

    This webservice is providing you the ability to retrieve a list of countries matching your search criterias.&lt;br /&gt;The 2 mains ways to search use this API are&lt;br /&gt;- by countrycode, it will only returns you one country&lt;br /&gt;- without the countrycode parameter which will return the full list of countries

    :param language: the language code of the language you want the content to be returned
    :type language: str
    :param countrycode: The code of the country you want to retrieve
    :type countrycode: str

    """
    return web.Response(status=200)


async def get_significant_cities(request: web.Request, language, sort, pourcent=None, countrycode=None, location=None, radius=None, limit=None, offset=None) -> web.Response:
    """Search significant cities from lat/long or countrycode

    Search cities according to given criterias. Either lat/long + radius or country code. A limit can be given but cannot exceed 50 results.&lt;br /&gt; A significant city will be defined according to the pourcent of population within a country.

    :param language: the language code of the language you want the content to be returned
    :type language: str
    :param sort: The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
    :type sort: str
    :param pourcent: The pourcent of population the cities need to be in order to appear in results
    :type pourcent: 
    :param countrycode: if you want to limit the result to one country
    :type countrycode: str
    :param location: The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456)
    :type location: str
    :param radius: Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed
    :type radius: int
    :param limit: Limit of the result. Default is 20 rows, and maximum is 50.
    :type limit: int
    :param offset: offset of the result set
    :type offset: int

    """
    return web.Response(status=200)
