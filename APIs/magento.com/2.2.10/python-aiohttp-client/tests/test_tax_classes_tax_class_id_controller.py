# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_data_tax_class_interface import TaxDataTaxClassInterface


pytestmark = pytest.mark.asyncio

async def test_tax_tax_class_repository_v1_delete_by_id_delete(client):
    """Test case for tax_tax_class_repository_v1_delete_by_id_delete

    taxClasses/{taxClassId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/taxClasses/{tax_class_id}'.format(tax_class_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tax_tax_class_repository_v1_get_get(client):
    """Test case for tax_tax_class_repository_v1_get_get

    taxClasses/{taxClassId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/taxClasses/{tax_class_id}'.format(tax_class_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

