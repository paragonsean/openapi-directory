# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_all_transfers200_response import GetAllTransfers200Response
from openapi_server.models.get_sub_partner_balance200_response import GetSubPartnerBalance200Response
from openapi_server.models.get_transfer200_response import GetTransfer200Response


pytestmark = pytest.mark.asyncio

async def test_get_all_transfers(client):
    """Test case for get_all_transfers

    Get all transfers
    """
    params = [('id', '111'),
                    ('status', 'CREATED'),
                    ('limit', '10'),
                    ('offset', '0'),
                    ('order', 'ASC')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/sub-partner/transfers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_partner_balance(client):
    """Test case for get_sub_partner_balance

    Get sub-partner balance
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/sub-partner/balance/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_partners(client):
    """Test case for get_sub_partners

    Get sub-partners
    """
    params = [('id', '111'),
                    ('offset', '0'),
                    ('limit', '10'),
                    ('order', 'DESC')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/sub-partner',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transfer(client):
    """Test case for get_transfer

    Get transfer
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/sub-partner/transfer/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

