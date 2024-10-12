from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_onboarding_url_request import GetOnboardingUrlRequest
from openapi_server.models.get_onboarding_url_response import GetOnboardingUrlResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_get_onboarding_url(request: web.Request, body=None) -> web.Response:
    """Get a link to a Adyen-hosted onboarding page

    Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more information on how to use HOP, refer to [Hosted onboarding](https://docs.adyen.com/marketplaces-and-platforms/classic/collect-verification-details/hosted-onboarding-page). 

    :param body: 
    :type body: dict | bytes

    """
    body = GetOnboardingUrlRequest.from_dict(body)
    return web.Response(status=200)
