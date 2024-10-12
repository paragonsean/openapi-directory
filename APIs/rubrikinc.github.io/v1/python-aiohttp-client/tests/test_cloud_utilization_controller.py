# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_out_forecast_request import CloudOutForecastRequest
from openapi_server.models.cloud_out_forecast_summary import CloudOutForecastSummary


pytestmark = pytest.mark.asyncio

async def test_do_cloud_out_forecast(client):
    """Test case for do_cloud_out_forecast

    Forecast of the cloud utilization for CloudOut
    """
    body = {"granularity":"Quarter","consolidationFilter":"ForecastWithConsolidation","slaParameters":{"advancedUiConfig":[{"retentionType":"Minute"},{"retentionType":"Minute"}],"archivalSpecs":{"archivalThreshold":6,"archivalTieringSpec":{"shouldTierExistingSnapshots":True,"minAccessibleDurationInSeconds":1,"coldStorageClass":"AzureArchive","isInstantTieringEnabled":True},"isPassthroughSupported":True,"locationName":"locationName","polarisManagedId":"polarisManagedId","locationId":"locationId"},"frequencies":{"daily":{"retention":5,"frequency":5},"monthly":{"dayOfMonth":"FirstDay","retention":7,"frequency":2},"hourly":{"retention":5,"frequency":5},"quarterly":{"dayOfQuarter":"FirstDay","firstQuarterStartMonth":"January","retention":3,"frequency":9},"yearly":{"dayOfYear":"FirstDay","retention":1,"frequency":7},"weekly":{"dayOfWeek":"Monday","retention":4,"frequency":2},"minute":{"retention":5,"frequency":5}},"maxLocalRetentionLimit":1},"forecastPeriodInGranularityUnit":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cloud_utilization/cloud_out_forecast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

