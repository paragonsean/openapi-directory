from typing import List, Dict
from aiohttp import web

from openapi_server.models.offers_offer_id_changelog_get200_response import OffersOfferIdChangelogGet200Response
from openapi_server import util


async def offers_offer_id_changelog_get(request: web.Request, offer_id) -> web.Response:
    """Get list of changelog history for the offer. Returns offer object with contact and user objects if they are provided

    

    :param offer_id: 
    :type offer_id: str
    :type offer_id: str

    """
    return web.Response(status=200)
