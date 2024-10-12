# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payments_program_onboarding_response import PaymentsProgramOnboardingResponse


pytestmark = pytest.mark.asyncio

async def test_get_payments_program_onboarding(client):
    """Test case for get_payments_program_onboarding

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/payments_program/{marketplace_id}/{payments_program_type}/onboarding'.format(marketplace_id='marketplace_id_example', payments_program_type='payments_program_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

