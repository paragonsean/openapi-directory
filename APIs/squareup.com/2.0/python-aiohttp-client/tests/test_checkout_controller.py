# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_checkout_request import CreateCheckoutRequest
from openapi_server.models.create_checkout_response import CreateCheckoutResponse


pytestmark = pytest.mark.asyncio

async def test_create_checkout(client):
    """Test case for create_checkout

    CreateCheckout
    """
    body = {"request_body":{"additional_recipients":[{"amount_money":{"amount":60,"currency":"USD"},"description":"Application fees","location_id":"057P5VYJ4A5X1"}],"ask_for_shipping_address":True,"idempotency_key":"86ae1696-b1e3-4328-af6d-f1e04d947ad6","merchant_support_email":"merchant+support@website.com","order":{"idempotency_key":"12ae1696-z1e3-4328-af6d-f1e04d947gd4","order":{"customer_id":"customer_id","discounts":[{"amount_money":{"amount":100,"currency":"USD"},"scope":"LINE_ITEM","type":"FIXED_AMOUNT","uid":"56ae1696-z1e3-9328-af6d-f1e04d947gd4"}],"line_items":[{"applied_discounts":[{"discount_uid":"56ae1696-z1e3-9328-af6d-f1e04d947gd4"}],"applied_taxes":[{"tax_uid":"38ze1696-z1e3-5628-af6d-f1e04d947fg3"}],"base_price_money":{"amount":1500,"currency":"USD"},"name":"Printed T Shirt","quantity":"2"},{"base_price_money":{"amount":2500,"currency":"USD"},"name":"Slim Jeans","quantity":"1"},{"base_price_money":{"amount":3500,"currency":"USD"},"name":"Woven Sweater","quantity":"3"}],"location_id":"location_id","reference_id":"reference_id","taxes":[{"percentage":"7.75","scope":"LINE_ITEM","type":"INCLUSIVE","uid":"38ze1696-z1e3-5628-af6d-f1e04d947fg3"}]}},"pre_populate_buyer_email":"example@email.com","pre_populate_shipping_address":{"address_line_1":"1455 Market St.","address_line_2":"Suite 600","administrative_district_level_1":"CA","country":"US","first_name":"Jane","last_name":"Doe","locality":"San Francisco","postal_code":"94103"},"redirect_url":"https://merchant.website.com/order-confirm"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/locations/{location_id}/checkouts'.format(location_id='location_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

