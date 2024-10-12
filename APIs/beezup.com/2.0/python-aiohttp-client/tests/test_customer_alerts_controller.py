# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.save_store_alert_request import SaveStoreAlertRequest
from openapi_server.models.store_alerts import StoreAlerts


pytestmark = pytest.mark.asyncio

async def test_get_store_alerts(client):
    """Test case for get_store_alerts

    Get store's alerts
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/stores/{store_id}/alerts'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_store_alerts(client):
    """Test case for save_store_alerts

    Save store alerts
    """
    body = {'key': openapi_server.SaveStoreAlertRequest()}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/stores/{store_id}/alerts'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

