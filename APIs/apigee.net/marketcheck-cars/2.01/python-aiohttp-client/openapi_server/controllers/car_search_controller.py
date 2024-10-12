from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listing import Listing
from openapi_server.models.listing_extra_attributes import ListingExtraAttributes
from openapi_server.models.listing_media import ListingMedia
from openapi_server.models.search_auto_complete_response import SearchAutoCompleteResponse
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.uk_search_response import UKSearchResponse
from openapi_server import util


async def auto_complete(request: web.Request, _field, input, api_key=None, year=None, make=None, model=None, trim=None, body_type=None, body_subtype=None, vehicle_type=None, transmission=None, drivetrain=None, fuel_type=None, exterior_color=None, interior_color=None, engine=None, engine_size=None, engine_block=None, state=None, city=None, source=None, dealer_id=None, country=None, car_type=None, include_non_vin_listings=None, ignore_case=None, term_counts=None, sort_by=None, seller_type=None, radius=None, zip=None, inventory_count_range=None, exclude_dealer_ids=None, exclude_sources=None, in_transit=None, facet_min_count=None) -> web.Response:
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
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param source: To filter listing on their source only for widget requests
    :type source: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param car_type: Car type. Allowed values are - new / used
    :type car_type: str
    :param include_non_vin_listings: Flag to indicate whether to include non vin listing terms in results or not. Default is false to avoid un-normalised terms from non vin listings out of results
    :type include_non_vin_listings: str
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
    :param inventory_count_range: Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    :type inventory_count_range: str
    :param exclude_dealer_ids: A list of dealer ids to exclude from result
    :type exclude_dealer_ids: str
    :param exclude_sources: A list of sources to exclude from result
    :type exclude_sources: str
    :param in_transit: A boolean to filter in transit vehicles
    :type in_transit: str
    :param facet_min_count: Provide minimum count value for facets
    :type facet_min_count: 

    """
    return web.Response(status=200)


async def car_dealer_inventory_active_get(request: web.Request, api_key=None, append_api_key=None, latitude=None, longitude=None, radius=None, zip=None, include_lease=None, include_finance=None, lease_term=None, lease_down_payment=None, lease_emp=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None, car_type=None, carfax_1_owner=None, carfax_clean_title=None, year_range=None, year=None, make=None, model=None, trim=None, dealer_id=None, vin=None, source=None, body_type=None, body_subtype=None, vehicle_type=None, vins=None, taxonomy_vins=None, mm=None, ymm=None, ymmt=None, match=None, cylinders=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, base_exterior_color=None, base_interior_color=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, highway_mpg_range=None, city_mpg_range=None, miles_range=None, price_range=None, msrp_range=None, dom_range=None, sort_by=None, sort_order=None, rows=None, start=None, include_non_vin_listings=None, msa_code=None, facets=None, range_facets=None, facet_sort=None, stats=None, country=None, plot=None, nodedup=None, dedup=None, owned=None, state=None, city=None, dealer_name=None, dealership_group_name=None, trim_o=None, trim_r=None, dom_active_range=None, dom_180_range=None, exclude_certified=None, fuel_type=None, dealer_type=None, photo_links=None, photo_links_cached=None, stock_no=None, last_seen_range=None, first_seen_range=None, first_seen_at_source_range=None, first_seen_at_mc_range=None, last_seen_days=None, first_seen_days=None, first_seen_at_source_days=None, first_seen_at_mc_days=None, include_relevant_links=None, inventory_count_range=None, in_transit=None, seating_capacity=None, engine_size_range=None, powertrain_type=None, min_photo_links=None, min_photo_links_cached=None) -> web.Response:
    """Get dealers active inventory

    Get dealers active inventory

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param include_lease: Boolean param to search for listings that include leasing options in them
    :type include_lease: bool
    :param include_finance: Boolean param to search for listings that include finance options in them
    :type include_finance: bool
    :param lease_term: Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60
    :type lease_term: str
    :param lease_down_payment: Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60
    :type lease_down_payment: str
    :param lease_emp: Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60
    :type lease_emp: str
    :param finance_loan_term: Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60
    :type finance_loan_term: str
    :param finance_loan_apr: Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60
    :type finance_loan_apr: str
    :param finance_emp: Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60
    :type finance_emp: str
    :param finance_down_payment: Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60
    :type finance_down_payment: str
    :param finance_down_payment_per: Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60
    :type finance_down_payment_per: str
    :param car_type: Car type. Allowed values are - new / used / certified
    :type car_type: str
    :param carfax_1_owner: Indicates whether car has had only one owner or not
    :type carfax_1_owner: str
    :param carfax_clean_title: Indicates whether car has clean ownership records
    :type carfax_clean_title: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param vin: To filter listing on their VIN
    :type vin: str
    :param source: To filter listing on their source
    :type source: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param vins: Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    :type vins: str
    :param taxonomy_vins: Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    :type taxonomy_vins: str
    :param mm: Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
    :type mm: str
    :param ymm: Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
    :type ymm: str
    :param ymmt: Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations.
    :type ymmt: str
    :param match: Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    :type match: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_aspiration: Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    :type engine_aspiration: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param highway_mpg_range: Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type highway_mpg_range: str
    :param city_mpg_range: City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type city_mpg_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param dom_range: Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_range: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param include_non_vin_listings: To include non vin listings. Default is false
    :type include_non_vin_listings: bool
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str
    :param facet_sort: Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    :type facet_sort: str
    :param stats: The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    :type stats: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param plot: If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    :type plot: bool
    :param nodedup: If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    :type nodedup: bool
    :param dedup: If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    :type dedup: bool
    :param owned: Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    :type owned: bool
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param dealer_name: Filter listings on dealer_name
    :type dealer_name: str
    :param dealership_group_name: Name of the dealership group to search for
    :type dealership_group_name: str
    :param trim_o: Filter listings on web scraped trim
    :type trim_o: str
    :param trim_r: Filter trim on custom possible matches
    :type trim_r: str
    :param dom_active_range: Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_active_range: str
    :param dom_180_range: Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_180_range: str
    :param exclude_certified: Boolean param to exclude certified cars from search results
    :type exclude_certified: bool
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param photo_links: A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them
    :type photo_links: bool
    :param photo_links_cached: A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them
    :type photo_links_cached: bool
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
    :param first_seen_at_source_range: First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_source_range: str
    :param first_seen_at_mc_range: First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_mc_range: str
    :param last_seen_days: Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type last_seen_days: str
    :param first_seen_days: First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_days: str
    :param first_seen_at_source_days: First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_source_days: str
    :param first_seen_at_mc_days: First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_mc_days: str
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool
    :param inventory_count_range: Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    :type inventory_count_range: str
    :param in_transit: A boolean to filter in transit vehicles
    :type in_transit: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param engine_size_range: Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    :type engine_size_range: str
    :param powertrain_type: To filter on powertrain_type
    :type powertrain_type: str
    :param min_photo_links: Filter listings based by number of photo links within given range
    :type min_photo_links: str
    :param min_photo_links_cached: Filter listings based by number of cached photo links within given range
    :type min_photo_links_cached: str

    """
    return web.Response(status=200)


async def get_listing(request: web.Request, id, api_key=None, append_api_key=None, include_relevant_links=None) -> web.Response:
    """Listing by id

    Get a particular dealer listing by its id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool

    """
    return web.Response(status=200)


async def listing_car_auction_id_extra_get(request: web.Request, id, api_key=None) -> web.Response:
    """Long text Listings attributes for Listing with the given id

    Get listing options, features, seller comments

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_car_auction_id_get(request: web.Request, id, api_key=None, append_api_key=None, include_relevant_links=None) -> web.Response:
    """Listing by id

    Get a particular auction listing by its id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool

    """
    return web.Response(status=200)


async def listing_car_auction_id_media_get(request: web.Request, id, api_key=None, append_api_key=None) -> web.Response:
    """Listing media by id

    Get listing media (photo, photos) by id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool

    """
    return web.Response(status=200)


async def listing_car_fsbo_id_extra_get(request: web.Request, id, api_key=None) -> web.Response:
    """Long text Listings attributes for Listing with the given id

    Get listing options, features, seller comments

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_car_fsbo_id_get(request: web.Request, id, api_key=None, append_api_key=None, include_relevant_links=None) -> web.Response:
    """Listing by id

    Get a particular private party listing by its id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool

    """
    return web.Response(status=200)


async def listing_car_fsbo_id_media_get(request: web.Request, id, api_key=None, append_api_key=None) -> web.Response:
    """Listing media by id

    Get listing media (photo, photos) by id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool

    """
    return web.Response(status=200)


async def listing_car_id_extra_get(request: web.Request, id, api_key=None) -> web.Response:
    """Long text Listings attributes for Listing with the given id

    Get listing options, features, seller comments

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_car_id_media_get(request: web.Request, id, api_key=None, append_api_key=None) -> web.Response:
    """Listing media by id

    Get listing media (photo, photos) by id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool

    """
    return web.Response(status=200)


async def listing_car_uk_id_extra_get(request: web.Request, id, api_key=None) -> web.Response:
    """Long text Listings attributes for Listing with the given id

    Get listing options, features, seller comments

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def listing_car_uk_id_get(request: web.Request, id, api_key=None, append_api_key=None) -> web.Response:
    """Listing by id

    Get a particular dealer listing by its id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool

    """
    return web.Response(status=200)


async def listing_car_uk_id_media_get(request: web.Request, id, api_key=None, append_api_key=None) -> web.Response:
    """Listing media by id

    Get listing media (photo, photos) by id

    :param id: Listing id to get all the listing attributes
    :type id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool

    """
    return web.Response(status=200)


async def search(request: web.Request, api_key=None, append_api_key=None, latitude=None, longitude=None, radius=None, postal_code=None, zip=None, car_type=None, year=None, year_range=None, make=None, model=None, variant=None, trim=None, body_type=None, ymmt=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, engine=None, miles_range=None, price_range=None, msrp_range=None, sort_by=None, sort_order=None, rows=None, start=None, msa_code=None, facets=None, range_facets=None, facet_sort=None, stats=None, country=None, plot=None, nodedup=None, dedup=None, county=None, state=None, city=None, fuel_type=None, stock_no=None, dom_range=None, dom_active_range=None, dom_180_range=None, last_seen_range=None, first_seen_range=None, first_seen_at_source_range=None, first_seen_at_mc_range=None, last_seen_days=None, first_seen_days=None, first_seen_at_source_days=None, first_seen_at_mc_days=None, co2_emissions=None, insurance_group=None, vehicle_registration_mark=None, vehicle_registration_date_range=None, num_owners=None, inventory_count_range=None, source=None, dealer_id=None, exclude_sources=None, exclude_dealer_ids=None, in_transit=None, include_non_vin_listings=None, cylinders=None, photo_links=None, photo_links_cached=None, base_exterior_color=None, base_interior_color=None, write_off_category=None, exclude_write_off_category=None, fca_status=None, seating_capacity=None, vrm=None, powertrain_type=None, client_filters=None, boost=None, car_location_seller_name=None, car_location_street=None, car_location_city=None, car_location_county=None, car_location_zip=None, car_location_latitude=None, car_location_longitude=None, price_change=None, price_change_range=None, active_inventory_date_range=None, engine_size=None, engine_size_range=None, uvc_id=None, highway_mpg_range=None, city_mpg_range=None, combined_mpg_range=None, owned=None, min_photo_links=None, min_photo_links_cached=None, match=None, ulez_compliant=None) -> web.Response:
    """Gets active car listings in UK for the given search criteria

    Search cars for sale in UK

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param postal_code: To filter listing on postal code around which they are listed
    :type postal_code: str
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param car_type: Car type. Allowed values are - new / used
    :type car_type: str
    :param year: To filter listing on their year
    :type year: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param variant: To filter listing on their variant
    :type variant: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param ymmt: Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations.
    :type ymmt: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str
    :param facet_sort: Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    :type facet_sort: str
    :param stats: The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    :type stats: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param plot: If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    :type plot: bool
    :param nodedup: If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    :type nodedup: bool
    :param dedup: If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    :type dedup: bool
    :param county: To filter listing on county in which they are listed
    :type county: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param dom_range: Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_range: str
    :param dom_active_range: Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_active_range: str
    :param dom_180_range: Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_180_range: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
    :param first_seen_at_source_range: First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_source_range: str
    :param first_seen_at_mc_range: First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_mc_range: str
    :param last_seen_days: Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type last_seen_days: str
    :param first_seen_days: First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_days: str
    :param first_seen_at_source_days: First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_source_days: str
    :param first_seen_at_mc_days: First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_mc_days: str
    :param co2_emissions: CO2 emissions
    :type co2_emissions: str
    :param insurance_group: Insurance Group
    :type insurance_group: str
    :param vehicle_registration_mark: Vehicle Registration Mark
    :type vehicle_registration_mark: str
    :param vehicle_registration_date_range: Vehicle registration date range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type vehicle_registration_date_range: str
    :param num_owners: Number of owners. Range to be given in the format - min-max e.g. 1000-5000
    :type num_owners: str
    :param inventory_count_range: Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    :type inventory_count_range: str
    :param source: To filter listing on their source only for widget requests
    :type source: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param exclude_sources: A list of sources to exclude from result
    :type exclude_sources: str
    :param exclude_dealer_ids: A list of dealer ids to exclude from result
    :type exclude_dealer_ids: str
    :param in_transit: A boolean to filter in transit vehicles
    :type in_transit: str
    :param include_non_vin_listings: To include non vin listings. Default is false
    :type include_non_vin_listings: bool
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param photo_links: A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them
    :type photo_links: bool
    :param photo_links_cached: A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them
    :type photo_links_cached: bool
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param write_off_category: write off category
    :type write_off_category: str
    :param exclude_write_off_category: To exclude write off category
    :type exclude_write_off_category: str
    :param fca_status: To filter on fca status
    :type fca_status: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param vrm: To filter on vrm
    :type vrm: str
    :param powertrain_type: To filter on powertrain_type
    :type powertrain_type: str
    :param client_filters: Flag to add explicit filters set on client level in solr
    :type client_filters: bool
    :param boost: Flag to sort listings based on client filter score in solr
    :type boost: bool
    :param car_location_seller_name: Filter cars on seller name
    :type car_location_seller_name: str
    :param car_location_street: Filter cars on street name
    :type car_location_street: str
    :param car_location_city: Filter cars on city
    :type car_location_city: str
    :param car_location_county: Filter cars on county
    :type car_location_county: str
    :param car_location_zip: To filter listing on car ZIP around which they are listed
    :type car_location_zip: str
    :param car_location_latitude: Latitude component of car location
    :type car_location_latitude: float
    :param car_location_longitude: Longitude component of car location
    :type car_location_longitude: float
    :param price_change: Query to filter listings based on their positive and negative price change
    :type price_change: str
    :param price_change_range: Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
    :type price_change_range: str
    :param active_inventory_date_range: date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type active_inventory_date_range: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_size_range: Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    :type engine_size_range: str
    :param uvc_id: To filter on uvc id
    :type uvc_id: str
    :param highway_mpg_range: Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type highway_mpg_range: str
    :param city_mpg_range: City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type city_mpg_range: str
    :param combined_mpg_range: Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type combined_mpg_range: str
    :param owned: Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    :type owned: bool
    :param min_photo_links: Filter listings based by number of photo links within given range
    :type min_photo_links: str
    :param min_photo_links_cached: Filter listings based by number of cached photo links within given range
    :type min_photo_links_cached: str
    :param match: Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    :type match: str
    :param ulez_compliant: Filter listings based on drive into ultra low emmition zone
    :type ulez_compliant: bool

    """
    return web.Response(status=200)


async def search_car_active_get(request: web.Request, api_key=None, append_api_key=None, latitude=None, longitude=None, radius=None, zip=None, include_lease=None, include_finance=None, lease_term=None, lease_down_payment=None, lease_emp=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None, car_type=None, carfax_1_owner=None, carfax_clean_title=None, year_range=None, year=None, make=None, model=None, trim=None, vin=None, body_type=None, body_subtype=None, vehicle_type=None, vins=None, taxonomy_vins=None, mm=None, ymm=None, ymmt=None, match=None, cylinders=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, base_exterior_color=None, base_interior_color=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, highway_mpg_range=None, city_mpg_range=None, miles_range=None, price_range=None, msrp_range=None, dom_range=None, sort_by=None, sort_order=None, rows=None, start=None, include_non_vin_listings=None, msa_code=None, facets=None, range_facets=None, facet_sort=None, stats=None, country=None, plot=None, nodedup=None, dedup=None, owned=None, source=None, state=None, city=None, trim_o=None, trim_r=None, dom_active_range=None, dom_180_range=None, exclude_certified=None, fuel_type=None, dealer_type=None, photo_links=None, photo_links_cached=None, stock_no=None, last_seen_range=None, first_seen_range=None, first_seen_at_source_range=None, first_seen_at_mc_range=None, last_seen_days=None, first_seen_days=None, first_seen_at_source_days=None, first_seen_at_mc_days=None, include_relevant_links=None, inventory_count_range=None, dealer_id=None, exclude_dealer_ids=None, exclude_sources=None, in_transit=None, seating_capacity=None, powertrain_type=None, price_change=None, price_change_range=None, active_inventory_date_range=None, engine_size_range=None, high_value_features=None, min_photo_links=None, min_photo_links_cached=None, client_filters=None) -> web.Response:
    """Gets active car listings for the given search criteria

    This endpoint is the meat of the API and serves many purposes. This API produces a list of currently active cars from the market for the given search criteria. The API results are limited to allow pagination upto 10000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param include_lease: Boolean param to search for listings that include leasing options in them
    :type include_lease: bool
    :param include_finance: Boolean param to search for listings that include finance options in them
    :type include_finance: bool
    :param lease_term: Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60
    :type lease_term: str
    :param lease_down_payment: Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60
    :type lease_down_payment: str
    :param lease_emp: Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60
    :type lease_emp: str
    :param finance_loan_term: Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60
    :type finance_loan_term: str
    :param finance_loan_apr: Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60
    :type finance_loan_apr: str
    :param finance_emp: Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60
    :type finance_emp: str
    :param finance_down_payment: Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60
    :type finance_down_payment: str
    :param finance_down_payment_per: Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60
    :type finance_down_payment_per: str
    :param car_type: Car type. Allowed values are - new / used / certified
    :type car_type: str
    :param carfax_1_owner: Indicates whether car has had only one owner or not
    :type carfax_1_owner: str
    :param carfax_clean_title: Indicates whether car has clean ownership records
    :type carfax_clean_title: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
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
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param vins: Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    :type vins: str
    :param taxonomy_vins: Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    :type taxonomy_vins: str
    :param mm: Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
    :type mm: str
    :param ymm: Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
    :type ymm: str
    :param ymmt: Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations.
    :type ymmt: str
    :param match: Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    :type match: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_aspiration: Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    :type engine_aspiration: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param highway_mpg_range: Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type highway_mpg_range: str
    :param city_mpg_range: City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type city_mpg_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param dom_range: Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_range: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param include_non_vin_listings: To include non vin listings. Default is false
    :type include_non_vin_listings: bool
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str
    :param facet_sort: Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    :type facet_sort: str
    :param stats: The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    :type stats: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param plot: If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    :type plot: bool
    :param nodedup: If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    :type nodedup: bool
    :param dedup: If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    :type dedup: bool
    :param owned: Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    :type owned: bool
    :param source: To filter listing on their source only for widget requests
    :type source: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param trim_o: Filter listings on web scraped trim
    :type trim_o: str
    :param trim_r: Filter trim on custom possible matches
    :type trim_r: str
    :param dom_active_range: Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_active_range: str
    :param dom_180_range: Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_180_range: str
    :param exclude_certified: Boolean param to exclude certified cars from search results
    :type exclude_certified: bool
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param photo_links: A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them
    :type photo_links: bool
    :param photo_links_cached: A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them
    :type photo_links_cached: bool
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
    :param first_seen_at_source_range: First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_source_range: str
    :param first_seen_at_mc_range: First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_mc_range: str
    :param last_seen_days: Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type last_seen_days: str
    :param first_seen_days: First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_days: str
    :param first_seen_at_source_days: First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_source_days: str
    :param first_seen_at_mc_days: First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_mc_days: str
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool
    :param inventory_count_range: Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    :type inventory_count_range: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param exclude_dealer_ids: A list of dealer ids to exclude from result
    :type exclude_dealer_ids: str
    :param exclude_sources: A list of sources to exclude from result
    :type exclude_sources: str
    :param in_transit: A boolean to filter in transit vehicles
    :type in_transit: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param powertrain_type: To filter on powertrain_type
    :type powertrain_type: str
    :param price_change: Query to filter listings based on their positive and negative price change
    :type price_change: str
    :param price_change_range: Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
    :type price_change_range: str
    :param active_inventory_date_range: date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type active_inventory_date_range: str
    :param engine_size_range: Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    :type engine_size_range: str
    :param high_value_features: To filter listings on their high_value_features. Results will be intersection of provided HVFs
    :type high_value_features: str
    :param min_photo_links: Filter listings based by number of photo links within given range
    :type min_photo_links: str
    :param min_photo_links_cached: Filter listings based by number of cached photo links within given range
    :type min_photo_links_cached: str
    :param client_filters: Flag to add explicit filters set on client level in solr
    :type client_filters: bool

    """
    return web.Response(status=200)


async def search_car_auction_active_get(request: web.Request, api_key=None, append_api_key=None, latitude=None, longitude=None, radius=None, zip=None, include_lease=None, include_finance=None, lease_term=None, lease_down_payment=None, lease_emp=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None, car_type=None, carfax_1_owner=None, carfax_clean_title=None, year_range=None, year=None, make=None, model=None, trim=None, vin=None, body_type=None, body_subtype=None, vehicle_type=None, vins=None, taxonomy_vins=None, mm=None, ymm=None, ymmt=None, match=None, cylinders=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, base_exterior_color=None, base_interior_color=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, highway_mpg_range=None, city_mpg_range=None, miles_range=None, price_range=None, msrp_range=None, dom_range=None, sort_by=None, sort_order=None, rows=None, start=None, include_non_vin_listings=None, msa_code=None, facets=None, range_facets=None, facet_sort=None, stats=None, country=None, plot=None, nodedup=None, dedup=None, owned=None, state=None, city=None, source=None, dealer_id=None, trim_o=None, trim_r=None, dom_active_range=None, dom_180_range=None, exclude_certified=None, fuel_type=None, dealer_type=None, photo_links=None, photo_links_cached=None, stock_no=None, last_seen_range=None, first_seen_range=None, first_seen_at_source_range=None, first_seen_at_mc_range=None, last_seen_days=None, first_seen_days=None, first_seen_at_source_days=None, first_seen_at_mc_days=None, include_relevant_links=None, inventory_count_range=None, exclude_dealer_ids=None, exclude_sources=None, in_transit=None, title_type=None, seating_capacity=None, engine_size_range=None, min_photo_links=None, min_photo_links_cached=None) -> web.Response:
    """Gets active auction car listings for the given search criteria

    This API produces a list of currently active auction cars from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param include_lease: Boolean param to search for listings that include leasing options in them
    :type include_lease: bool
    :param include_finance: Boolean param to search for listings that include finance options in them
    :type include_finance: bool
    :param lease_term: Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60
    :type lease_term: str
    :param lease_down_payment: Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60
    :type lease_down_payment: str
    :param lease_emp: Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60
    :type lease_emp: str
    :param finance_loan_term: Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60
    :type finance_loan_term: str
    :param finance_loan_apr: Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60
    :type finance_loan_apr: str
    :param finance_emp: Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60
    :type finance_emp: str
    :param finance_down_payment: Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60
    :type finance_down_payment: str
    :param finance_down_payment_per: Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60
    :type finance_down_payment_per: str
    :param car_type: Car type. Allowed values are - new / used / certified
    :type car_type: str
    :param carfax_1_owner: Indicates whether car has had only one owner or not
    :type carfax_1_owner: str
    :param carfax_clean_title: Indicates whether car has clean ownership records
    :type carfax_clean_title: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
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
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param vins: Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    :type vins: str
    :param taxonomy_vins: Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    :type taxonomy_vins: str
    :param mm: Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
    :type mm: str
    :param ymm: Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
    :type ymm: str
    :param ymmt: Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations.
    :type ymmt: str
    :param match: Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    :type match: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_aspiration: Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    :type engine_aspiration: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param highway_mpg_range: Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type highway_mpg_range: str
    :param city_mpg_range: City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type city_mpg_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param dom_range: Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_range: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param include_non_vin_listings: To include non vin listings. Default is false
    :type include_non_vin_listings: bool
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str
    :param facet_sort: Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    :type facet_sort: str
    :param stats: The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    :type stats: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param plot: If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    :type plot: bool
    :param nodedup: If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    :type nodedup: bool
    :param dedup: If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    :type dedup: bool
    :param owned: Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    :type owned: bool
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param source: To filter listing on their source only for widget requests
    :type source: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param trim_o: Filter listings on web scraped trim
    :type trim_o: str
    :param trim_r: Filter trim on custom possible matches
    :type trim_r: str
    :param dom_active_range: Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_active_range: str
    :param dom_180_range: Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_180_range: str
    :param exclude_certified: Boolean param to exclude certified cars from search results
    :type exclude_certified: bool
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param photo_links: A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them
    :type photo_links: bool
    :param photo_links_cached: A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them
    :type photo_links_cached: bool
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
    :param first_seen_at_source_range: First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_source_range: str
    :param first_seen_at_mc_range: First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_mc_range: str
    :param last_seen_days: Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type last_seen_days: str
    :param first_seen_days: First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_days: str
    :param first_seen_at_source_days: First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_source_days: str
    :param first_seen_at_mc_days: First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_mc_days: str
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool
    :param inventory_count_range: Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    :type inventory_count_range: str
    :param exclude_dealer_ids: A list of dealer ids to exclude from result
    :type exclude_dealer_ids: str
    :param exclude_sources: A list of sources to exclude from result
    :type exclude_sources: str
    :param in_transit: A boolean to filter in transit vehicles
    :type in_transit: str
    :param title_type: To filter on title type
    :type title_type: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param engine_size_range: Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    :type engine_size_range: str
    :param min_photo_links: Filter listings based by number of photo links within given range
    :type min_photo_links: str
    :param min_photo_links_cached: Filter listings based by number of cached photo links within given range
    :type min_photo_links_cached: str

    """
    return web.Response(status=200)


async def search_car_fsbo_active_get(request: web.Request, api_key=None, append_api_key=None, latitude=None, longitude=None, radius=None, zip=None, include_lease=None, include_finance=None, lease_term=None, lease_down_payment=None, lease_emp=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None, car_type=None, carfax_1_owner=None, carfax_clean_title=None, year_range=None, year=None, make=None, model=None, trim=None, vin=None, body_type=None, body_subtype=None, vehicle_type=None, vins=None, taxonomy_vins=None, mm=None, ymm=None, ymmt=None, match=None, cylinders=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, base_exterior_color=None, base_interior_color=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, highway_mpg_range=None, city_mpg_range=None, miles_range=None, price_range=None, msrp_range=None, dom_range=None, sort_by=None, sort_order=None, rows=None, start=None, include_non_vin_listings=None, msa_code=None, facets=None, range_facets=None, facet_sort=None, stats=None, country=None, plot=None, nodedup=None, dedup=None, owned=None, state=None, city=None, source=None, dealer_id=None, trim_o=None, trim_r=None, dom_active_range=None, dom_180_range=None, exclude_certified=None, fuel_type=None, dealer_type=None, photo_links=None, photo_links_cached=None, stock_no=None, last_seen_range=None, first_seen_range=None, first_seen_at_source_range=None, first_seen_at_mc_range=None, last_seen_days=None, first_seen_days=None, first_seen_at_source_days=None, first_seen_at_mc_days=None, include_relevant_links=None, inventory_count_range=None, exclude_dealer_ids=None, exclude_sources=None, exclude_dealer_listings=None, in_transit=None, seating_capacity=None, engine_size_range=None, min_photo_links=None, min_photo_links_cached=None) -> web.Response:
    """Gets active private party car listings for the given search criteria

    This API produces a list of currently active FSBO cars from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param include_lease: Boolean param to search for listings that include leasing options in them
    :type include_lease: bool
    :param include_finance: Boolean param to search for listings that include finance options in them
    :type include_finance: bool
    :param lease_term: Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60
    :type lease_term: str
    :param lease_down_payment: Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60
    :type lease_down_payment: str
    :param lease_emp: Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60
    :type lease_emp: str
    :param finance_loan_term: Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60
    :type finance_loan_term: str
    :param finance_loan_apr: Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60
    :type finance_loan_apr: str
    :param finance_emp: Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60
    :type finance_emp: str
    :param finance_down_payment: Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60
    :type finance_down_payment: str
    :param finance_down_payment_per: Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60
    :type finance_down_payment_per: str
    :param car_type: Car type. Allowed values are - new / used / certified
    :type car_type: str
    :param carfax_1_owner: Indicates whether car has had only one owner or not
    :type carfax_1_owner: str
    :param carfax_clean_title: Indicates whether car has clean ownership records
    :type carfax_clean_title: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
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
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param vins: Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    :type vins: str
    :param taxonomy_vins: Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    :type taxonomy_vins: str
    :param mm: Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
    :type mm: str
    :param ymm: Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
    :type ymm: str
    :param ymmt: Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations.
    :type ymmt: str
    :param match: Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    :type match: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_aspiration: Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    :type engine_aspiration: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param highway_mpg_range: Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type highway_mpg_range: str
    :param city_mpg_range: City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type city_mpg_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param dom_range: Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_range: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param include_non_vin_listings: To include non vin listings. Default is false
    :type include_non_vin_listings: bool
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str
    :param facet_sort: Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    :type facet_sort: str
    :param stats: The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    :type stats: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param plot: If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    :type plot: bool
    :param nodedup: If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    :type nodedup: bool
    :param dedup: If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    :type dedup: bool
    :param owned: Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    :type owned: bool
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param source: To filter listing on their source only for widget requests
    :type source: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param trim_o: Filter listings on web scraped trim
    :type trim_o: str
    :param trim_r: Filter trim on custom possible matches
    :type trim_r: str
    :param dom_active_range: Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_active_range: str
    :param dom_180_range: Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_180_range: str
    :param exclude_certified: Boolean param to exclude certified cars from search results
    :type exclude_certified: bool
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param photo_links: A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them
    :type photo_links: bool
    :param photo_links_cached: A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them
    :type photo_links_cached: bool
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
    :param first_seen_at_source_range: First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_source_range: str
    :param first_seen_at_mc_range: First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_mc_range: str
    :param last_seen_days: Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type last_seen_days: str
    :param first_seen_days: First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_days: str
    :param first_seen_at_source_days: First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_source_days: str
    :param first_seen_at_mc_days: First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_mc_days: str
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool
    :param inventory_count_range: Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    :type inventory_count_range: str
    :param exclude_dealer_ids: A list of dealer ids to exclude from result
    :type exclude_dealer_ids: str
    :param exclude_sources: A list of sources to exclude from result
    :type exclude_sources: str
    :param exclude_dealer_listings: A list of fsbo listings to exclude from result
    :type exclude_dealer_listings: bool
    :param in_transit: A boolean to filter in transit vehicles
    :type in_transit: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param engine_size_range: Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    :type engine_size_range: str
    :param min_photo_links: Filter listings based by number of photo links within given range
    :type min_photo_links: str
    :param min_photo_links_cached: Filter listings based by number of cached photo links within given range
    :type min_photo_links_cached: str

    """
    return web.Response(status=200)


async def search_car_recents_get(request: web.Request, api_key=None, append_api_key=None, latitude=None, longitude=None, radius=None, zip=None, include_lease=None, include_finance=None, lease_term=None, lease_down_payment=None, lease_emp=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None, car_type=None, carfax_1_owner=None, carfax_clean_title=None, year_range=None, year=None, make=None, model=None, trim=None, dealer_id=None, vin=None, source=None, body_type=None, body_subtype=None, vehicle_type=None, vins=None, taxonomy_vins=None, ymmt=None, match=None, cylinders=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, base_exterior_color=None, base_interior_color=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, highway_mpg_range=None, city_mpg_range=None, miles_range=None, price_range=None, msrp_range=None, dom_range=None, last_seen_range=None, first_seen_range=None, first_seen_at_source_range=None, first_seen_at_mc_range=None, last_seen_days=None, first_seen_days=None, first_seen_at_source_days=None, first_seen_at_mc_days=None, sort_by=None, sort_order=None, rows=None, start=None, include_non_vin_listings=None, facets=None, range_facets=None, facet_sort=None, stats=None, country=None, plot=None, nodedup=None, dedup=None, owned=None, state=None, city=None, msa_code=None, dealer_name=None, dealership_group_name=None, trim_o=None, trim_r=None, dom_active_range=None, dom_180_range=None, exclude_certified=None, fuel_type=None, dealer_type=None, photo_links=None, photo_links_cached=None, stock_no=None, sold=None, include_relevant_links=None, expired=None, exclude_dealer_ids=None, exclude_sources=None, in_transit=None, seating_capacity=None, active_inventory_date_range=None, engine_size_range=None, price_change_range=None) -> web.Response:
    """Gets Recent car listings for the given search criteria

    This API produces a list of recently active (past 90 days) cars from the market for the given search criteria

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param include_lease: Boolean param to search for listings that include leasing options in them
    :type include_lease: bool
    :param include_finance: Boolean param to search for listings that include finance options in them
    :type include_finance: bool
    :param lease_term: Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60
    :type lease_term: str
    :param lease_down_payment: Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60
    :type lease_down_payment: str
    :param lease_emp: Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60
    :type lease_emp: str
    :param finance_loan_term: Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60
    :type finance_loan_term: str
    :param finance_loan_apr: Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60
    :type finance_loan_apr: str
    :param finance_emp: Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60
    :type finance_emp: str
    :param finance_down_payment: Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60
    :type finance_down_payment: str
    :param finance_down_payment_per: Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60
    :type finance_down_payment_per: str
    :param car_type: Car type. Allowed values are - new / used / certified
    :type car_type: str
    :param carfax_1_owner: Indicates whether car has had only one owner or not
    :type carfax_1_owner: str
    :param carfax_clean_title: Indicates whether car has clean ownership records
    :type carfax_clean_title: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param vin: To filter listing on their VIN
    :type vin: str
    :param source: To filter listing on their source
    :type source: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param vins: Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    :type vins: str
    :param taxonomy_vins: Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    :type taxonomy_vins: str
    :param ymmt: Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations.
    :type ymmt: str
    :param match: Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    :type match: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_aspiration: Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    :type engine_aspiration: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param highway_mpg_range: Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type highway_mpg_range: str
    :param city_mpg_range: City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type city_mpg_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param dom_range: Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_range: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
    :param first_seen_at_source_range: First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_source_range: str
    :param first_seen_at_mc_range: First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_mc_range: str
    :param last_seen_days: Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type last_seen_days: str
    :param first_seen_days: First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_days: str
    :param first_seen_at_source_days: First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_source_days: str
    :param first_seen_at_mc_days: First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_mc_days: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param include_non_vin_listings: To include non vin listings. Default is false
    :type include_non_vin_listings: bool
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str
    :param facet_sort: Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    :type facet_sort: str
    :param stats: The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    :type stats: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param plot: If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    :type plot: bool
    :param nodedup: If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    :type nodedup: bool
    :param dedup: If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    :type dedup: bool
    :param owned: Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    :type owned: bool
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param dealer_name: Filter listings on dealer_name
    :type dealer_name: str
    :param dealership_group_name: Name of the dealership group to search for
    :type dealership_group_name: str
    :param trim_o: Filter listings on web scraped trim
    :type trim_o: str
    :param trim_r: Filter trim on custom possible matches
    :type trim_r: str
    :param dom_active_range: Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_active_range: str
    :param dom_180_range: Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_180_range: str
    :param exclude_certified: Boolean param to exclude certified cars from search results
    :type exclude_certified: bool
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param photo_links: A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them
    :type photo_links: bool
    :param photo_links_cached: A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them
    :type photo_links_cached: bool
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param sold: sold parameter to fetch only sold listings
    :type sold: bool
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool
    :param expired: Boolean falg to either fetch only the expired listings or active ones
    :type expired: str
    :param exclude_dealer_ids: A list of dealer ids to exclude from result
    :type exclude_dealer_ids: str
    :param exclude_sources: A list of sources to exclude from result
    :type exclude_sources: str
    :param in_transit: A boolean to filter in transit vehicles
    :type in_transit: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param active_inventory_date_range: date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type active_inventory_date_range: str
    :param engine_size_range: Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    :type engine_size_range: str
    :param price_change_range: Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
    :type price_change_range: str

    """
    return web.Response(status=200)


async def search_car_uk_recents_get(request: web.Request, api_key=None, append_api_key=None, latitude=None, longitude=None, radius=None, zip=None, include_lease=None, include_finance=None, lease_term=None, lease_down_payment=None, lease_emp=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None, car_type=None, carfax_1_owner=None, carfax_clean_title=None, year_range=None, year=None, make=None, model=None, trim=None, dealer_id=None, source=None, body_type=None, body_subtype=None, vehicle_type=None, ymmt=None, match=None, cylinders=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, base_exterior_color=None, base_interior_color=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, highway_mpg_range=None, city_mpg_range=None, combined_mpg_range=None, miles_range=None, price_range=None, msrp_range=None, dom_range=None, last_seen_range=None, first_seen_range=None, first_seen_at_source_range=None, first_seen_at_mc_range=None, last_seen_days=None, first_seen_days=None, first_seen_at_source_days=None, first_seen_at_mc_days=None, sort_by=None, sort_order=None, rows=None, start=None, include_non_vin_listings=None, facets=None, range_facets=None, facet_sort=None, stats=None, country=None, plot=None, nodedup=None, dedup=None, owned=None, state=None, city=None, msa_code=None, dealer_name=None, dealership_group_name=None, trim_o=None, trim_r=None, dom_active_range=None, dom_180_range=None, exclude_certified=None, fuel_type=None, dealer_type=None, photo_links=None, photo_links_cached=None, stock_no=None, sold=None, include_relevant_links=None, expired=None, exclude_dealer_ids=None, exclude_sources=None, in_transit=None, seating_capacity=None, insurance_group=None, vrm=None, num_owners=None, variant=None, postal_code=None, write_off_category=None, fca_status=None, active_inventory_date_range=None, engine_size_range=None, price_change_range=None) -> web.Response:
    """Gets Recent UK car listings for the given search criteria

    This API produces a list of recently active (past 90 days) cars from the market for the given search criteria

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param include_lease: Boolean param to search for listings that include leasing options in them
    :type include_lease: bool
    :param include_finance: Boolean param to search for listings that include finance options in them
    :type include_finance: bool
    :param lease_term: Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60
    :type lease_term: str
    :param lease_down_payment: Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60
    :type lease_down_payment: str
    :param lease_emp: Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60
    :type lease_emp: str
    :param finance_loan_term: Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60
    :type finance_loan_term: str
    :param finance_loan_apr: Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60
    :type finance_loan_apr: str
    :param finance_emp: Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60
    :type finance_emp: str
    :param finance_down_payment: Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60
    :type finance_down_payment: str
    :param finance_down_payment_per: Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60
    :type finance_down_payment_per: str
    :param car_type: Car type. Allowed values are - new / used / certified
    :type car_type: str
    :param carfax_1_owner: Indicates whether car has had only one owner or not
    :type carfax_1_owner: str
    :param carfax_clean_title: Indicates whether car has clean ownership records
    :type carfax_clean_title: str
    :param year_range: Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    :type year_range: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param source: To filter listing on their source
    :type source: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param ymmt: Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations.
    :type ymmt: str
    :param match: Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    :type match: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_aspiration: Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    :type engine_aspiration: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param highway_mpg_range: Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type highway_mpg_range: str
    :param city_mpg_range: City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type city_mpg_range: str
    :param combined_mpg_range: Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type combined_mpg_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param dom_range: Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_range: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
    :param first_seen_at_source_range: First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_source_range: str
    :param first_seen_at_mc_range: First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_at_mc_range: str
    :param last_seen_days: Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type last_seen_days: str
    :param first_seen_days: First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_days: str
    :param first_seen_at_source_days: First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_source_days: str
    :param first_seen_at_mc_days: First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    :type first_seen_at_mc_days: str
    :param sort_by: Sort by field. Default sort field is distance from the given point
    :type sort_by: str
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str
    :param rows: Number of results to return. Default is 10. Max is 50
    :type rows: int
    :param start: Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    :type start: int
    :param include_non_vin_listings: To include non vin listings. Default is false
    :type include_non_vin_listings: bool
    :param facets: The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    :type facets: str
    :param range_facets: The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    :type range_facets: str
    :param facet_sort: Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    :type facet_sort: str
    :param stats: The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    :type stats: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param plot: If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    :type plot: bool
    :param nodedup: If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    :type nodedup: bool
    :param dedup: If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    :type dedup: bool
    :param owned: Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    :type owned: bool
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param dealer_name: Filter listings on dealer_name
    :type dealer_name: str
    :param dealership_group_name: Name of the dealership group to search for
    :type dealership_group_name: str
    :param trim_o: Filter listings on web scraped trim
    :type trim_o: str
    :param trim_r: Filter trim on custom possible matches
    :type trim_r: str
    :param dom_active_range: Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_active_range: str
    :param dom_180_range: Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_180_range: str
    :param exclude_certified: Boolean param to exclude certified cars from search results
    :type exclude_certified: bool
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param photo_links: A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them
    :type photo_links: bool
    :param photo_links_cached: A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them
    :type photo_links_cached: bool
    :param stock_no: To filter listing on their stock number on lot
    :type stock_no: str
    :param sold: sold parameter to fetch only sold listings
    :type sold: bool
    :param include_relevant_links: To include_relevant_links. Default is true
    :type include_relevant_links: bool
    :param expired: Boolean falg to either fetch only the expired listings or active ones
    :type expired: str
    :param exclude_dealer_ids: A list of dealer ids to exclude from result
    :type exclude_dealer_ids: str
    :param exclude_sources: A list of sources to exclude from result
    :type exclude_sources: str
    :param in_transit: A boolean to filter in transit vehicles
    :type in_transit: str
    :param seating_capacity: To filter on vehicle seating capacity
    :type seating_capacity: str
    :param insurance_group: Insurance Group
    :type insurance_group: str
    :param vrm: To filter on vrm
    :type vrm: str
    :param num_owners: Number of owners. Range to be given in the format - min-max e.g. 1000-5000
    :type num_owners: str
    :param variant: To filter listing on their variant
    :type variant: str
    :param postal_code: To filter listing on postal code around which they are listed
    :type postal_code: str
    :param write_off_category: write off category
    :type write_off_category: str
    :param fca_status: To filter on fca status
    :type fca_status: str
    :param active_inventory_date_range: date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type active_inventory_date_range: str
    :param engine_size_range: Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    :type engine_size_range: str
    :param price_change_range: Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
    :type price_change_range: str

    """
    return web.Response(status=200)
