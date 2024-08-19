# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.digital_account89_wrapper import DigitalAccount89Wrapper
from openapi_server.models.digital_account90_wrapper import DigitalAccount90Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_retrieve_digital_accnt_ref_num_list(client):
    """Test case for retrieve_digital_accnt_ref_num_list

    Used to retreive a digital account reference list from Incontrol 
    """
    digital_account = openapi_server.DigitalAccount89Wrapper()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/send/v1/{partner_id}/digital-account/search'.format(partner_id='partner_id_example'),
        headers=headers,
        json=digital_account,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

