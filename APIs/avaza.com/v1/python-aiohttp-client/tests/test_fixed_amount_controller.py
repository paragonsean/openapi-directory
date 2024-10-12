# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fixed_amount_list import FixedAmountList


pytestmark = pytest.mark.asyncio

async def test_fixed_amount_get(client):
    """Test case for fixed_amount_get

    Gets list of Fixed Amounts
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('EntryDateFrom', '2013-10-20T19:20:30+01:00'),
                    ('EntryDateTo', '2013-10-20T19:20:30+01:00'),
                    ('ProjectID', 56),
                    ('TaskID', 56),
                    ('isInvoiced', True),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/FixedAmount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

