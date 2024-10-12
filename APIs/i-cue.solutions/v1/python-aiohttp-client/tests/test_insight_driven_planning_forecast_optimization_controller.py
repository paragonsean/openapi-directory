# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

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


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_ai_history_and_forecast_post(client):
    """Test case for forecast_ai_history_and_forecast_post

    History and forecast utilizing advanced machine learning models
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"method":"icueMLP | icueMLO","params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast/AI/history-and-forecast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_aipost(client):
    """Test case for forecast_aipost

    Forecast utilizing advanced machine learning models
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"method":"icueMLP | icueMLO","params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast/AI',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_forecast_file_to_forecast_post(client):
    """Test case for forecast_file_to_forecast_post

    Forecast from file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'token': 'token_example',
    }
    data = FormData()
    data.add_field('discard_data', True)
    data.add_field('error_type', 'error_type_example')
    data.add_field('file', '/path/to/file')
    data.add_field('hold_out_period', 56)
    data.add_field('method', 'method_example')
    data.add_field('no_fcst', 56)
    data.add_field('outlier_detection', True)
    data.add_field('periodicity', 56)
    response = await client.request(
        method='POST',
        path='/forecast/file-to-forecast',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_forecast_bottom_up_post(client):
    """Test case for forecast_forecast_bottom_up_post

    Bottom up forecasting
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"method":"iCUE1","override":False,"params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast/forecast-bottom-up',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_forecast_top_down_post(client):
    """Test case for forecast_forecast_top_down_post

    Top down forecasting
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"method":"iCUE1","override":False,"params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016"}
    headers = { 
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast/forecast-top-down',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_full_detail_post(client):
    """Test case for forecast_full_detail_post

    Full forecast result details, including error, trend seasonality and outlier
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"method":"iCUE1","override":False,"params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast/full-detail',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_history_and_forecast_post(client):
    """Test case for forecast_history_and_forecast_post

    History and forecast for fast timeseries view
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"method":"iCUE1","override":False,"params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast/history-and-forecast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_optimal_parameter_post(client):
    """Test case for forecast_optimal_parameter_post

    Get optimal parameter per method
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"method":"iCUE1","override":False,"params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast/optimal-parameter',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_post(client):
    """Test case for forecast_post

    Forecasts only, for faster results
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"method":"iCUE1","override":False,"params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forecast_rerun_post(client):
    """Test case for forecast_rerun_post

    Rerun previously uploaded planning level
    """
    body = {"planningLevelId":0,"method":"iCUE1","params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/forecast/rerun',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_result_job_id_get(client):
    """Test case for forecast_result_job_id_get

    Forecast result
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/forecast/result/{job_id}'.format(job_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_status_job_id_get(client):
    """Test case for forecast_status_job_id_get

    Forecast status
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/forecast/status/{job_id}'.format(job_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_outlier_post(client):
    """Test case for outlier_post

    Get outlier
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/outlier',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

