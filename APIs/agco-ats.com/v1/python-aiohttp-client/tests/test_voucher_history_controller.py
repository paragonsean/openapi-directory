# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_paged_response_dealer_db_models_voucher_history import APIPagedResponseDealerDBModelsVoucherHistory


pytestmark = pytest.mark.asyncio

async def test_voucher_history_get_voucher_history(client):
    """Test case for voucher_history_get_voucher_history

    Gets voucher history data
    """
    params = [('VoucherCode', 'voucher_code_example'),
                    ('ChangedBefore', '2013-10-20T19:20:30+01:00'),
                    ('ChangedAfter', '2013-10-20T19:20:30+01:00'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/VoucherHistory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

