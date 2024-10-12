# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_pos_payment_response import CreatePosPaymentResponse
from openapi_server.models.delete_pos_payment_response import DeletePosPaymentResponse
from openapi_server.models.get_pos_payment_response import GetPosPaymentResponse
from openapi_server.models.get_pos_payments_response import GetPosPaymentsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.pos_payment import PosPayment
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_pos_payment_response import UpdatePosPaymentResponse


pytestmark = pytest.mark.asyncio

async def test_payments_add(client):
    """Test case for payments_add

    Create Payment
    """
    body = {"change_back_cash_amount":20,"created_at":"2020-09-30T07:43:32Z","tender_id":"12345","merchant_id":"12345","source":"external","location_id":"12345","custom_mappings":"{}","external_payment_id":"12345","approved":37.5,"total":37.5,"updated_at":"2020-09-30T07:43:32Z","idempotency_key":"random_string","app_fee":3,"currency":"USD","refunded":37.5,"tip":7,"id":"12345","cash":{"amount":"","charge_back_amount":""},"external_details":{"source_fee_amount":2.5,"source":"source","source_id":"source_id","type":"check"},"bank_account":{"country":"US","account_ownership_type":"account_ownership_type","bank_name":"bank_name","fingerprint":"fingerprint","transfer_type":"transfer_type","ach_details":{"account_type":"account_type","routing_number":"routing_number","account_number_suffix":"account_number_suffix"},"statement_description":"statement_description"},"card_details":{"card":{"reference_id":"card-001","bin":"41111","exp_month":1,"billing_address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"exp_year":2022,"merchant_id":"12345","card_type":"credit","cardholder_name":"John Doe","version":"230320320320","enabled":True,"last_4":"The last 4 digits of the card number.","card_brand":"visa","fingerprint":" Intended as a POS-assigned identifier, based on the card number, to identify the card across multiple locations within a single application.","prepaid_type":"prepaid","id":"12345","customer_id":"12345"}},"amount":27.5,"wallet":{"status":"authorized"},"device_id":"12345","processing_fees":[{"amount":1.05,"effective_at":"2020-09-30T07:43:32.000Z","processing_type":"initial"}],"service_charges":[{"amount":27500,"percentage":12.5,"name":"Charge for delivery","active":True,"currency":"USD","id":"12345","type":"auto_gratuity"},{"amount":27500,"percentage":12.5,"name":"Charge for delivery","active":True,"currency":"USD","id":"12345","type":"auto_gratuity"}],"tax":20,"created_by":"12345","employee_id":"12345","updated_by":"12345","source_id":"12345","customer_id":"12345","order_id":"12345","status":"approved"}
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
        path='/pos/payments',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_all(client):
    """Test case for payments_all

    List Payments
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pos/payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_delete(client):
    """Test case for payments_delete

    Delete Payment
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
        path='/pos/payments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_one(client):
    """Test case for payments_one

    Get Payment
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pos/payments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_update(client):
    """Test case for payments_update

    Update Payment
    """
    body = {"change_back_cash_amount":20,"created_at":"2020-09-30T07:43:32Z","tender_id":"12345","merchant_id":"12345","source":"external","location_id":"12345","custom_mappings":"{}","external_payment_id":"12345","approved":37.5,"total":37.5,"updated_at":"2020-09-30T07:43:32Z","idempotency_key":"random_string","app_fee":3,"currency":"USD","refunded":37.5,"tip":7,"id":"12345","cash":{"amount":"","charge_back_amount":""},"external_details":{"source_fee_amount":2.5,"source":"source","source_id":"source_id","type":"check"},"bank_account":{"country":"US","account_ownership_type":"account_ownership_type","bank_name":"bank_name","fingerprint":"fingerprint","transfer_type":"transfer_type","ach_details":{"account_type":"account_type","routing_number":"routing_number","account_number_suffix":"account_number_suffix"},"statement_description":"statement_description"},"card_details":{"card":{"reference_id":"card-001","bin":"41111","exp_month":1,"billing_address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"exp_year":2022,"merchant_id":"12345","card_type":"credit","cardholder_name":"John Doe","version":"230320320320","enabled":True,"last_4":"The last 4 digits of the card number.","card_brand":"visa","fingerprint":" Intended as a POS-assigned identifier, based on the card number, to identify the card across multiple locations within a single application.","prepaid_type":"prepaid","id":"12345","customer_id":"12345"}},"amount":27.5,"wallet":{"status":"authorized"},"device_id":"12345","processing_fees":[{"amount":1.05,"effective_at":"2020-09-30T07:43:32.000Z","processing_type":"initial"}],"service_charges":[{"amount":27500,"percentage":12.5,"name":"Charge for delivery","active":True,"currency":"USD","id":"12345","type":"auto_gratuity"},{"amount":27500,"percentage":12.5,"name":"Charge for delivery","active":True,"currency":"USD","id":"12345","type":"auto_gratuity"}],"tax":20,"created_by":"12345","employee_id":"12345","updated_by":"12345","source_id":"12345","customer_id":"12345","order_id":"12345","status":"approved"}
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
        path='/pos/payments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

