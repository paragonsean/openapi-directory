# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill import Bill
from openapi_server.models.bill_include import BillInclude
from openapi_server.models.bill_list import BillList
from openapi_server.models.bill_sort_option import BillSortOption
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_bill_detail_bills_jurisdiction_session_bill_id_get(client):
    """Test case for bill_detail_bills_jurisdiction_session_bill_id_get

    Bill Detail
    """
    params = [('include', []),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/bills/{jurisdiction}/{session}/{bill_id}'.format(jurisdiction='jurisdiction_example', session='session_example', bill_id='bill_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bill_detail_by_id_bills_ocd_bill_openstates_bill_id_get(client):
    """Test case for bill_detail_by_id_bills_ocd_bill_openstates_bill_id_get

    Bill Detail By Id
    """
    params = [('include', []),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/bills/ocd-bill/{openstates_bill_id}'.format(openstates_bill_id='openstates_bill_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bills_search_bills_get(client):
    """Test case for bills_search_bills_get

    Bills Search
    """
    params = [('jurisdiction', 'jurisdiction_example'),
                    ('session', 'session_example'),
                    ('chamber', 'chamber_example'),
                    ('identifier', []),
                    ('classification', 'classification_example'),
                    ('subject', []),
                    ('updated_since', 'updated_since_example'),
                    ('created_since', 'created_since_example'),
                    ('action_since', 'action_since_example'),
                    ('sort', openapi_server.BillSortOption()),
                    ('sponsor', 'sponsor_example'),
                    ('sponsor_classification', 'sponsor_classification_example'),
                    ('q', 'q_example'),
                    ('include', []),
                    ('page', 1),
                    ('per_page', 10),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/bills',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

