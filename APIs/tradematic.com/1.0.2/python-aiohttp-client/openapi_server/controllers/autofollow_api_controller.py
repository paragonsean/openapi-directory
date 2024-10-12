from typing import List, Dict
from aiohttp import web

from openapi_server.models.autofollow_strategies_post200_response import AutofollowStrategiesPost200Response
from openapi_server.models.autofollow_strategies_post_request import AutofollowStrategiesPostRequest
from openapi_server.models.autofollow_strategies_strategyid_content_put200_response import AutofollowStrategiesStrategyidContentPut200Response
from openapi_server.models.autofollow_strategies_strategyid_content_put_request import AutofollowStrategiesStrategyidContentPutRequest
from openapi_server.models.autofollow_strategies_strategyid_put200_response import AutofollowStrategiesStrategyidPut200Response
from openapi_server.models.autofollow_strategies_strategyid_put_request import AutofollowStrategiesStrategyidPutRequest
from openapi_server.models.autofollow_strategies_strategyid_signals_post200_response import AutofollowStrategiesStrategyidSignalsPost200Response
from openapi_server.models.autofollow_strategies_strategyid_signals_post_request import AutofollowStrategiesStrategyidSignalsPostRequest
from openapi_server.models.error import Error
from openapi_server.models.signal import Signal
from openapi_server.models.strategy import Strategy
from openapi_server.models.strategy_position import StrategyPosition
from openapi_server import util


async def autofollow_strategies_get(request: web.Request, ) -> web.Response:
    """Get autofollow strategies list

    Get autofollow strategies list


    """
    return web.Response(status=200)


async def autofollow_strategies_post(request: web.Request, body) -> web.Response:
    """Create new autofollow strategy

    Create new autofollow strategy

    :param body: 
    :type body: dict | bytes

    """
    body = AutofollowStrategiesPostRequest.from_dict(body)
    return web.Response(status=200)


async def autofollow_strategies_strategyid_content_put(request: web.Request, strategyid, body) -> web.Response:
    """Update rules for strategy that was created with strategy builder

    Update rules for strategy that was created with strategy builder

    :param strategyid: 
    :type strategyid: int
    :param body: 
    :type body: dict | bytes

    """
    body = AutofollowStrategiesStrategyidContentPutRequest.from_dict(body)
    return web.Response(status=200)


async def autofollow_strategies_strategyid_get(request: web.Request, strategyid) -> web.Response:
    """Get autofollow strategy by ID

    Get autofollow strategy by ID

    :param strategyid: 
    :type strategyid: int

    """
    return web.Response(status=200)


async def autofollow_strategies_strategyid_positions_get(request: web.Request, strategyid) -> web.Response:
    """Get positions for strategy

    Get positions for strategy

    :param strategyid: 
    :type strategyid: int

    """
    return web.Response(status=200)


async def autofollow_strategies_strategyid_put(request: web.Request, strategyid, body) -> web.Response:
    """Update autofollow strategy

    Update autofollow strategy

    :param strategyid: 
    :type strategyid: int
    :param body: 
    :type body: dict | bytes

    """
    body = AutofollowStrategiesStrategyidPutRequest.from_dict(body)
    return web.Response(status=200)


async def autofollow_strategies_strategyid_signals_get(request: web.Request, strategyid, count) -> web.Response:
    """Get trading signals for strategy

    Get trading signals for strategy

    :param strategyid: 
    :type strategyid: int
    :param count: 
    :type count: int

    """
    return web.Response(status=200)


async def autofollow_strategies_strategyid_signals_post(request: web.Request, strategyid, body) -> web.Response:
    """Send a new signal for autofollow strategy

    Send a new signal for autofollow strategy

    :param strategyid: 
    :type strategyid: int
    :param body: 
    :type body: dict | bytes

    """
    body = AutofollowStrategiesStrategyidSignalsPostRequest.from_dict(body)
    return web.Response(status=200)
