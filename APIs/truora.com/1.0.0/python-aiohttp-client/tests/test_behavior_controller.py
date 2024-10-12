# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.behaviour_output import BehaviourOutput
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_report_behavior(client):
    """Test case for report_behavior

    Report Behavior
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
    }
    data = {
        'birth_date': '2013-10-20T19:20:30+01:00',
        'country': 'country_example',
        'document_id': 'document_id_example',
        'document_type': 'document_type_example',
        'email': 'email_example',
        'feedback_date': '2013-10-20T19:20:30+01:00',
        'first_name': 'first_name_example',
        'last_name': 'last_name_example',
        'phone_number': 'phone_number_example',
        'reason': 'reason_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/behavior',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

