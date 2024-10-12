# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.codat_error_message import CodatErrorMessage
from openapi_server.models.company_configuration import CompanyConfiguration


pytestmark = pytest.mark.asyncio

async def test_get_company_configuration(client):
    """Test case for get_company_configuration

    Get company configuration
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/sync/expenses/config'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_company_configuration(client):
    """Test case for save_company_configuration

    Set company configuration
    """
    body = {"bankAccount":{"id":"32"},"supplier":{"id":"124"},"customer":{"id":"142"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/companies/{company_id}/sync/expenses/config'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

