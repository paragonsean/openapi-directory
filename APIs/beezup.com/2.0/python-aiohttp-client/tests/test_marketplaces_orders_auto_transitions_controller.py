# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.automatic_transition_info_list import AutomaticTransitionInfoList
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.configure_automatic_transition_request import ConfigureAutomaticTransitionRequest


pytestmark = pytest.mark.asyncio

async def test_configure_automatic_transitions(client):
    """Test case for configure_automatic_transitions

    Configure new or existing automatic Order status transition
    """
    body = openapi_server.ConfigureAutomaticTransitionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/automaticTransitions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automatic_transitions(client):
    """Test case for get_automatic_transitions

    Get list of configured automatic Order status transitions
    """
    params = [('storeId', '04730364-9826-4ff3-92e4-51fccd02bf10')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/automaticTransitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

