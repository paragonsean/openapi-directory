# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_cloud_accounts_accountid_closeall_post(client):
    """Test case for cloud_accounts_accountid_closeall_post

    Close all positions by account
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cloud/accounts/{accountid}/closeall'.format(accountid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_accounts_accountid_get(client):
    """Test case for cloud_accounts_accountid_get

    Get trading account by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/accounts/{accountid}'.format(accountid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_accounts_accountid_orders_get(client):
    """Test case for cloud_accounts_accountid_orders_get

    Get orders list by account
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/accounts/{accountid}/orders'.format(accountid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_accounts_accountid_orders_orderid_delete(client):
    """Test case for cloud_accounts_accountid_orders_orderid_delete

    Cancel an order by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/cloud/accounts/{accountid}/orders/{orderid}'.format(accountid=56, orderid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cloud_accounts_accountid_orders_post(client):
    """Test case for cloud_accounts_accountid_orders_post

    Place a new order
    """
    body = openapi_server.CloudAccountsAccountidOrdersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cloud/accounts/{accountid}/orders'.format(accountid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_accounts_accountid_snapshots_get(client):
    """Test case for cloud_accounts_accountid_snapshots_get

    Get account equity and cash snapshots
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/accounts/{accountid}/snapshots'.format(accountid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_accounts_accountid_sync_post(client):
    """Test case for cloud_accounts_accountid_sync_post

    Syhchronize an account with account active strategies
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cloud/accounts/{accountid}/sync'.format(accountid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_accounts_accountid_trades_get(client):
    """Test case for cloud_accounts_accountid_trades_get

    Get trades list by account
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/accounts/{accountid}/trades'.format(accountid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_accounts_get(client):
    """Test case for cloud_accounts_get

    Get trading accounts list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/accounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_commands_commandid_get(client):
    """Test case for cloud_commands_commandid_get

    Get command by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/commands/{commandid}'.format(commandid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_commands_get(client):
    """Test case for cloud_commands_get

    Get commands list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/commands',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connections_connectionid_delete(client):
    """Test case for cloud_connections_connectionid_delete

    Delete connection by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/cloud/connections/{connectionid}'.format(connectionid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connections_connectionid_get(client):
    """Test case for cloud_connections_connectionid_get

    Get connection by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/connections/{connectionid}'.format(connectionid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cloud_connections_connectionid_put(client):
    """Test case for cloud_connections_connectionid_put

    Update existing connection
    """
    body = openapi_server.CloudConnectionsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/cloud/connections/{connectionid}'.format(connectionid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connections_get(client):
    """Test case for cloud_connections_get

    Get connections list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/connections',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cloud_connections_post(client):
    """Test case for cloud_connections_post

    Create a new connection
    """
    body = openapi_server.CloudConnectionsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cloud/connections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connectors_connectorid_get(client):
    """Test case for cloud_connectors_connectorid_get

    Get connector by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/connectors/{connectorid}'.format(connectorid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_connectors_get(client):
    """Test case for cloud_connectors_get

    Get available connectors list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/connectors',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_sessions_get(client):
    """Test case for cloud_sessions_get

    Get sessions list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/sessions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_sessions_sessionid_get(client):
    """Test case for cloud_sessions_sessionid_get

    Get session by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/sessions/{sessionid}'.format(sessionid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_strategies_get(client):
    """Test case for cloud_strategies_get

    Get list of active (executing) strategies
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/strategies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cloud_strategies_start_post(client):
    """Test case for cloud_strategies_start_post

    Start a strategy execution for account
    """
    body = openapi_server.CloudStrategiesStartPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cloud/strategies/start',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_strategies_strategyid_get(client):
    """Test case for cloud_strategies_strategyid_get

    Get active (executing) strategy by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cloud/strategies/{strategyid}'.format(strategyid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloud_strategies_strategyid_stop_post(client):
    """Test case for cloud_strategies_strategyid_stop_post

    Stop a strategy execution by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cloud/strategies/{strategyid}/stop'.format(strategyid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

