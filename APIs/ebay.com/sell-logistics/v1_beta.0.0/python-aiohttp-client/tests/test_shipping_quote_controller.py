# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.shipping_quote import ShippingQuote
from openapi_server.models.shipping_quote_request import ShippingQuoteRequest


pytestmark = pytest.mark.asyncio

async def test_create_shipping_quote(client):
    """Test case for create_shipping_quote

    
    """
    body = {"packageSpecification":{"weight":{"unit":"unit","value":"value"},"dimensions":{"unit":"unit","length":"length","width":"width","height":"height"}},"shipFrom":{"primaryPhone":{"phoneNumber":"phoneNumber"},"companyName":"companyName","fullName":"fullName","contactAddress":{"stateOrProvince":"stateOrProvince","city":"city","countryCode":"countryCode","postalCode":"postalCode","county":"county","addressLine1":"addressLine1","addressLine2":"addressLine2"}},"orders":[{"orderId":"orderId","channel":"channel"},{"orderId":"orderId","channel":"channel"}],"shipTo":{"primaryPhone":{"phoneNumber":"phoneNumber"},"companyName":"companyName","fullName":"fullName","contactAddress":{"stateOrProvince":"stateOrProvince","city":"city","countryCode":"countryCode","postalCode":"postalCode","county":"county","addressLine1":"addressLine1","addressLine2":"addressLine2"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/logistics/v1_beta/shipping_quote',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipping_quote(client):
    """Test case for get_shipping_quote

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/logistics/v1_beta/shipping_quote/{shipping_quote_id}'.format(shipping_quote_id='shipping_quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

