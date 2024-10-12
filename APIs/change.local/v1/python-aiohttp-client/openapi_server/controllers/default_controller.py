from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_v1_donations_carbon_calculate_get(request: web.Request, weight_lb, origin_address=None, destination_address=None, distance_mi=None, transportation_method=None) -> web.Response:
    """Calculate shipping carbon offset

    Calculates the donation amount (to CarbonFund 501\\(c\\)3) needed to offset a physical shipment. This calculation depends on the weight, primary transportation method, and distance of the shipment. Provide the distance of the shipment using the origin and destination address, or directly with the number of miles. For convenience, this endpoint also returns the id of the nonprofit CarbonFund, for making a subsequent donation to. See the [Carbon offsets guide](/recipes/carbon-offsets/) for more on using this endpoint.

    :param weight_lb: The total weight (in pounds) of the shipment.
    :type weight_lb: 
    :param origin_address: The origin zip code (US only) of the shipment. If you send this parameter, also send &#x60;destination_address&#x60;.
    :type origin_address: 
    :param destination_address: The destination zip code (US only) of the shipment. If you send this parameter, also send &#x60;origin_address&#x60;.
    :type destination_address: 
    :param distance_mi: The total distance (in miles) of the shipment. You can use this parameter in place of &#x60;origin_address&#x60; and &#x60;destination_address&#x60;.
    :type distance_mi: 
    :param transportation_method: The primary transportation method of the shipment.
    :type transportation_method: str

    """
    return web.Response(status=200)


async def api_v1_donations_carbon_stats_get(request: web.Request, id=None) -> web.Response:
    """Retrieve carbon offset stats

    Measures your carbon offset impact in relatable terms. Provide the id of a donation to CarbonFund to see stats about that specific donation. If you omit the donation id, this endpoint returns aggregate stats for all of your CarbonFund donations.

    :param id: The id of a donation to the CarbonFund nonprofit. Ids are returned when a donation is created. If an ID is not provided, the total stats for all donations to CarbonFund are returned.
    :type id: 

    """
    return web.Response(status=200)


async def api_v1_donations_create_post(request: web.Request, amount, nonprofit_id, funding_source, zip_code=None) -> web.Response:
    """Create a donation

    Creates a donation to any nonprofit. CHANGE keeps track of your donations, bills you at the end of the month, and handles the nonprofit payouts for you.

    :param amount: The amount of the donation in cents.
    :type amount: str
    :param nonprofit_id: The id of a nonprofit from the CHANGE network.
    :type nonprofit_id: str
    :param funding_source: Source of the donation funds. If you are collecting payment from your customer for the donation, use &#x60;customer&#x60;.
    :type funding_source: str
    :param zip_code: The customer&#39;s zip code. Provide this to unlock geographic insights.
    :type zip_code: str

    """
    return web.Response(status=200)


async def api_v1_donations_crypto_calculate_get(request: web.Request, currency, count=None) -> web.Response:
    """Calculate crypto carbon offset

    Calculates the donation amount (to CarbonFund 501\\(c\\)3) needed to offset a cryptocurrency transaction. For convenience, this endpoint also returns the id of the nonprofit CarbonFund, for making a subsequent donation to. See the [Carbon offsets guide](/recipes/carbon-offsets/) for more on using this endpoint.

    :param currency: The currency of the transaction.
    :type currency: str
    :param count: The number of transactions to offset.
    :type count: 

    """
    return web.Response(status=200)


async def api_v1_donations_index_get(request: web.Request, page=None) -> web.Response:
    """List your donations

    Retrieves a list of donations you&#39;ve previously made. The donations are returned in order of creation, with the most recent donations appearing first. This endpoint is paginated.

    :param page: Which page to return. This endpoint is paginated, and returns maximum 30 donations per page.
    :type page: 

    """
    return web.Response(status=200)


async def api_v1_donations_show_get(request: web.Request, id) -> web.Response:
    """Retrieve a donation

    Retrieves the details of a donation you&#39;ve previously made.

    :param id: The id of a donation. Ids are returned when a donation is created.
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_nonprofits_list_get(request: web.Request, name=None, page=None) -> web.Response:
    """Search a nonprofit

    Retrieves a list of nonprofits whose names match the provided name. This endpoint is paginated.

    :param name: A string to search.
    :type name: str
    :param page: The page to return. This endpoint is paginated, and returns up to 30 nonprofits at a time.
    :type page: 

    """
    return web.Response(status=200)


async def api_v1_nonprofits_show_get(request: web.Request, id) -> web.Response:
    """Show a nonprofit

    Retrieves information for a nonprofit.

    :param id: The id of a nonprofit from the CHANGE network.
    :type id: str

    """
    return web.Response(status=200)
