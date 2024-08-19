# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.funding_reversal144_wrapper import FundingReversal144Wrapper
from openapi_server.models.transfer145_wrapper import Transfer145Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_create_funding_reversal(client):
    """Test case for create_funding_reversal

    Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account.
    """
    funding_reversal = openapi_server.FundingReversal144Wrapper()
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'application/xml',
    }
    response = await client.request(
        method='POST',
        path='/send/v1/partners/{partner_id}/transfers/{transfer_id}/transactions/{transaction_id}/reversals'.format(partner_id='partner_id_example', transfer_id='transfer_id_example', transaction_id='transaction_id_example'),
        headers=headers,
        json=funding_reversal,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

