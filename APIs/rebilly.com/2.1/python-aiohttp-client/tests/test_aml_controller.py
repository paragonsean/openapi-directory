# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aml import AML


pytestmark = pytest.mark.asyncio

async def test_get_aml_entry(client):
    """Test case for get_aml_entry

    Search PEP/Sanctions/Adverse Media lists
    """
    params = [('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example'),
                    ('dob', 'dob_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/aml',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

