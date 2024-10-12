from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.search_response import SearchResponse
from openapi_server import util


async def oem_search(request: web.Request, api_key=None, offer_type=None, year=None, make=None, model=None, trim=None, msrp=None, apr=None, monthly=None, monthly_per_thousand=None, down_payment=None, due_at_signing=None, security_deposit=None, disposition_fee=None, acquisition_fee=None, duration=None, dealer_contribution=None, mileage_charge=None, mileage_charge_limit=None, cashback_amount=None, cashback_target_group=None, lease_end_purchase_option=None, net_capitalised_cost=None, gross_capitalised_cost=None, total_monthly_payment=None, zip=None, city=None, state=None, country=None, latitude=None, longitude=None, radius=None, search_text=None, last_seen_range=None, first_seen_range=None, sort_by=None, sort_order=None, rows=None, start=None, facets=None, range_facets=None, facet_sort=None, stats=None) -> web.Response:
    """Gets oem incentive listings for the given search criteria

    This endpoint is the meat of the API and serves many purposes. This API produces a list of currently active oem incentive from the market for the given search criteria. The API results are limited to allow pagination upto 10000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param offer_type: The type of the incentive
    :type offer_type: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param msrp: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp: str
    :param apr: APR range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type apr: str
    :param monthly: To filter listing on Monthly payment amount, usually populated in Lease offers
    :type monthly: str
    :param monthly_per_thousand: To filter listing on monthly amount to be paid by customer for every $1000 financed at the advertised APR rate
    :type monthly_per_thousand: str
    :param down_payment: To filter listing on down payment offer on car
    :type down_payment: str
    :param due_at_signing: To filter listing on total amount due at signing, that usually includes first month payment, down payment, acquisition fee etc
    :type due_at_signing: str
    :param security_deposit: To filter listing on security deposit required for the offer
    :type security_deposit: str
    :param disposition_fee: To filter listing on disposition fee of the car
    :type disposition_fee: str
    :param acquisition_fee: To filter listing on acquisition fee of the car
    :type acquisition_fee: str
    :param duration: To filter listing on offer duration in months
    :type duration: str
    :param dealer_contribution: To filter listing on any contribution from dealer&#39;s side
    :type dealer_contribution: str
    :param mileage_charge: Mileage Charge Range range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 100-1000
    :type mileage_charge: str
    :param mileage_charge_limit: To filter listing on mileage charge limit the offer is valid up to under the default clauses
    :type mileage_charge_limit: str
    :param cashback_amount: To filter listing on cashback amounts listed in offer
    :type cashback_amount: str
    :param cashback_target_group: To filter listing on the demographic or any other entity for whom this cashback offer is for. Not all target groups are identified but the most common ones are tagged like Military, Grad students Current owners etc
    :type cashback_target_group: str
    :param lease_end_purchase_option: To filter listing on amount at the lease end to pay for buying the car
    :type lease_end_purchase_option: str
    :param net_capitalised_cost: To filter listing on net capitalised cost of the car
    :type net_capitalised_cost: str
    :param gross_capitalised_cost: To filter listing on gross capitalised cost of the car
    :type gross_capitalised_cost: str
    :param total_monthly_payment: To filter listing on gross capitalised cost of the car
    :type total_monthly_payment: str
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param search_text: To search a substring across entire document
    :type search_text: str
    :param last_seen_range: Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type last_seen_range: str
    :param first_seen_range: First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    :type first_seen_range: str
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

    """
    return web.Response(status=200)
