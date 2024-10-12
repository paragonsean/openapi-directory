# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.funding_transfer118_wrapper import FundingTransfer118Wrapper
from openapi_server.models.transfer129_wrapper import Transfer129Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_create_funding(client):
    """Test case for create_funding

    The Funding Transaction enables the 'pull' of money from the sender's card to the Transaction Originator who is providing the Person to Merchant service. The amount that is debited from the Funding Account (sending consumer's account) will be the amount 'pushed' to the recipient via a payment transfer request.  Funds can be transferred from Mastercard® or Maestro® debit card accounts. To initiate the funding transaction, users can provide the sending consumer's Primary Account Number (PAN) or a unique identifier previously mapped to the sending consumer's account.
    """
    funding_transfer = openapi_server.FundingTransfer118Wrapper()
    headers = { 
        'Accept': 'application/xml',
        'Content-Type': 'application/xml',
    }
    response = await client.request(
        method='POST',
        path='/send/v1/partners/{partner_id}/transfers/funding'.format(partner_id='ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9'),
        headers=headers,
        json=funding_transfer,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

