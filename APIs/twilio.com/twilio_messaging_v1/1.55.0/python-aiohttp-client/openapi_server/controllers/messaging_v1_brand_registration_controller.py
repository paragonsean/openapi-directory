from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_brand_registrations_response import ListBrandRegistrationsResponse
from openapi_server.models.messaging_v1_brand_registrations import MessagingV1BrandRegistrations
from openapi_server import util


async def create_brand_registrations(request: web.Request, a2_p_profile_bundle_sid, customer_profile_bundle_sid, brand_type=None, mock=None, skip_automatic_sec_vet=None) -> web.Response:
    """create_brand_registrations

    

    :param a2_p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
    :type a2_p_profile_bundle_sid: str
    :param customer_profile_bundle_sid: Customer Profile Bundle Sid.
    :type customer_profile_bundle_sid: str
    :param brand_type: Type of brand being created. One of: \\\&quot;STANDARD\\\&quot;, \\\&quot;SOLE_PROPRIETOR\\\&quot;. SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
    :type brand_type: str
    :param mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
    :type mock: bool
    :param skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be done.
    :type skip_automatic_sec_vet: bool

    """
    return web.Response(status=200)


async def fetch_brand_registrations(request: web.Request, sid) -> web.Response:
    """fetch_brand_registrations

    

    :param sid: The SID of the Brand Registration resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_brand_registrations(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_brand_registrations

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_brand_registrations(request: web.Request, sid) -> web.Response:
    """update_brand_registrations

    

    :param sid: The SID of the Brand Registration resource to update.
    :type sid: str

    """
    return web.Response(status=200)
