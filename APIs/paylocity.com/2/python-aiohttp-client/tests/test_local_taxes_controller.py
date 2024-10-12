# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.local_tax import LocalTax


pytestmark = pytest.mark.asyncio

async def test_add_local_tax(client):
    """Test case for add_local_tax

    Add new local tax
    """
    body = openapi_server.LocalTax()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/localTaxes'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_local_tax_by_tax_code(client):
    """Test case for delete_local_tax_by_tax_code

    Delete local tax by tax code
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/localTaxes/{tax_code}'.format(company_id='company_id_example', employee_id='employee_id_example', tax_code='tax_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_local_taxes(client):
    """Test case for get_all_local_taxes

    Get all local taxes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/localTaxes'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_local_tax_by_tax_code(client):
    """Test case for get_local_tax_by_tax_code

    Get local taxes by tax code
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/localTaxes/{tax_code}'.format(company_id='company_id_example', employee_id='employee_id_example', tax_code='tax_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

