# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_customer_support_customer_response import CreateCustomerSupportCustomerResponse
from openapi_server.models.customer_support_customer import CustomerSupportCustomer
from openapi_server.models.delete_customer_support_customer_response import DeleteCustomerSupportCustomerResponse
from openapi_server.models.get_customer_support_customer_response import GetCustomerSupportCustomerResponse
from openapi_server.models.get_customer_support_customers_response import GetCustomerSupportCustomersResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_customer_support_customer_response import UpdateCustomerSupportCustomerResponse


pytestmark = pytest.mark.asyncio

async def test_customers_add(client):
    """Test case for customers_add

    Create Customer Support Customer
    """
    body = {"addresses":[{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"}],"notes":"Some notes about this customer","individual":True,"created_at":"2020-09-30T07:43:32Z","last_name":"Musk","created_by":"12345","emails":[{"id":"123","type":"primary","email":"elon@musk.com"},{"id":"123","type":"primary","email":"elon@musk.com"}],"phone_numbers":[{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"},{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"}],"updated_at":"2020-09-30T07:43:32Z","tax_number":"US123945459","company_name":"SpaceX","updated_by":"12345","currency":"USD","bank_accounts":{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","currency":"USD","bic":"AUDSCHGGXXX","branch_identifier":"001"},"id":"12345","first_name":"Elon","status":"active"}
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
        path='/customer-support/customers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_all(client):
    """Test case for customers_all

    List Customer Support Customers
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
        path='/customer-support/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_delete(client):
    """Test case for customers_delete

    Delete Customer Support Customer
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
        path='/customer-support/customers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_one(client):
    """Test case for customers_one

    Get Customer Support Customer
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
        path='/customer-support/customers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_update(client):
    """Test case for customers_update

    Update Customer Support Customer
    """
    body = {"addresses":[{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"}],"notes":"Some notes about this customer","individual":True,"created_at":"2020-09-30T07:43:32Z","last_name":"Musk","created_by":"12345","emails":[{"id":"123","type":"primary","email":"elon@musk.com"},{"id":"123","type":"primary","email":"elon@musk.com"}],"phone_numbers":[{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"},{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"}],"updated_at":"2020-09-30T07:43:32Z","tax_number":"US123945459","company_name":"SpaceX","updated_by":"12345","currency":"USD","bank_accounts":{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","currency":"USD","bic":"AUDSCHGGXXX","branch_identifier":"001"},"id":"12345","first_name":"Elon","status":"active"}
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
        path='/customer-support/customers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

