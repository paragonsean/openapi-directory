# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.jurisdiction import Jurisdiction
from openapi_server.models.jurisdiction_classification import JurisdictionClassification
from openapi_server.models.jurisdiction_include import JurisdictionInclude
from openapi_server.models.jurisdiction_list import JurisdictionList


pytestmark = pytest.mark.asyncio

async def test_jurisdiction_detail_jurisdictions_jurisdiction_id_get(client):
    """Test case for jurisdiction_detail_jurisdictions_jurisdiction_id_get

    Jurisdiction Detail
    """
    params = [('include', []),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/jurisdictions/{jurisdiction_id}'.format(jurisdiction_id='jurisdiction_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jurisdiction_list_jurisdictions_get(client):
    """Test case for jurisdiction_list_jurisdictions_get

    Jurisdiction List
    """
    params = [('classification', openapi_server.JurisdictionClassification()),
                    ('include', []),
                    ('page', 1),
                    ('per_page', 52),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/jurisdictions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

