# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.merchant_transfer54_wrapper import MerchantTransfer54Wrapper
from openapi_server.models.merchant_transfers69_wrapper import MerchantTransfers69Wrapper


pytestmark = pytest.mark.asyncio

async def test_get_merchant_transfer_by_id(client):
    """Test case for get_merchant_transfer_by_id

    Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/send/#env/v1/partners/{partner_id}/merchant/transfers/{transfer_id}'.format(partner_id='partner_id_example', transfer_id='transfer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchant_transfer_by_ref(client):
    """Test case for get_merchant_transfer_by_ref

    Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value.
    """
    params = [('ref', 'ref_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/send/#env/v1/partners/{partner_id}/merchant/transfers'.format(partner_id='partner_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

