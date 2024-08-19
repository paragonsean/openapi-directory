# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.find_form_by_form_name200_response import FindFormByFormName200Response
from openapi_server.models.find_form_by_form_name404_response import FindFormByFormName404Response
from openapi_server.models.find_forms200_response import FindForms200Response
from openapi_server.models.find_forms401_response import FindForms401Response
from openapi_server.models.find_forms429_response import FindForms429Response


pytestmark = pytest.mark.asyncio

async def test_find_form_by_form_name(client):
    """Test case for find_form_by_form_name

    Find form by form name
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/services/va_forms/v0/forms/{form_name}'.format(form_name='10-10EZ'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_forms(client):
    """Test case for find_forms

    Returns all VA Forms and their last revision date
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/services/va_forms/v0/forms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

