# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tax_class_info200_response import TaxClassInfo200Response


pytestmark = pytest.mark.asyncio

async def test_tax_class_info(client):
    """Test case for tax_class_info

    
    """
    params = [('tax_class_id', 'tax_class_id_example'),
                    ('store_id', 'store_id_example'),
                    ('lang_id', 'lang_id_example'),
                    ('params', 'tax_class_id,name,avail'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/tax.class.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

