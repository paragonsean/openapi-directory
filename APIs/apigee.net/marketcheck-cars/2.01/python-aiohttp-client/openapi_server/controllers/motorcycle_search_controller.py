from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listing_extra_attributes import ListingExtraAttributes
from openapi_server.models.listing_media import ListingMedia
from openapi_server.models.motorcycle_listing import MotorcycleListing
from openapi_server.models.motorcycle_search_response import MotorcycleSearchResponse
from openapi_server.models.search_auto_complete_response import SearchAutoCompleteResponse
from openapi_server import util


async def listing_motorcycle_id_extra_get(request: web.Request, id, api_key=None) -> web.Response:
    """Long text Motorcycle Listings attributes for Listing with the given id

    Get Motorcycle listing options, features, seller comments

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_motorcycle_id_get(request: web.Request, id, api_key=None) -> web.Response:
    """Motorcycle listing by id

    Get a particular Motorcycle listing by its id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_motorcycle_id_media_get(request: web.Request, id, api_key=None) -> web.Response:
    """Motorcycle listing media by id

    Get Motorcycle listing media (photo, photos) by id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def search_motorcycle_active_get(request: web.Request, api_key=None, price_range=None, miles_range=None, msrp_range=None, latitude=None, longitude=None, radius=None, search_text=None, year=None, make=None, model=None, trim=None, vin=None, taxonomy_vin=None, inventory_type=None, stock_no=None, source=None, dealer_id=None, color=None, body_type=None, vehicle_type=None, cylinders=None, drivetrain=None, engine=None, fuel_type=None, transmission=None, state=None, city=None, zip=None, msa_code=None, sort_by=None, sort_order=None, rows=None, start=None, facets=None, range_facets=None, facet_sort=None, stats=None, last_seen_range=None, first_seen_range=None, last_seen_days=None, first_seen_days=None) -> web.Response:
    """Gets active motorcycle listings for the given search criteria

    This endpoint provides search on motorcycle inventory. This API produces a list of currently active motorcycles from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search motorcycles around a given geo-point within a given radius  2. Search motorcycles for a specific year / make / model or combination of these  3. Search motorcycles matching multiple year, make, model combinatins in the same search request 4. Filter results by most motorcycle specification attributes 5. Search for similar motorcycles by VIN or Taxonomy VIN  6. Filter motorcycles within a given price / miles range 7. Specify a sort order for the results on price / miles / listed date  8. Search motorcycles for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles for your search

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param search_text: To search a substring across entire document
    :type search_text: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param vin: To filter listing on their VIN
    :type vin: str
    :param taxonomy_vin: Taxonomy VIN of the motorcycle
    :type taxonomy_vin: str
    :param inventory_type: To filter listing on their condition. Either used or new
    :type inventory_type: str
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param source: To filter listing on their source
    :type source: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param color: Color of the vehicle
    :type color: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str
    :param facet_sort: Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    :type facet_sort: str
    :param stats: The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    :type stats: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
    :param last_seen_days: Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type last_seen_days: str
    :param first_seen_days: First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_days: str

    """
    return web.Response(status=200)


async def search_motorcycle_auto_complete_get(request: web.Request, _field, input, api_key=None, year=None, make=None, model=None, trim=None, body_type=None, vehicle_type=None, transmission=None, drivetrain=None, fuel_type=None, color=None, engine=None, state=None, city=None, inventory_type=None, ignore_case=None, term_counts=None, sort_by=None, seller_type=None, radius=None, zip=None, facet_min_count=None) -> web.Response:
    """API for auto-completion of inputs

    Auto-complete the inputs of your end users

    :param _field: Field name for which you want auto-completion
    :type _field: str
    :param input: Input entered so far
    :type input: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param color: Color of the vehicle
    :type color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param inventory_type: To filter listing on their condition. Either used or new
    :type inventory_type: str
    :param ignore_case: Boolean variable to indicate ignore case of current input
    :type ignore_case: bool
    :param term_counts: Boolean variable to indicate wheather to include term counts as well in response
    :type term_counts: bool
    :param sort_by: Sort the response, either by index or count(default)
    :type sort_by: str
    :param seller_type: seller type for autocomplete
    :type seller_type: str
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param facet_min_count: Provide minimum count value for facets
    :type facet_min_count: 

    """
    return web.Response(status=200)
