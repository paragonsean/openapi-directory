from typing import List, Dict
from aiohttp import web

from openapi_server.models.numbers_v2_regulatory_compliance_bundle_replace_items import NumbersV2RegulatoryComplianceBundleReplaceItems
from openapi_server import util


async def create_replace_items(request: web.Request, bundle_sid, from_bundle_sid) -> web.Response:
    """create_replace_items

    Replaces all bundle items in the target bundle (specified in the path) with all the bundle items of the source bundle (specified by the from_bundle_sid body param)

    :param bundle_sid: The unique string that identifies the Bundle where the item assignments are going to be replaced.
    :type bundle_sid: str
    :param from_bundle_sid: The source bundle sid to copy the item assignments from.
    :type from_bundle_sid: str

    """
    return web.Response(status=200)
