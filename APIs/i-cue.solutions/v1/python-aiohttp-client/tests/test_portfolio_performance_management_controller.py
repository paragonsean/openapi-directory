# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.forecast_performance_request import ForecastPerformanceRequest
from openapi_server.models.portfolio_abc_model import PortfolioAbcModel
from openapi_server.models.portfolio_model import PortfolioModel
from openapi_server.models.portfolio_request import PortfolioRequest
from openapi_server.models.portfolio_xyz_model import PortfolioXyzModel
from openapi_server.models.rewind_response import RewindResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_portfolio_abc_post(client):
    """Test case for portfolio_abc_post

    ABC Analysis
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/portfolio/abc',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_portfolio_file_to_portfolio_post(client):
    """Test case for portfolio_file_to_portfolio_post

    ABCxyz Analysis
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'token': 'token_example',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/portfolio/file-to-portfolio',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_portfolio_forecast_performance_rewind_post(client):
    """Test case for portfolio_forecast_performance_rewind_post

    Planning level rewind to calculate and measure performance potential (internal versus iCUE).
    """
    body = {"planningLevelId":"planningLevelId","data":[{"forecastValues":[0.8008281904610115,0.8008281904610115],"timeSeriesId":"timeSeriesId","historyValues":[6.027456183070403,6.027456183070403]},{"forecastValues":[0.8008281904610115,0.8008281904610115],"timeSeriesId":"timeSeriesId","historyValues":[6.027456183070403,6.027456183070403]}],"method":"iCUE1","rewindTimeFrame":12,"params":{"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"noFcst":18,"holdOutPeriod":4,"outlierDetection":True},"startDate":"1/16/2016","costOfError":200}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/portfolio/forecast-performance-rewind',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_portfolio_post(client):
    """Test case for portfolio_post

    ABCxyz Analysis
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/portfolio',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_portfolio_xyz_post(client):
    """Test case for portfolio_xyz_post

    xyz Analysis
    """
    body = {"planningLevelId":"planningLevelId","data":[{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]},{"timeSeriesId":"timeSeriesId","historyValues":[0.8008281904610115,0.8008281904610115]}],"startDate":"1/16/2016"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/portfolio/xyz',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

