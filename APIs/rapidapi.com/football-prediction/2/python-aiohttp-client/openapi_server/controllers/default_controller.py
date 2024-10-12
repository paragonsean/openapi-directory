from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2_list_federations_get200_response import ApiV2ListFederationsGet200Response
from openapi_server.models.api_v2_list_federations_get404_response import ApiV2ListFederationsGet404Response
from openapi_server.models.api_v2_list_markets_get200_response import ApiV2ListMarketsGet200Response
from openapi_server.models.api_v2_performance_stats_get200_response import ApiV2PerformanceStatsGet200Response
from openapi_server.models.api_v2_predictions_id_get200_response import ApiV2PredictionsIdGet200Response
from openapi_server import util


async def api_v2_list_federations_get(request: web.Request, x_rapid_api_key=None) -> web.Response:
    """api_v2_list_federations_get

    Returns an array of all the available federations.

    :param x_rapid_api_key: Your key obtained from https://boggio-analytics.com/fp-api/
    :type x_rapid_api_key: str
    :type x_rapid_api_key: str

    """
    return web.Response(status=200)


async def api_v2_list_markets_get(request: web.Request, x_rapid_api_key=None) -> web.Response:
    """api_v2_list_markets_get

    Returns an array of all the supported prediction markets

    :param x_rapid_api_key: Your key obtained from https://boggio-analytics.com/fp-api/
    :type x_rapid_api_key: str
    :type x_rapid_api_key: str

    """
    return web.Response(status=200)


async def api_v2_performance_stats_get(request: web.Request, x_rapid_api_key=None) -> web.Response:
    """api_v2_performance_stats_get

    Returns predictions accuracy in the last 1, 7, 14, 30 days.

    :param x_rapid_api_key: Your key obtained from https://boggio-analytics.com/fp-api/
    :type x_rapid_api_key: str
    :type x_rapid_api_key: str

    """
    return web.Response(status=200)


async def api_v2_predictions_get(request: web.Request, x_rapid_api_key=None) -> web.Response:
    """api_v2_predictions_get

    This endpoint returns by default the next non-expired football predictions. URL parameters can be specified to show specific date in the past or future or to filter by federation and prediction market name.

    :param x_rapid_api_key: Your key obtained from https://boggio-analytics.com/fp-api/
    :type x_rapid_api_key: str
    :type x_rapid_api_key: str

    """
    return web.Response(status=200)


async def api_v2_predictions_id_get(request: web.Request, id) -> web.Response:
    """api_v2_predictions_id_get

    Returns all predictions available for a match id.

    :param id: ID of match
    :type id: int

    """
    return web.Response(status=200)
