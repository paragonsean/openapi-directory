# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_extracts_event_response import DataExtractsEventResponse
from openapi_server.models.data_extracts_user_data_response import DataExtractsUserDataResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_get_data_extracts_events(client):
    """Test case for get_data_extracts_events

    Get Events
    """
    params = [('eventName', 'event_name_example'),
                    ('fromDate', 'from_date_example'),
                    ('toDate', 'to_date_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/dataExtracts/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_extracts_user_data(client):
    """Test case for get_data_extracts_user_data

    Get userData
    """
    params = [('fromDate', 'from_date_example'),
                    ('loginName', 'login_name_example'),
                    ('toDate', 'to_date_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/dataExtracts/userData',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

