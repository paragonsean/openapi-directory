from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_bundle_copy_response import ListBundleCopyResponse
from openapi_server.models.numbers_v2_regulatory_compliance_bundle_bundle_copy import NumbersV2RegulatoryComplianceBundleBundleCopy
from openapi_server import util


async def create_bundle_copy(request: web.Request, bundle_sid, friendly_name=None) -> web.Response:
    """create_bundle_copy

    Creates a new copy of a Bundle. It will internally create copies of all the bundle items (identities and documents) of the original bundle

    :param bundle_sid: The unique string that identifies the Bundle to be copied.
    :type bundle_sid: str
    :param friendly_name: The string that you assigned to describe the copied bundle.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def list_bundle_copy(request: web.Request, bundle_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_bundle_copy

    Retrieve a list of all Bundles Copies for a Bundle.

    :param bundle_sid: The unique string that we created to identify the Bundle resource.
    :type bundle_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
