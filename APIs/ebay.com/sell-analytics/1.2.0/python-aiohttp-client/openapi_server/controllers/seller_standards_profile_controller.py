from typing import List, Dict
from aiohttp import web

from openapi_server.models.find_seller_standards_profiles_response import FindSellerStandardsProfilesResponse
from openapi_server.models.standards_profile import StandardsProfile
from openapi_server import util


async def find_seller_standards_profiles(request: web.Request, ) -> web.Response:
    """find_seller_standards_profiles

    This call retrieves all the standards profiles for the associated seller. A standards profile is a set of eBay seller metrics and the seller&#39;s associated compliance values (either TOP_RATED, ABOVE_STANDARD, or BELOW_STANDARD). A seller&#39;s multiple profiles are distinguished by two criteria, a &amp;quot;program&amp;quot; and a &amp;quot;cycle.&amp;quot; A profile&#39;s program is one of three regions where the seller may have done business, or PROGRAM_GLOBAL to indicate all marketplaces where the seller has done business. The cycle value specifies whether the standards compliance values were determined at the last official eBay evaluation or at the time of the request.


    """
    return web.Response(status=200)


async def get_seller_standards_profile(request: web.Request, cycle, program) -> web.Response:
    """get_seller_standards_profile

    This call retrieves a single standards profile for the associated seller. A standards profile is a set of eBay seller metrics and the seller&#39;s associated compliance values (either TOP_RATED, ABOVE_STANDARD, or BELOW_STANDARD). A seller can have multiple profiles distinguished by two criteria, a &amp;quot;program&amp;quot; and a &amp;quot;cycle.&amp;quot; A profile&#39;s program is one of three regions where the seller may have done business, or PROGRAM_GLOBAL to indicate all marketplaces where the seller has done business. The cycle value specifies whether the standards compliance values were determined at the last official eBay evaluation (CURRENT) or at the time of the request (PROJECTED). Both cycle and a program values are required URI parameters for this method.

    :param cycle: The period covered by the returned standards profile evaluation. Supply one of two values, CURRENT means the response reflects eBay&#39;s most recent monthly standards evaluation and PROJECTED means the response reflect the seller&#39;s projected monthly evaluation, as calculated at the time of the request.
    :type cycle: str
    :param program: This input value specifies the region used to determine the seller&#39;s standards profile. Supply one of the four following values, PROGRAM_DE, PROGRAM_UK, PROGRAM_US, or PROGRAM_GLOBAL.
    :type program: str

    """
    return web.Response(status=200)
