# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device


pytestmark = pytest.mark.asyncio

async def test_virtual_meter_calculate_formula_get(client):
    """Test case for virtual_meter_calculate_formula_get

    Calculates a virtual meter from a formula.               A meter is coded as ID(\"METERID\")
    """
    params = [('formula', 'formula_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/VirtualMeterCalculateFormula',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

