# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversion_rate_request import ConversionRateRequest


pytestmark = pytest.mark.asyncio

async def test_get_conversion_detail_using_get(client):
    """Test case for get_conversion_detail_using_get

    Get the currency conversion rate details.
    """
    params = [('fxDate', 'fx_date_example'),
                    ('transCurr', 'trans_curr_example'),
                    ('crdhldBillCurr', 'crdhld_bill_curr_example'),
                    ('bankFee', 3.4),
                    ('transAmt', 3.4)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/mcapi/settlement/currencyrate/conversion-rate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

