# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.code_sample import CodeSample
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_code_find_by_element_element_get(client):
    """Test case for code_find_by_element_element_get

    Finds code samples by XML element
    """
    params = [('namespace', 'http://www.tei-c.org/ns/1.0'),
                    ('docType', ['doc_type_example']),
                    ('offset', 1),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/code/findByElement/{element}'.format(element='element_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

