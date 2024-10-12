# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.patch_payment_instrument_request import PatchPaymentInstrumentRequest
from openapi_server.models.payment_instrument2 import PaymentInstrument2
from openapi_server.models.post_payment_instrument_request import PostPaymentInstrumentRequest


pytestmark = pytest.mark.asyncio

async def test_get_payment_instrument(client):
    """Test case for get_payment_instrument

    Retrieve a Payment Instrument
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payment-instruments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_instrument_collection(client):
    """Test case for get_payment_instrument_collection

    Retrieve a list of payment instruments
    """
    params = [('filter', 'filter_example'),
                    ('sort', ['sort_example']),
                    ('limit', 56),
                    ('offset', 56),
                    ('q', 'q_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payment-instruments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_payment_instrument(client):
    """Test case for patch_payment_instrument

    Update a Payment Instrument's values
    """
    body = openapi_server.PatchPaymentInstrumentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/payment-instruments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_instrument(client):
    """Test case for post_payment_instrument

    Create a Payment Instrument
    """
    body = openapi_server.PostPaymentInstrumentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payment-instruments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_instrument_deactivation(client):
    """Test case for post_payment_instrument_deactivation

    Deactivate a payment instrument
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payment-instruments/{id}/deactivation'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

