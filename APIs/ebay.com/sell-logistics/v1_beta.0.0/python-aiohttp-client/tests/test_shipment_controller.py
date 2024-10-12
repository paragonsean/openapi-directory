# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_shipment_from_quote_request import CreateShipmentFromQuoteRequest
from openapi_server.models.shipment import Shipment


pytestmark = pytest.mark.asyncio

async def test_cancel_shipment(client):
    """Test case for cancel_shipment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/logistics/v1_beta/shipment/{shipment_id}/cancel'.format(shipment_id='shipment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_from_shipping_quote(client):
    """Test case for create_from_shipping_quote

    
    """
    body = {"labelCustomMessage":"labelCustomMessage","additionalOptions":[{"optionType":"optionType","additionalCost":{"currency":"currency","value":"value"}},{"optionType":"optionType","additionalCost":{"currency":"currency","value":"value"}}],"labelSize":"labelSize","returnTo":{"primaryPhone":{"phoneNumber":"phoneNumber"},"companyName":"companyName","fullName":"fullName","contactAddress":{"stateOrProvince":"stateOrProvince","city":"city","countryCode":"countryCode","postalCode":"postalCode","county":"county","addressLine1":"addressLine1","addressLine2":"addressLine2"}},"shippingQuoteId":"shippingQuoteId","rateId":"rateId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/logistics/v1_beta/shipment/create_from_shipping_quote',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_label_file(client):
    """Test case for download_label_file

    
    """
    headers = { 
        'Accept': 'application/pdf',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/logistics/v1_beta/shipment/{shipment_id}/download_label_file'.format(shipment_id='shipment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipment(client):
    """Test case for get_shipment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/logistics/v1_beta/shipment/{shipment_id}'.format(shipment_id='shipment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

