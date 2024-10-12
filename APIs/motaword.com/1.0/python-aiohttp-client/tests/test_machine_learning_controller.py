# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delivery_prediction_payload import DeliveryPredictionPayload
from openapi_server.models.delivery_prediction_response import DeliveryPredictionResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_delivery_prediction(client):
    """Test case for get_delivery_prediction

    Get a delivery prediction for a project
    """
    body = {"projectId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ml/delivery-prediction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

