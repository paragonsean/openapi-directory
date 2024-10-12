# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.checkout_agreements_data_agreement_interface import CheckoutAgreementsDataAgreementInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_checkout_agreements_checkout_agreements_repository_v1_get_list_get(client):
    """Test case for checkout_agreements_checkout_agreements_repository_v1_get_list_get

    carts/licence
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/carts/licence',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

