from typing import List, Dict
from aiohttp import web

from openapi_server.models.dealer import Dealer
from openapi_server.models.dealers_response import DealersResponse
from openapi_server.models.error import Error
from openapi_server import util


async def dealer_car_uk_id_get(request: web.Request, id, api_key=None, provider=None) -> web.Response:
    """Dealer by id

    Get a particular dealer&#39;s information by its id

    :param id: Dealer id to get all the dealer info attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool

    """
    return web.Response(status=200)


async def dealer_heavy_equipment_id_get(request: web.Request, id, api_key=None, provider=None) -> web.Response:
    """Dealer by id

    Get a particular dealer&#39;s information by its id

    :param id: Dealer id to get all the dealer info attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool

    """
    return web.Response(status=200)


async def dealer_motorcycle_id_get(request: web.Request, id, api_key=None, provider=None) -> web.Response:
    """Dealer by id

    Get a particular dealer&#39;s information by its id

    :param id: Dealer id to get all the dealer info attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool

    """
    return web.Response(status=200)


async def dealer_rv_id_get(request: web.Request, id, api_key=None, provider=None) -> web.Response:
    """Dealer by id

    Get a particular dealer&#39;s information by its id

    :param id: Dealer id to get all the dealer info attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool

    """
    return web.Response(status=200)


async def dealer_search(request: web.Request, api_key=None, latitude=None, longitude=None, radius=None, rows=None, start=None, country=None, dealer_type=None, city=None, state=None, listing_count_range=None, inventory_url=None, zip=None, sort_by=None, sort_order=None, provider=None, facets=None, range_facets=None) -> web.Response:
    """Find car dealers around

    The dealers API returns a list of dealers around a given point and radius.

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param listing_count_range: To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    :type listing_count_range: str
    :param inventory_url: inventory_url of dealer to be searched
    :type inventory_url: str
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str

    """
    return web.Response(status=200)


async def dealers_car_uk_get(request: web.Request, api_key=None, latitude=None, longitude=None, radius=None, rows=None, start=None, country=None, dealer_type=None, city=None, county=None, listing_count_range=None, inventory_url=None, postal_code=None, sort_by=None, sort_order=None, provider=None, facets=None, range_facets=None) -> web.Response:
    """Find car dealers around

    The dealers API returns a list of dealers around a given point and radius.

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param county: To filter listing on county in which they are listed
    :type county: str
    :param listing_count_range: To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    :type listing_count_range: str
    :param inventory_url: inventory_url of dealer to be searched
    :type inventory_url: str
    :param postal_code: To filter listing on postal code around which they are listed
    :type postal_code: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str

    """
    return web.Response(status=200)


async def dealers_heavy_equipment_get(request: web.Request, api_key=None, latitude=None, longitude=None, radius=None, rows=None, start=None, country=None, dealer_type=None, city=None, state=None, listing_count_range=None, inventory_url=None, zip=None, sort_by=None, sort_order=None, provider=None, facets=None, range_facets=None) -> web.Response:
    """Find car dealers around

    The dealers API returns a list of dealers around a given point and radius.

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param listing_count_range: To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    :type listing_count_range: str
    :param inventory_url: inventory_url of dealer to be searched
    :type inventory_url: str
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str

    """
    return web.Response(status=200)


async def dealers_motorcycle_get(request: web.Request, api_key=None, latitude=None, longitude=None, radius=None, rows=None, start=None, country=None, dealer_type=None, city=None, state=None, listing_count_range=None, inventory_url=None, zip=None, sort_by=None, sort_order=None, provider=None, facets=None, range_facets=None) -> web.Response:
    """Find car dealers around

    The dealers API returns a list of dealers around a given point and radius.

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param listing_count_range: To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    :type listing_count_range: str
    :param inventory_url: inventory_url of dealer to be searched
    :type inventory_url: str
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str

    """
    return web.Response(status=200)


async def dealers_rv_get(request: web.Request, api_key=None, latitude=None, longitude=None, radius=None, rows=None, start=None, country=None, dealer_type=None, city=None, state=None, listing_count_range=None, inventory_url=None, zip=None, sort_by=None, sort_order=None, provider=None, facets=None, range_facets=None) -> web.Response:
    """Find car dealers around

    The dealers API returns a list of dealers around a given point and radius.

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param listing_count_range: To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
    :type listing_count_range: str
    :param inventory_url: inventory_url of dealer to be searched
    :type inventory_url: str
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str

    """
    return web.Response(status=200)


async def get_dealer(request: web.Request, id, api_key=None, provider=None) -> web.Response:
    """Dealer by id

    Get a particular dealer&#39;s information by its id

    :param id: Dealer id to get all the dealer info attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param provider: boolean param to include site providers name in response
    :type provider: bool

    """
    return web.Response(status=200)
