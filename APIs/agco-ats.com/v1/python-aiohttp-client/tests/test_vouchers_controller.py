# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_paged_response_dealer_db_models_voucher import APIPagedResponseDealerDBModelsVoucher
from openapi_server.models.api_paged_response_dealer_db_models_voucher_history import APIPagedResponseDealerDBModelsVoucherHistory
from openapi_server.models.dealer_db_models_voucher import DealerDBModelsVoucher


pytestmark = pytest.mark.asyncio

async def test_api_v2_vouchers_voucher_code_get(client):
    """Test case for api_v2_vouchers_voucher_code_get

    Get a voucher
    """
    params = [('Deleted', 'deleted_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Vouchers/{voucher_code}'.format(voucher_code='voucher_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vouchers_delete(client):
    """Test case for vouchers_delete

    Delete a voucher
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/Vouchers/{voucher_code}'.format(voucher_code='voucher_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vouchers_get(client):
    """Test case for vouchers_get

    Gets a list of vouchers
    """
    params = [('Type', 'type_example'),
                    ('DealerCode', 'dealer_code_example'),
                    ('LicenseTo', 'license_to_example'),
                    ('Purpose', 'purpose_example'),
                    ('OrderNumber', 'order_number_example'),
                    ('Email', 'email_example'),
                    ('ModifiedBy', 'modified_by_example'),
                    ('CreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('CreatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('PunchedAfter', '2013-10-20T19:20:30+01:00'),
                    ('PunchedBefore', '2013-10-20T19:20:30+01:00'),
                    ('Punched', True),
                    ('ExpirationAfter', '2013-10-20T19:20:30+01:00'),
                    ('ExpirationBefore', '2013-10-20T19:20:30+01:00'),
                    ('Deleted', 'deleted_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Vouchers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vouchers_get_voucher_history(client):
    """Test case for vouchers_get_voucher_history

    Get a voucher's history.
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Vouchers/{voucher_code}/VoucherHistory'.format(voucher_code='voucher_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_vouchers_post(client):
    """Test case for vouchers_post

    Create a voucher
    """
    body = openapi_server.DealerDBModelsVoucher()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Vouchers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_vouchers_put(client):
    """Test case for vouchers_put

    Update a voucher
    """
    body = openapi_server.DealerDBModelsVoucher()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Vouchers/{voucher_code}'.format(voucher_code='voucher_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

