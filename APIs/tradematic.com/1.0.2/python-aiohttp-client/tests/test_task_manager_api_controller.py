# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backtest_trade import BacktestTrade
from openapi_server.models.by_months import ByMonths
from openapi_server.models.by_quarters import ByQuarters
from openapi_server.models.by_years import ByYears
from openapi_server.models.contribution import Contribution
from openapi_server.models.drawdown_item import DrawdownItem
from openapi_server.models.equity_item import EquityItem
from openapi_server.models.equity_pct_item import EquityPctItem
from openapi_server.models.equity_pct_sm_item import EquityPctSmItem
from openapi_server.models.error import Error
from openapi_server.models.task import Task
from openapi_server.models.taskmanager_tasks_post202_response import TaskmanagerTasksPost202Response
from openapi_server.models.taskmanager_tasks_post_request import TaskmanagerTasksPostRequest
from openapi_server.models.taskmanager_tasks_taskid_folder_get200_response import TaskmanagerTasksTaskidFolderGet200Response
from openapi_server.models.taskmanager_tasks_taskid_performance_get200_response import TaskmanagerTasksTaskidPerformanceGet200Response
from openapi_server.models.taskmanager_tasks_taskid_result2_get200_response import TaskmanagerTasksTaskidResult2Get200Response
from openapi_server.models.taskmanager_tasks_taskid_result_get200_response import TaskmanagerTasksTaskidResultGet200Response
from openapi_server.models.taskmanager_tasks_taskid_status_get200_response import TaskmanagerTasksTaskidStatusGet200Response


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_get(client):
    """Test case for taskmanager_tasks_get

    Get tasks list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_taskmanager_tasks_post(client):
    """Test case for taskmanager_tasks_post

    Create a new task
    """
    body = openapi_server.TaskmanagerTasksPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/taskmanager/tasks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_bymonths_get(client):
    """Test case for taskmanager_tasks_taskid_bymonths_get

    Get backtest data for equity chart, grouped by months
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/bymonths'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_byquarters_get(client):
    """Test case for taskmanager_tasks_taskid_byquarters_get

    Get backtest data for equity chart, grouped by quarters
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/byquarters'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_byyears_get(client):
    """Test case for taskmanager_tasks_taskid_byyears_get

    Get backtest data for equity chart, grouped by years
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/byyears'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_contribution_get(client):
    """Test case for taskmanager_tasks_taskid_contribution_get

    Get backtest symbol contribution data
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/contribution'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_drawdown_get(client):
    """Test case for taskmanager_tasks_taskid_drawdown_get

    Get data for drawdown chart
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/drawdown'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_equity_get(client):
    """Test case for taskmanager_tasks_taskid_equity_get

    Get data for equity chart
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/equity'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_equitypct_get(client):
    """Test case for taskmanager_tasks_taskid_equitypct_get

    Get data for equity chart (%)
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/equitypct'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_equitypctsm_get(client):
    """Test case for taskmanager_tasks_taskid_equitypctsm_get

    Get spared data for equity chart (%)
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/equitypctsm'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_folder_get(client):
    """Test case for taskmanager_tasks_taskid_folder_get

    Get task result folder name
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/folder'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_get(client):
    """Test case for taskmanager_tasks_taskid_get

    Get task by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_performance_get(client):
    """Test case for taskmanager_tasks_taskid_performance_get

    Get backtest statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/performance'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_result2_get(client):
    """Test case for taskmanager_tasks_taskid_result2_get

    Get task result (version 2)
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/result2'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_result_get(client):
    """Test case for taskmanager_tasks_taskid_result_get

    Get task result
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/result'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_status_get(client):
    """Test case for taskmanager_tasks_taskid_status_get

    Get task status
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/status'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taskmanager_tasks_taskid_trades_get(client):
    """Test case for taskmanager_tasks_taskid_trades_get

    Get backtest trades list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taskmanager/tasks/{taskid}/trades'.format(taskid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

