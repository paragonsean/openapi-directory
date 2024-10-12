# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.setsinglecustomfieldvalue_request import SetsinglecustomfieldvalueRequest


pytestmark = pytest.mark.asyncio

async def test_removesinglecustomfieldvalue(client):
    """Test case for removesinglecustomfieldvalue

    Remove single custom field value
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/checkout/pub/orderForm/{order_form_id}/customData/{app_id}/{app_field_name}'.format(order_form_id='order_form_id_example', app_id='app_id_example', app_field_name='app_field_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_multiple_custom_field_values(client):
    """Test case for set_multiple_custom_field_values

    Set multiple custom field values
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/checkout/pub/orderForm/{order_form_id}/customData/{app_id}'.format(order_form_id='order_form_id_example', app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_single_custom_field_value(client):
    """Test case for set_single_custom_field_value

    Set single custom field value
    """
    body = {"value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/checkout/pub/orderForm/{order_form_id}/customData/{app_id}/{app_field_name}'.format(order_form_id='order_form_id_example', app_id='app_id_example', app_field_name='app_field_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

