# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_purchase_order_response import CreatePurchaseOrderResponse
from openapi_server.models.delete_purchase_order_response import DeletePurchaseOrderResponse
from openapi_server.models.get_purchase_order_response import GetPurchaseOrderResponse
from openapi_server.models.get_purchase_orders_response import GetPurchaseOrdersResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.purchase_order import PurchaseOrder
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_purchase_order_response import UpdatePurchaseOrderResponse


pytestmark = pytest.mark.asyncio

async def test_purchase_orders_add(client):
    """Test case for purchase_orders_add

    Create Purchase Order
    """
    body = {"channel":"email","created_at":"2020-09-30T07:43:32Z","memo":"Thank you for the partnership and have a great day!","discount_percentage":5.5,"line_items":[{"tax_amount":27500,"item":{"code":"120-C","name":"Model Y","id":"12344"},"code":"120-C","quantity":1,"department_id":"1234","discount_amount":19.99,"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","discount_percentage":0.01,"type":"sales_item","unit_price":27500.5,"created_by":"12345","location_id":"1234","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"line_number":1,"row_version":"1-12345","updated_by":"12345","unit_of_measure":"pc.","id":"12345","row_id":"12345"},{"tax_amount":27500,"item":{"code":"120-C","name":"Model Y","id":"12344"},"code":"120-C","quantity":1,"department_id":"1234","discount_amount":19.99,"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","discount_percentage":0.01,"type":"sales_item","unit_price":27500.5,"created_by":"12345","location_id":"1234","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"line_number":1,"row_version":"1-12345","updated_by":"12345","unit_of_measure":"pc.","id":"12345","row_id":"12345"}],"custom_mappings":"{}","expected_arrival_date":"2020-09-30","reference":"123456","currency_rate":0.69,"po_number":"90000117","total":27500,"issued_date":"2020-09-30","updated_at":"2020-09-30T07:43:32Z","ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"supplier":{"address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"display_id":"SUPP00101","company_name":"The boring company","id":"12345","display_name":"Windsurf Shop"},"currency":"USD","downstream_id":"12345","id":"12345","shipping_address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"payment_method":"cash","accounting_by_row":False,"bank_account":{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","bank_name":"Monzo","currency":"USD","routing_number":"012345678","bic":"AUDSCHGGXXX","branch_identifier":"001"},"due_date":"2020-10-30","tax_inclusive":True,"total_tax":2500,"created_by":"12345","delivery_date":"2020-09-30","tax_code":"1234","row_version":"1-12345","sub_total":27500,"updated_by":"12345","template_id":"123456","status":"open"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/accounting/purchase-orders',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchase_orders_all(client):
    """Test case for purchase_orders_all

    List Purchase Orders
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('pass_through', None),
                    ('limit', 20)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounting/purchase-orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchase_orders_delete(client):
    """Test case for purchase_orders_delete

    Delete Purchase Order
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/accounting/purchase-orders/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchase_orders_one(client):
    """Test case for purchase_orders_one

    Get Purchase Order
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounting/purchase-orders/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchase_orders_update(client):
    """Test case for purchase_orders_update

    Update Purchase Order
    """
    body = {"channel":"email","created_at":"2020-09-30T07:43:32Z","memo":"Thank you for the partnership and have a great day!","discount_percentage":5.5,"line_items":[{"tax_amount":27500,"item":{"code":"120-C","name":"Model Y","id":"12344"},"code":"120-C","quantity":1,"department_id":"1234","discount_amount":19.99,"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","discount_percentage":0.01,"type":"sales_item","unit_price":27500.5,"created_by":"12345","location_id":"1234","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"line_number":1,"row_version":"1-12345","updated_by":"12345","unit_of_measure":"pc.","id":"12345","row_id":"12345"},{"tax_amount":27500,"item":{"code":"120-C","name":"Model Y","id":"12344"},"code":"120-C","quantity":1,"department_id":"1234","discount_amount":19.99,"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","discount_percentage":0.01,"type":"sales_item","unit_price":27500.5,"created_by":"12345","location_id":"1234","tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"},"custom_mappings":"{}","updated_at":"2020-09-30T07:43:32Z","total_amount":27500,"ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"line_number":1,"row_version":"1-12345","updated_by":"12345","unit_of_measure":"pc.","id":"12345","row_id":"12345"}],"custom_mappings":"{}","expected_arrival_date":"2020-09-30","reference":"123456","currency_rate":0.69,"po_number":"90000117","total":27500,"issued_date":"2020-09-30","updated_at":"2020-09-30T07:43:32Z","ledger_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"supplier":{"address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"display_id":"SUPP00101","company_name":"The boring company","id":"12345","display_name":"Windsurf Shop"},"currency":"USD","downstream_id":"12345","id":"12345","shipping_address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"payment_method":"cash","accounting_by_row":False,"bank_account":{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","bank_name":"Monzo","currency":"USD","routing_number":"012345678","bic":"AUDSCHGGXXX","branch_identifier":"001"},"due_date":"2020-10-30","tax_inclusive":True,"total_tax":2500,"created_by":"12345","delivery_date":"2020-09-30","tax_code":"1234","row_version":"1-12345","sub_total":27500,"updated_by":"12345","template_id":"123456","status":"open"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/accounting/purchase-orders/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

