# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.get_payroll_response import GetPayrollResponse
from openapi_server.models.get_payrolls_response import GetPayrollsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.payrolls_filter import PayrollsFilter
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse


pytestmark = pytest.mark.asyncio

async def test_payrolls_all(client):
    """Test case for payrolls_all

    List Payroll
    """
    params = [('raw', False),
                    ('filter', openapi_server.PayrollsFilter()),
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
        path='/hris/payrolls',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payrolls_one(client):
    """Test case for payrolls_one

    Get Payroll
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
        path='/hris/payrolls/{payroll_id}'.format(payroll_id='payroll_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

