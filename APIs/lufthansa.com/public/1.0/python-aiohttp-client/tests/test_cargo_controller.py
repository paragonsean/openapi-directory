# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_cargo_get_route_from_date_product_code_by_origin_and_destination_get(client):
    """Test case for cargo_get_route_from_date_product_code_by_origin_and_destination_get

    Retrieve all flights
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/cargo/getRoute/{origin_destination}/{from_date}/{product_code}'.format(origin='origin_example', destination='destination_example', from_date='from_date_example', product_code='product_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cargo_shipment_tracking_by_awb_prefix_and_awb_number_get(client):
    """Test case for cargo_shipment_tracking_by_awb_prefix_and_awb_number_get

    Shipment Tracking
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/cargo/shipmentTracking/{a_wb_prefix_a_wb_number}'.format(a_wb_prefix='a_wb_prefix_example', a_wb_number='a_wb_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

