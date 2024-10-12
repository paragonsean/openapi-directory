from typing import List, Dict
from aiohttp import web

from openapi_server.models.ai_planning_level_request import AiPlanningLevelRequest
from openapi_server.models.forecast_bottom_up_response import ForecastBottomUpResponse
from openapi_server.models.forecast_response import ForecastResponse
from openapi_server.models.full_details_forecast_response import FullDetailsForecastResponse
from openapi_server.models.history_and_forecast_response import HistoryAndForecastResponse
from openapi_server.models.job_response import JobResponse
from openapi_server.models.optimal_parameter_response import OptimalParameterResponse
from openapi_server.models.outliers_request import OutliersRequest
from openapi_server.models.planning_level_re_run_request import PlanningLevelReRunRequest
from openapi_server.models.planning_level_request import PlanningLevelRequest
from openapi_server.models.time_series_outliers_response import TimeSeriesOutliersResponse
from openapi_server import util


async def forecast_ai_history_and_forecast_post(request: web.Request, token=None, body=None) -> web.Response:
    """History and forecast utilizing advanced machine learning models

    History and forecast utilizing advanced machine learning models. Please be mindful of enhanced execution times (~1-2s per timeseries).

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AiPlanningLevelRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_aipost(request: web.Request, token=None, body=None) -> web.Response:
    """Forecast utilizing advanced machine learning models

    Forecast AI is utilizing advanced machine learning models. Please be mindful of enhanced execution times (~1-2s per timeseries).

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AiPlanningLevelRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_file_to_forecast_post(request: web.Request, file, method, token=None, discard_data=None, error_type=None, hold_out_period=None, no_fcst=None, outlier_detection=None, periodicity=None) -> web.Response:
    """Forecast from file

    Forecast from file allows for quick analysis via Microsoft Excel and CSV file format. Please check documentation link for help.

    :param file: 
    :type file: str
    :param method: 
    :type method: str
    :param token: User Authentication Token
    :type token: str
    :param discard_data: 
    :type discard_data: bool
    :param error_type: 
    :type error_type: str
    :param hold_out_period: 
    :type hold_out_period: int
    :param no_fcst: 
    :type no_fcst: int
    :param outlier_detection: 
    :type outlier_detection: bool
    :param periodicity: 
    :type periodicity: int

    """
    return web.Response(status=200)


async def forecast_forecast_bottom_up_post(request: web.Request, token=None, body=None) -> web.Response:
    """Bottom up forecasting

    Calculate forecast by timeseries and sum results up to establish forecast for top level timeseries.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlanningLevelRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_forecast_top_down_post(request: web.Request, token=None, body=None) -> web.Response:
    """Top down forecasting

    Calculate forecast based on sum of of lower level timeseries and distribute forecast down based on ratios. Great feature for planning levels with dynamic timeseries.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlanningLevelRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_full_detail_post(request: web.Request, token=None, body=None) -> web.Response:
    """Full forecast result details, including error, trend seasonality and outlier

    Response provides full forecast result details, including error, trend seasonality and outlier. Great for advanced analysis.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlanningLevelRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_history_and_forecast_post(request: web.Request, token=None, body=None) -> web.Response:
    """History and forecast for fast timeseries view

    Reponse provides history and forecast per timeseries. Great for visualizing results.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlanningLevelRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_optimal_parameter_post(request: web.Request, token=None, body=None) -> web.Response:
    """Get optimal parameter per method

    Use the optimal parameter sets created by iCUE to set the method parameters of your internal planning system.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlanningLevelRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_post(request: web.Request, token=None, body=None) -> web.Response:
    """Forecasts only, for faster results

    To support maximum operation and integration speed, this endpoint only returns the calculated forecast.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlanningLevelRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_rerun_post(request: web.Request, token=None, body=None) -> web.Response:
    """Rerun previously uploaded planning level

    Rerun previously uploaded planning level.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlanningLevelReRunRequest.from_dict(body)
    return web.Response(status=200)


async def forecast_result_job_id_get(request: web.Request, job_id, token=None) -> web.Response:
    """Forecast result

    Get result for forecast job

    :param job_id: 
    :type job_id: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def forecast_status_job_id_get(request: web.Request, job_id, token=None) -> web.Response:
    """Forecast status

    Get status for forecast job

    :param job_id: 
    :type job_id: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def outlier_post(request: web.Request, token=None, body=None) -> web.Response:
    """Get outlier

    Identify outliers (single and repetitive spikes, seasonality, masked outliers, trend and level jumps, amongst other topics) and use for cleansing of the history stream prior to forecast claculation. Depending on math model used, this approach often improves results dramatically, as it removes disturbances.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = OutliersRequest.from_dict(body)
    return web.Response(status=200)
