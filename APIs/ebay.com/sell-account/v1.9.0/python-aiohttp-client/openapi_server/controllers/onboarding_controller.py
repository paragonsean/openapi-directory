from typing import List, Dict
from aiohttp import web

from openapi_server.models.payments_program_onboarding_response import PaymentsProgramOnboardingResponse
from openapi_server import util


async def get_payments_program_onboarding(request: web.Request, marketplace_id, payments_program_type) -> web.Response:
    """get_payments_program_onboarding

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is no longer applicable, as all seller accounts globally have been enabled for the new eBay payment and checkout flow.&lt;/span&gt;&lt;br/&gt;&lt;br/&gt;This method retrieves a seller&#39;s onboarding status for a payments program for a specified marketplace. The overall onboarding status of the seller and the status of each onboarding step is returned.

    :param marketplace_id: The eBay marketplace ID associated with the onboarding status to retrieve.
    :type marketplace_id: str
    :param payments_program_type: The type of payments program whose status is returned by the method.
    :type payments_program_type: str

    """
    return web.Response(status=200)
