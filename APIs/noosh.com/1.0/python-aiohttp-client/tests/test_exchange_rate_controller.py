# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.multi_exchange_rate_list_vo import MultiExchangeRateListVO
from openapi_server.models.multi_exchange_rate_persist_list_vo import MultiExchangeRatePersistListVO


pytestmark = pytest.mark.asyncio

async def test_get_exchange_rate_list(client):
    """Test case for get_exchange_rate_list

    Get Exchange Rate List
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/exchangeRate'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_exchange_rate(client):
    """Test case for post_exchange_rate

    Create Exchange Rates
    """
    body = {"exchange_rates":[{"activate_date":"2000-01-23","rate":"","currency":"sample currency","buClientWorkgroupId":1,"target":"sample target"},{"activate_date":"2000-01-23","rate":"","currency":"sample currency","buClientWorkgroupId":1,"target":"sample target"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/exchangeRate'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

