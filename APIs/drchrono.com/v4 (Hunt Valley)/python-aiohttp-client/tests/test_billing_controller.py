# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_line_item import BillingLineItem
from openapi_server.models.billing_profile import BillingProfile
from openapi_server.models.billing_profiles_list200_response import BillingProfilesList200Response
from openapi_server.models.cash_payment import CashPayment
from openapi_server.models.cash_payment_log import CashPaymentLog
from openapi_server.models.comm_logs_list200_response import CommLogsList200Response
from openapi_server.models.coverage import Coverage
from openapi_server.models.custom_insurance_plan_name import CustomInsurancePlanName
from openapi_server.models.custom_insurance_plan_names_list200_response import CustomInsurancePlanNamesList200Response
from openapi_server.models.eligibility_checks_list200_response import EligibilityChecksList200Response
from openapi_server.models.line_item_transaction import LineItemTransaction
from openapi_server.models.line_items_list200_response import LineItemsList200Response
from openapi_server.models.patient_payment_log_list200_response import PatientPaymentLogList200Response
from openapi_server.models.patient_payments_list200_response import PatientPaymentsList200Response
from openapi_server.models.phone_call_log import PhoneCallLog
from openapi_server.models.transactions_list200_response import TransactionsList200Response


pytestmark = pytest.mark.asyncio

async def test_billing_profiles_list(client):
    """Test case for billing_profiles_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/billing_profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_profiles_read(client):
    """Test case for billing_profiles_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/billing_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comm_logs_create(client):
    """Test case for comm_logs_create

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/comm_logs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comm_logs_list(client):
    """Test case for comm_logs_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/comm_logs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comm_logs_partial_update(client):
    """Test case for comm_logs_partial_update

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/comm_logs/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comm_logs_read(client):
    """Test case for comm_logs_read

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/comm_logs/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comm_logs_update(client):
    """Test case for comm_logs_update

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/comm_logs/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_insurance_plan_names_list(client):
    """Test case for custom_insurance_plan_names_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('user', 56),
                    ('name', 'name_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/custom_insurance_plan_names',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_insurance_plan_names_read(client):
    """Test case for custom_insurance_plan_names_read

    
    """
    params = [('since', 'since_example'),
                    ('user', 56),
                    ('name', 'name_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/custom_insurance_plan_names/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eligibility_checks_list(client):
    """Test case for eligibility_checks_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('appointment', 56),
                    ('appointment_date', 'appointment_date_example'),
                    ('doctor', 56),
                    ('query_date_range', 'query_date_range_example'),
                    ('appointment_date_range', 'appointment_date_range_example'),
                    ('query_date', 'query_date_example'),
                    ('patient', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/eligibility_checks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eligibility_checks_read(client):
    """Test case for eligibility_checks_read

    
    """
    params = [('appointment', 56),
                    ('appointment_date', 'appointment_date_example'),
                    ('doctor', 56),
                    ('query_date_range', 'query_date_range_example'),
                    ('appointment_date_range', 'appointment_date_range_example'),
                    ('query_date', 'query_date_example'),
                    ('patient', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/eligibility_checks/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_items_create(client):
    """Test case for line_items_create

    
    """
    params = [('posted_date', 'posted_date_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('service_date', 'service_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/line_items',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_items_delete(client):
    """Test case for line_items_delete

    
    """
    params = [('posted_date', 'posted_date_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('service_date', 'service_date_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/line_items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_items_list(client):
    """Test case for line_items_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('posted_date', 'posted_date_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('service_date', 'service_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/line_items',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_items_partial_update(client):
    """Test case for line_items_partial_update

    
    """
    params = [('posted_date', 'posted_date_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('service_date', 'service_date_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/line_items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_items_read(client):
    """Test case for line_items_read

    
    """
    params = [('posted_date', 'posted_date_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('service_date', 'service_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/line_items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_items_update(client):
    """Test case for line_items_update

    
    """
    params = [('posted_date', 'posted_date_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('service_date', 'service_date_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/line_items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_payment_log_list(client):
    """Test case for patient_payment_log_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('office', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_payment_log',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_payment_log_read(client):
    """Test case for patient_payment_log_read

    
    """
    params = [('since', 'since_example'),
                    ('office', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_payment_log/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_payments_create(client):
    """Test case for patient_payments_create

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_payments_list(client):
    """Test case for patient_payments_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_payments_read(client):
    """Test case for patient_payments_read

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_payments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_procedures_list(client):
    """Test case for procedures_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('mu_date', 'mu_date_example'),
                    ('patient', 56),
                    ('doctor', 56),
                    ('mu_date_range', 'mu_date_range_example'),
                    ('appointment', 56),
                    ('service_date', 'service_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/procedures',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_procedures_read(client):
    """Test case for procedures_read

    
    """
    params = [('mu_date', 'mu_date_example'),
                    ('patient', 56),
                    ('doctor', 56),
                    ('mu_date_range', 'mu_date_range_example'),
                    ('appointment', 56),
                    ('service_date', 'service_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/procedures/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_list(client):
    """Test case for transactions_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('line_item', 56),
                    ('posted_date', 'posted_date_example'),
                    ('appointment', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_read(client):
    """Test case for transactions_read

    
    """
    params = [('line_item', 56),
                    ('posted_date', 'posted_date_example'),
                    ('appointment', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transactions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

