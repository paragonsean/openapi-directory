# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.all_request_types_example import AllRequestTypesExample
from openapi_server.models.all_response_types_example import AllResponseTypesExample


pytestmark = pytest.mark.asyncio

async def test_request_post(client):
    """Test case for request_post

    
    """
    body = {"opTypes":"heartbeat","heartbeat":{"op":"op","id":6},"orderSubscriptionMessage":{"op":"op","segmentationEnabled":True,"orderFilter":{"includeOverallPosition":True,"accountIds":[2,2],"customerStrategyRefs":["customerStrategyRefs","customerStrategyRefs"],"partitionMatchedByStrategyRef":True},"clk":"clk","heartbeatMs":3,"initialClk":"initialClk","conflateMs":9,"id":7},"marketSubscription":{"op":"op","segmentationEnabled":True,"clk":"clk","heartbeatMs":5,"initialClk":"initialClk","marketFilter":{"countryCodes":["countryCodes","countryCodes"],"bettingTypes":["ODDS","ODDS"],"turnInPlayEnabled":True,"marketTypes":["marketTypes","marketTypes"],"venues":["venues","venues"],"marketIds":["marketIds","marketIds"],"eventIds":["eventIds","eventIds"],"eventTypeIds":["eventTypeIds","eventTypeIds"],"bspMarket":True,"raceTypes":["raceTypes","raceTypes"]},"conflateMs":5,"id":1,"marketDataFilter":{"ladderLevels":2,"fields":["EX_BEST_OFFERS_DISP","EX_BEST_OFFERS_DISP"]}},"authentication":{"op":"op","session":"session","appKey":"appKey","id":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/request',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

