# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_shipment_track_interface import SalesDataShipmentTrackInterface
from openapi_server.models.sales_shipment_track_repository_v1_save_post_request import SalesShipmentTrackRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_shipment_track_repository_v1_save_post(client):
    """Test case for sales_shipment_track_repository_v1_save_post

    shipment/track
    """
    body = openapi_server.SalesShipmentTrackRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/shipment/track',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

