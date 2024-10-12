# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.link_create_request import LinkCreateRequest
from openapi_server.models.link_response import LinkResponse
from openapi_server.models.page_link_response import PageLinkResponse


pytestmark = pytest.mark.asyncio

async def test_create_payment_link(client):
    """Test case for create_payment_link

    Create a payment link.
    """
    body = {"backgroundImage":"linear-gradient(to bottom right, #ffffff, #3295d6)","active":True,"description":"This payment is awesome!!","successUrl":"successUrl","language":"en_US","intent":"authorization","userId":"12345678","billing":{"zip":"24118","country":"DE","firstName":"John","lastName":"Doe","addressAddition":"7th floor","city":"Kiel","street":"Fraunhoferstr. 2-4","company":"PAYONE GmbH","state":"state"},"mode":"live","reference":"payment_1","accountId":"12345","errorUrl":"errorUrl","invoiceInformation":{"invoiceText":"invoiceText","invoiceId":"invoiceId"},"shipping":{"zip":"24118","country":"DE","firstName":"John","lastName":"Doe","addressAddition":"7th floor","city":"Kiel","street":"Fraunhoferstr. 2-4","company":"PAYONE GmbH","state":"state"},"merchantId":"12345","paymentMethods":["visa","mastercard"],"portalId":"1234567","shoppingCart":[{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"},{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"},{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"},{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"},{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"}],"logo":"https://www.payone.com/wp-content/uploads/2018/12/Payone-Logo-2020.jpg","notifyUrl":"notifyUrl","currency":"EUR","expiration":"2020-02-20","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        
    }
    response = await client.request(
        method='POST',
        path='/api/v1/payment-links',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_link(client):
    """Test case for get_payment_link

    Get payment link by id.
    """
    headers = { 
        'Accept': 'application/json',
        
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payment-links/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_links(client):
    """Test case for get_payment_links

    List all payment links.
    """
    params = [('page', 0),
                    ('limit', 25),
                    ('merchantId', 'merchant_id_example'),
                    ('accountId', 'account_id_example'),
                    ('portalId', 'portal_id_example'),
                    ('mode', 'mode_example')]
    headers = { 
        'Accept': 'application/json',
        
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payment-links',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment_link(client):
    """Test case for update_payment_link

    Update a payment link.
    """
    body = {"backgroundImage":"linear-gradient(to bottom right, #ffffff, #3295d6)","active":True,"description":"This payment is awesome!!","successUrl":"successUrl","language":"en_US","intent":"authorization","userId":"12345678","billing":{"zip":"24118","country":"DE","firstName":"John","lastName":"Doe","addressAddition":"7th floor","city":"Kiel","street":"Fraunhoferstr. 2-4","company":"PAYONE GmbH","state":"state"},"mode":"live","reference":"payment_1","accountId":"12345","errorUrl":"errorUrl","invoiceInformation":{"invoiceText":"invoiceText","invoiceId":"invoiceId"},"shipping":{"zip":"24118","country":"DE","firstName":"John","lastName":"Doe","addressAddition":"7th floor","city":"Kiel","street":"Fraunhoferstr. 2-4","company":"PAYONE GmbH","state":"state"},"merchantId":"12345","paymentMethods":["visa","mastercard"],"portalId":"1234567","shoppingCart":[{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"},{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"},{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"},{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"},{"number":"73883HFJ","quantity":1,"price":1999,"vatRate":20,"description":"Potatoes","deliveryDateStart":"2021-01-01","type":"goods","deliveryDateEnd":"2021-01-01"}],"logo":"https://www.payone.com/wp-content/uploads/2018/12/Payone-Logo-2020.jpg","notifyUrl":"notifyUrl","currency":"EUR","expiration":"2020-02-20","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/payment-links/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

