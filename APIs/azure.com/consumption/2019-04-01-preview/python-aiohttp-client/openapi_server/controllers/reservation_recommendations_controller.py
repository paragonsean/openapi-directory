from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.reservation_recommendations_list_result import ReservationRecommendationsListResult
from openapi_server import util


async def reservation_recommendations_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """reservation_recommendations_list

    List of recommendations for purchasing reserved instances.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param filter: May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod.
    :type filter: str

    """
    return web.Response(status=200)
