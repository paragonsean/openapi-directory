from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listing_extra_attributes import ListingExtraAttributes
from openapi_server.models.listing_media import ListingMedia
from openapi_server.models.rv_listing import RVListing
from openapi_server.models.rv_search_response import RVSearchResponse
from openapi_server.models.search_auto_complete_response import SearchAutoCompleteResponse
from openapi_server.models.ukrv_search_response import UKRVSearchResponse
from openapi_server import util


async def listing_rv_id_extra_get(request: web.Request, id, api_key=None) -> web.Response:
    """Long text RV Listings attributes for Listing with the given id

    Get RV listing options, features, seller comments

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_rv_id_get(request: web.Request, id, api_key=None) -> web.Response:
    """RV listing by id

    Get a particular RV listing by its id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_rv_id_media_get(request: web.Request, id, api_key=None) -> web.Response:
    """Listing media by id

    Get listing media (photo, photos) by id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_rv_uk_id_extra_get(request: web.Request, id, api_key=None) -> web.Response:
    """Long text RV Listings attributes for Listing with the given id

    Get RV listing options, features, seller comments

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_rv_uk_id_get(request: web.Request, id, api_key=None) -> web.Response:
    """RV listing by id

    Get a particular RV listing by its id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_rv_uk_id_media_get(request: web.Request, id, api_key=None) -> web.Response:
    """Listing media by id

    Get listing media (photo, photos) by id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def search_rv_active_get(request: web.Request, api_key=None, price_range=None, miles_range=None, msrp_range=None, year_range=None, search_text=None, latitude=None, longitude=None, radius=None, year=None, make=None, model=None, model_o=None, vin=None, inventory_type=None, stock_no=None, source=None, dealer_name=None, dealer_id=None, exterior_color=None, interior_color=None, engine=None, fuel_type=None, transmission=None, _class=None, state=None, city=None, zip=None, msa_code=None, sort_by=None, sort_order=None, rows=None, start=None, facets=None, range_facets=None, facet_sort=None, stats=None, last_seen_range=None, first_seen_range=None, last_seen_days=None, first_seen_days=None, slideouts=None, length_range=None, length=None, base_exterior_color=None, base_interior_color=None, seating_capacity=None, fresh_water_capacity=None, sleeps=None, cylinders=None, number_of_awnings=None, doors=None, gvwr=None) -> web.Response:
    """Gets active RV listings for the given search criteria

    This endpoint provides search on RV inventory. This API produces a list of currently active RV from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search RV around a given geo-point within a given radius  2. Search RV for a specific year / make / model or combination of these  3. Search RV matching multiple year, make, model combinatins in the same search request 4. Filter results by most RV specification attributes 5. Filter RV within a given price / miles range 6. Specify a sort order for the results on price / miles / listed date  7. Search RV for a given City / State combination  8. Get Facets to build the search drill downs  9. Get Market averages for price/miles for your search

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
    :param search_text: To search a substring across entire document
    :type search_text: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param model_o: To filter listings on their model orig (as described on the webpage)
    :type model_o: str
    :param vin: To filter listing on their VIN
    :type vin: str
    :param inventory_type: To filter listing on their condition. Either used or new
    :type inventory_type: str
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param source: To filter listing on their source
    :type source: str
    :param dealer_name: Filter listings on dealer_name
    :type dealer_name: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param _class: Filter RV listings on class
    :type _class: str
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
    :param slideouts: Filter RV listings on slideouts
    :type slideouts: str
    :param length_range: length range to filter listings with the length in the range given. Range to be given in the format - min-max e.g. 50-200
    :type length_range: str
    :param length: Filter RV listings on length
    :type length: str
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param fresh_water_capacity: To filter on fresh water capacity of vehicle
    :type fresh_water_capacity: str
    :param sleeps: To filter data based on sleeps
    :type sleeps: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param number_of_awnings: To filter on number_of_awnings
    :type number_of_awnings: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param gvwr: To filter on the maximum total weight of your vehicle
    :type gvwr: str

    """
    return web.Response(status=200)


async def search_rv_auto_complete_get(request: web.Request, _field, input, api_key=None, year=None, make=None, model=None, trim=None, body_type=None, vehicle_type=None, transmission=None, drivetrain=None, fuel_type=None, color=None, engine=None, state=None, city=None, inventory_type=None, ignore_case=None, term_counts=None, sort_by=None, seller_type=None, radius=None, zip=None, facet_min_count=None) -> web.Response:
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


async def search_rv_uk_active_get(request: web.Request, api_key=None, price_range=None, miles_range=None, msrp_range=None, year_range=None, search_text=None, latitude=None, longitude=None, radius=None, year=None, make=None, model=None, vin=None, source=None, dealer_name=None, dealer_id=None, exterior_color=None, interior_color=None, engine_size=None, fuel_type=None, category=None, state=None, city=None, county=None, postal_code=None, zip=None, sort_by=None, sort_order=None, rows=None, start=None, facets=None, range_facets=None, facet_sort=None, stats=None, last_seen_range=None, first_seen_range=None, last_seen_days=None, first_seen_days=None, base_exterior_color=None, base_interior_color=None, seating_capacity=None, cylinders=None, doors=None, mtplm=None, sub_category=None, availability_status=None, berths=None, inventory_type=None, width_range=None, exterior_length_range=None, interior_length_range=None, drive_type=None, steering=None, chassis=None, transmission=None) -> web.Response:
    """Gets active RV listings for the given search criteria

    This endpoint provides search on RV inventory. This API produces a list of currently active RV from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search RV around a given geo-point within a given radius  2. Search RV for a specific year / make / model or combination of these  3. Search RV matching multiple year, make, model combinatins in the same search request 4. Filter results by most RV specification attributes 5. Filter RV within a given price / miles range 6. Specify a sort order for the results on price / miles / listed date  7. Search RV for a given City / State combination  8. Get Facets to build the search drill downs  9. Get Market averages for price/miles for your search

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
    :param search_text: To search a substring across entire document
    :type search_text: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param vin: To filter listing on their VIN
    :type vin: str
    :param source: To filter listing on their source
    :type source: str
    :param dealer_name: Filter listings on dealer_name
    :type dealer_name: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param category: Filter RV listings on category
    :type category: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param county: To filter listing on county in which they are listed
    :type county: str
    :param postal_code: To filter listing on postal code around which they are listed
    :type postal_code: str
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
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
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param mtplm: To filter rv on mtplm
    :type mtplm: str
    :param sub_category: To filter rv on their sub-category
    :type sub_category: str
    :param availability_status: To filter rv on their availability_status
    :type availability_status: str
    :param berths: To filter rv on their berths
    :type berths: str
    :param inventory_type: To filter listing on their condition. Either used or new
    :type inventory_type: str
    :param width_range: width range to filter listings on width in the range given. Range to be given in the format - min-max e.g. 4-8
    :type width_range: str
    :param exterior_length_range: width range to filter listings on exterior_length in the range given. Range to be given in the format - min-max e.g. 4-8
    :type exterior_length_range: str
    :param interior_length_range: width range to filter listings on interior_length in the range given. Range to be given in the format - min-max e.g. 4-8
    :type interior_length_range: str
    :param drive_type: To filter rv on their drive_type
    :type drive_type: str
    :param steering: To filter rv on their steering
    :type steering: str
    :param chassis: To filter rv on their chassis
    :type chassis: str
    :param transmission: To filter listing on their transmission
    :type transmission: str

    """
    return web.Response(status=200)
