from typing import List, Dict
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
from openapi_server import util


async def taskmanager_tasks_get(request: web.Request, ) -> web.Response:
    """Get tasks list

    Get tasks list


    """
    return web.Response(status=200)


async def taskmanager_tasks_post(request: web.Request, body) -> web.Response:
    """Create a new task

    Create a new task

    :param body: 
    :type body: dict | bytes

    """
    body = TaskmanagerTasksPostRequest.from_dict(body)
    return web.Response(status=200)


async def taskmanager_tasks_taskid_bymonths_get(request: web.Request, taskid) -> web.Response:
    """Get backtest data for equity chart, grouped by months

    Get backtest data for equity chart, grouped by months

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_byquarters_get(request: web.Request, taskid) -> web.Response:
    """Get backtest data for equity chart, grouped by quarters

    Get backtest data for equity chart, grouped by quarters

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_byyears_get(request: web.Request, taskid) -> web.Response:
    """Get backtest data for equity chart, grouped by years

    Get backtest data for equity chart, grouped by years

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_contribution_get(request: web.Request, taskid) -> web.Response:
    """Get backtest symbol contribution data

    Get backtest symbol contribution data

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_drawdown_get(request: web.Request, taskid) -> web.Response:
    """Get data for drawdown chart

    Get data for drawdown chart

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_equity_get(request: web.Request, taskid) -> web.Response:
    """Get data for equity chart

    Get data for equity chart

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_equitypct_get(request: web.Request, taskid) -> web.Response:
    """Get data for equity chart (%)

    Get data for equity chart (%)

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_equitypctsm_get(request: web.Request, taskid) -> web.Response:
    """Get spared data for equity chart (%)

    Get spared data for equity chart (%)

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_folder_get(request: web.Request, taskid) -> web.Response:
    """Get task result folder name

    Get task result folder name

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_get(request: web.Request, taskid) -> web.Response:
    """Get task by ID

    Get task by ID

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_performance_get(request: web.Request, taskid) -> web.Response:
    """Get backtest statistics

    Get backtest statistics

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_result2_get(request: web.Request, taskid) -> web.Response:
    """Get task result (version 2)

    Get task result (version 2)

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_result_get(request: web.Request, taskid) -> web.Response:
    """Get task result

    Get task result

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_status_get(request: web.Request, taskid) -> web.Response:
    """Get task status

    Get task status

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)


async def taskmanager_tasks_taskid_trades_get(request: web.Request, taskid) -> web.Response:
    """Get backtest trades list

    Get backtest trades list

    :param taskid: 
    :type taskid: int

    """
    return web.Response(status=200)
