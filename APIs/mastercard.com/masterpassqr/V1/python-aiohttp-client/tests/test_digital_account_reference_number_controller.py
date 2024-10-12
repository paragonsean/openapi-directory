# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.digital_account86_wrapper import DigitalAccount86Wrapper
from openapi_server.models.digital_account87_wrapper import DigitalAccount87Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_digital_accnt_ref_num(client):
    """Test case for create_digital_accnt_ref_num

    Used to create a digital account reference number from Incontrol 
    """
    digital_account = openapi_server.DigitalAccount86Wrapper()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/send/v1/{partner_id}/digital-account'.format(partner_id='ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9'),
        headers=headers,
        json=digital_account,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

