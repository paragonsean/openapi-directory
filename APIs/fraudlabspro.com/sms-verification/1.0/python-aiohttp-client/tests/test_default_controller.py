# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_v1_verification_result_get(client):
    """Test case for v1_verification_result_get

    
    """
    params = [('tran_id', 'tran_id_example'),
                    ('key', 'key_example'),
                    ('format', 'format_example'),
                    ('otp', 'otp_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/verification/result',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_verification_send_post(client):
    """Test case for v1_verification_send_post

    
    """
    params = [('country_code', 'country_code_example'),
                    ('format', 'format_example'),
                    ('tel', 'tel_example'),
                    ('key', 'key_example'),
                    ('mesg', 'mesg_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='POST',
        path='/v1/verification/send',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

