# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_convert(client):
    """Test case for convert

    
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('hundreds_form', 'hundreds_form_example')
    data.add_field('the_number', 'the_number_example')
    data.add_field('unit', 'unit_example')
    response = await client.request(
        method='POST',
        path='/convert',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

