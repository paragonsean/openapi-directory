from typing import List, Dict
from aiohttp import web

from openapi_server.models.car_rank_request import CarRankRequest
from openapi_server.models.car_rank_response import CarRankResponse
from openapi_server.models.error import Error
from openapi_server import util


async def rank_car(request: web.Request, body, api_key=None, append_api_key=None) -> web.Response:
    """Compute relative rank for car listings.

    Computer rank for car listings based on inputs provided.Weights for ranking parameters can also be provided.

    :param body: Inputs needed for ranking a group of car listings
    :type body: dict | bytes
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param append_api_key: Flag on whether to include api_key in response API urls (if any)
    :type append_api_key: bool

    """
    body = CarRankRequest.from_dict(body)
    return web.Response(status=200)


async def search_and_rank_car(request: web.Request, body, api_key=None, append_api_key=None, latitude=None, longitude=None, radius=None, zip=None, include_lease=None, include_finance=None, lease_term=None, lease_down_payment=None, lease_emp=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None, car_type=None, carfax_1_owner=None, carfax_clean_title=None, year=None, make=None, model=None, trim=None, vin=None, body_type=None, body_subtype=None, vehicle_type=None, vins=None, taxonomy_vins=None, ymmt=None, match=None, cylinders=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, base_exterior_color=None, base_interior_color=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, highway_mpg_range=None, city_mpg_range=None, miles_range=None, price_range=None, msrp_range=None, dom_range=None, sort_by=None, sort_order=None, rows=None, start=None, include_non_vin_listings=None, msa_code=None, facets=None, range_facets=None, facet_sort=None, stats=None, country=None, plot=None, nodedup=None, dedup=None, owned=None, state=None, city=None, trim_o=None, trim_r=None, dom_active_range=None, dom_180_range=None, exclude_certified=None, fuel_type=None, dealer_type=None, photo_links=None, photo_links_cached=None, stock_no=None, last_seen_range=None, first_seen_range=None, first_seen_at_source_range=None, first_seen_at_mc_range=None, last_seen_days=None, first_seen_days=None, first_seen_at_source_days=None, first_seen_at_mc_days=None, inventory_type=None, page=None) -> web.Response:
    """Compute relative rank for car listings.

    Computer rank for car listings based on inputs provided.Weights for ranking parameters can also be provided.

    :param body: Inputs needed for ranking a group of car listings
    :type body: dict | bytes
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
    :param inventory_type: To filter listing on their condition. Either used or new
    :type inventory_type: str
    :param page: Page number to fetch the results for the given criteria. Default is 1.
    :type page: 

    """
    body = CarRankRequest.from_dict(body)
    return web.Response(status=200)
