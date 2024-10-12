from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.cloud_accounts_accountid_closeall_post202_response import CloudAccountsAccountidCloseallPost202Response
from openapi_server.models.cloud_accounts_accountid_orders_post_request import CloudAccountsAccountidOrdersPostRequest
from openapi_server.models.cloud_connections_post200_response import CloudConnectionsPost200Response
from openapi_server.models.cloud_connections_post_request import CloudConnectionsPostRequest
from openapi_server.models.cloud_strategies_start_post_request import CloudStrategiesStartPostRequest
from openapi_server.models.cloud_strategy import CloudStrategy
from openapi_server.models.command import Command
from openapi_server.models.connection import Connection
from openapi_server.models.connector import Connector
from openapi_server.models.error import Error
from openapi_server.models.order import Order
from openapi_server.models.session import Session
from openapi_server.models.snapshot import Snapshot
from openapi_server.models.trade import Trade
from openapi_server import util


async def cloud_accounts_accountid_closeall_post(request: web.Request, accountid) -> web.Response:
    """Close all positions by account

    Close all positions by account

    :param accountid: 
    :type accountid: int

    """
    return web.Response(status=200)


async def cloud_accounts_accountid_get(request: web.Request, accountid) -> web.Response:
    """Get trading account by ID

    Get trading account by ID

    :param accountid: 
    :type accountid: int

    """
    return web.Response(status=200)


async def cloud_accounts_accountid_orders_get(request: web.Request, accountid) -> web.Response:
    """Get orders list by account

    Get orders list by account

    :param accountid: 
    :type accountid: int

    """
    return web.Response(status=200)


async def cloud_accounts_accountid_orders_orderid_delete(request: web.Request, accountid, orderid) -> web.Response:
    """Cancel an order by ID

    Cancel an order by ID

    :param accountid: 
    :type accountid: int
    :param orderid: 
    :type orderid: int

    """
    return web.Response(status=200)


async def cloud_accounts_accountid_orders_post(request: web.Request, accountid, body) -> web.Response:
    """Place a new order

    Place a new order

    :param accountid: 
    :type accountid: int
    :param body: 
    :type body: dict | bytes

    """
    body = CloudAccountsAccountidOrdersPostRequest.from_dict(body)
    return web.Response(status=200)


async def cloud_accounts_accountid_snapshots_get(request: web.Request, accountid) -> web.Response:
    """Get account equity and cash snapshots

    Get account equity and cash snapshots

    :param accountid: 
    :type accountid: int

    """
    return web.Response(status=200)


async def cloud_accounts_accountid_sync_post(request: web.Request, accountid) -> web.Response:
    """Syhchronize an account with account active strategies

    Syhchronize an account with account active strategies

    :param accountid: 
    :type accountid: int

    """
    return web.Response(status=200)


async def cloud_accounts_accountid_trades_get(request: web.Request, accountid) -> web.Response:
    """Get trades list by account

    Get trades list by account

    :param accountid: 
    :type accountid: int

    """
    return web.Response(status=200)


async def cloud_accounts_get(request: web.Request, ) -> web.Response:
    """Get trading accounts list

    Get trading accounts list


    """
    return web.Response(status=200)


async def cloud_commands_commandid_get(request: web.Request, commandid) -> web.Response:
    """Get command by ID

    Get command by ID

    :param commandid: 
    :type commandid: int

    """
    return web.Response(status=200)


async def cloud_commands_get(request: web.Request, ) -> web.Response:
    """Get commands list

    Get commands list


    """
    return web.Response(status=200)


async def cloud_connections_connectionid_delete(request: web.Request, connectionid) -> web.Response:
    """Delete connection by ID

    Delete connection by ID

    :param connectionid: 
    :type connectionid: int

    """
    return web.Response(status=200)


async def cloud_connections_connectionid_get(request: web.Request, connectionid) -> web.Response:
    """Get connection by ID

    Get connection by ID

    :param connectionid: 
    :type connectionid: int

    """
    return web.Response(status=200)


async def cloud_connections_connectionid_put(request: web.Request, connectionid, body) -> web.Response:
    """Update existing connection

    Update existing connection

    :param connectionid: 
    :type connectionid: int
    :param body: 
    :type body: dict | bytes

    """
    body = CloudConnectionsPostRequest.from_dict(body)
    return web.Response(status=200)


async def cloud_connections_get(request: web.Request, ) -> web.Response:
    """Get connections list

    Get connections list


    """
    return web.Response(status=200)


async def cloud_connections_post(request: web.Request, body) -> web.Response:
    """Create a new connection

    Create a new connection

    :param body: 
    :type body: dict | bytes

    """
    body = CloudConnectionsPostRequest.from_dict(body)
    return web.Response(status=200)


async def cloud_connectors_connectorid_get(request: web.Request, connectorid) -> web.Response:
    """Get connector by ID

    Get connector by ID

    :param connectorid: 
    :type connectorid: int

    """
    return web.Response(status=200)


async def cloud_connectors_get(request: web.Request, ) -> web.Response:
    """Get available connectors list

    Get available connectors list


    """
    return web.Response(status=200)


async def cloud_sessions_get(request: web.Request, ) -> web.Response:
    """Get sessions list

    Get sessions list


    """
    return web.Response(status=200)


async def cloud_sessions_sessionid_get(request: web.Request, sessionid) -> web.Response:
    """Get session by ID

    Get session by ID

    :param sessionid: 
    :type sessionid: int

    """
    return web.Response(status=200)


async def cloud_strategies_get(request: web.Request, ) -> web.Response:
    """Get list of active (executing) strategies

    Get list of active (executing) strategies


    """
    return web.Response(status=200)


async def cloud_strategies_start_post(request: web.Request, body) -> web.Response:
    """Start a strategy execution for account

    Start a strategy execution for account

    :param body: 
    :type body: dict | bytes

    """
    body = CloudStrategiesStartPostRequest.from_dict(body)
    return web.Response(status=200)


async def cloud_strategies_strategyid_get(request: web.Request, strategyid) -> web.Response:
    """Get active (executing) strategy by ID

    Get active (executing) strategy by ID

    :param strategyid: 
    :type strategyid: int

    """
    return web.Response(status=200)


async def cloud_strategies_strategyid_stop_post(request: web.Request, strategyid) -> web.Response:
    """Stop a strategy execution by ID

    Stop a strategy execution by ID

    :param strategyid: 
    :type strategyid: int

    """
    return web.Response(status=200)
