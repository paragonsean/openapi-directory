# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.creditor_account import CreditorAccount
from openapi_server.models.creditor_account_write import CreditorAccountWrite
from openapi_server.models.creditor_account_write_request import CreditorAccountWriteRequest
from openapi_server.models.paginated_creditor_account_list import PaginatedCreditorAccountList
from openapi_server.models.paginated_payment_read_list import PaginatedPaymentReadList
from openapi_server.models.payment_read import PaymentRead
from openapi_server.models.payment_read_request import PaymentReadRequest
from openapi_server.models.payment_write import PaymentWrite
from openapi_server.models.payment_write_request import PaymentWriteRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_payment(client):
    """Test case for create_payment

    
    """
    body = {"periodic_payment":{"end_date":"2000-01-23","day_of_execution":"day_of_execution","execution_rule":"","frequency":"","start_date":"2000-01-23"},"redirect":"https://openapi-generator.tech","instructed_amount":"","payment_product":"","creditor_account":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","requested_execution_date":"2000-01-23","creditor_object":"","description":"GOCARDLESS","custom_payment_id":"custom_payment_id","submit_payment":False,"debtor_account":"","institution_id":"SWEDBANK_SANDBOX_SANDLV22"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/payments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_periodic_payment(client):
    """Test case for delete_periodic_payment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/payments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_minimum_required_fields_for_institution(client):
    """Test case for list_minimum_required_fields_for_institution

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/payments/fields/{institution_id}'.format(institution_id='institution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payments(client):
    """Test case for list_payments

    
    """
    params = [('limit', 100),
                    ('offset', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/payments/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_payments_creditors_create(client):
    """Test case for payments_creditors_create

    
    """
    body = {"agent":"agent","agent_name":"agent_name","address_country":"AT","address_street":"address_street","post_code":"post_code","name":"name","currency":"currency","type":"","account":"account","institution_id":"institution_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/payments/creditors/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_creditors_destroy(client):
    """Test case for payments_creditors_destroy

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/payments/creditors/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_creditors_list(client):
    """Test case for payments_creditors_list

    
    """
    params = [('account', 'account_example'),
                    ('address_country', 'address_country_example'),
                    ('agent', 'agent_example'),
                    ('currency', 'currency_example'),
                    ('limit', 100),
                    ('name', 'name_example'),
                    ('offset', 1),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/payments/creditors/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_creditors_retrieve(client):
    """Test case for payments_creditors_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/payments/creditors/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_payments_submit_create(client):
    """Test case for payments_submit_create

    
    """
    body = {"redirect":"https://openapi-generator.tech","instructed_amount":"","payment_product":"","creditor_account":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","creditor_object":"","description":"GOCARDLESS","custom_payment_id":"custom_payment_id","debtor_account":{"address_country":"address_country","address_street":"address_street","post_code":"post_code","name":"name","type_number":"type_number","currency":"currency","type":"","account":"account"},"institution_id":"SWEDBANK_SANDBOX_SANDLV22"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/payments/{id}/submit'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_all_payment_creditor_accounts(client):
    """Test case for retrieve_all_payment_creditor_accounts

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/payments/account/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_payment(client):
    """Test case for retrieve_payment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/payments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

