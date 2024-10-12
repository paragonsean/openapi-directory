from typing import List, Dict
from aiohttp import web

from openapi_server.models.seller_eligibility_multi_program_response import SellerEligibilityMultiProgramResponse
from openapi_server import util


async def get_advertising_eligibility(request: web.Request, x_ebay_c_marketplace_id, program_types=None) -> web.Response:
    """get_advertising_eligibility

    This method allows developers to check the seller eligibility status for eBay advertising programs.

    :param x_ebay_c_marketplace_id: The unique identifier of the eBay marketplace for which the seller eligibility status shall be checked.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This value is case-sensitive.&lt;/span&gt;
    :type x_ebay_c_marketplace_id: str
    :param program_types: A comma-separated list of eBay advertising programs.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Tip:&lt;/b&gt; See the &lt;a href&#x3D;\&quot;/api-docs/sell/account/types/plser:AdvertisingProgramEnum\&quot;&gt; AdvertisingProgramEnum&lt;/a&gt; type for possible values.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;If no programs are specified, the results will be returned for all programs.
    :type program_types: str

    """
    return web.Response(status=200)
