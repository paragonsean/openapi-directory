# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_payment_response import CreatePaymentResponse
from openapi_server.models.delete_payment_response import DeletePaymentResponse
from openapi_server.models.get_payment_response import GetPaymentResponse
from openapi_server.models.get_payments_response import GetPaymentsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment import Payment
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.payments_filter import PaymentsFilter
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_payment_response import UpdatePaymentResponse


pytestmark = pytest.mark.asyncio

async def test_payments_add(client):
    """Test case for payments_add

    Create Payment
    """
    body = {"note":"Some notes about this payment","display_id":"123456","created_at":"2020-09-30T07:43:32Z","type":"accounts_receivable","custom_mappings":"{}","reference":"123456","currency_rate":0.69,"allocations":[{"amount":49.99,"code":"N091","id":"123456","type":"invoice"},{"amount":49.99,"code":"N091","id":"123456","type":"invoice"}],"updated_at":"2020-09-30T07:43:32Z","supplier":{"address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"display_id":"SUPP00101","company_name":"The boring company","id":"12345","display_name":"Windsurf Shop"},"currency":"USD","downstream_id":"12345","id":"123456","payment_method":"Credit Card","transaction_date":"2021-05-01T12:00:00Z","accounts_receivable_account_id":"123456","reconciled":True,"payment_method_reference":"123456","created_by":"12345","payment_method_id":"123456","accounts_receivable_account_type":"Account","total_amount":49.99,"row_version":"1-12345","updated_by":"12345","account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"customer":{"display_id":"CUST00101","company_name":"The boring company","name":"Windsurf Shop","id":"12345","display_name":"Windsurf Shop"},"status":"authorised"}
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
        path='/accounting/payments',
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
                    ('filter', openapi_server.PaymentsFilter()),
                    ('pass_through', None),
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
        path='/accounting/payments',
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
        path='/accounting/payments/{id}'.format(id='id_example'),
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
        path='/accounting/payments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_update(client):
    """Test case for payments_update

    Update Payment
    """
    body = {"note":"Some notes about this payment","display_id":"123456","created_at":"2020-09-30T07:43:32Z","type":"accounts_receivable","custom_mappings":"{}","reference":"123456","currency_rate":0.69,"allocations":[{"amount":49.99,"code":"N091","id":"123456","type":"invoice"},{"amount":49.99,"code":"N091","id":"123456","type":"invoice"}],"updated_at":"2020-09-30T07:43:32Z","supplier":{"address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"display_id":"SUPP00101","company_name":"The boring company","id":"12345","display_name":"Windsurf Shop"},"currency":"USD","downstream_id":"12345","id":"123456","payment_method":"Credit Card","transaction_date":"2021-05-01T12:00:00Z","accounts_receivable_account_id":"123456","reconciled":True,"payment_method_reference":"123456","created_by":"12345","payment_method_id":"123456","accounts_receivable_account_type":"Account","total_amount":49.99,"row_version":"1-12345","updated_by":"12345","account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"customer":{"display_id":"CUST00101","company_name":"The boring company","name":"Windsurf Shop","id":"12345","display_name":"Windsurf Shop"},"status":"authorised"}
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
        path='/accounting/payments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

