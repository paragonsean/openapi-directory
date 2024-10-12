# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_v1_order_feedback_post(client):
    """Test case for v1_order_feedback_post

    
    """
    params = [('id', 'id_example'),
                    ('key', 'key_example'),
                    ('format', 'format_example'),
                    ('action', 'action_example'),
                    ('notes', 'notes_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='POST',
        path='/v1/order/feedback',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_order_screen_post(client):
    """Test case for v1_order_screen_post

    
    """
    params = [('ip', 'ip_example'),
                    ('key', 'key_example'),
                    ('format', 'format_example'),
                    ('last_name', 'last_name_example'),
                    ('first_name', 'first_name_example'),
                    ('bill_addr', 'bill_addr_example'),
                    ('bill_city', 'bill_city_example'),
                    ('bill_state', 'bill_state_example'),
                    ('bill_country', 'bill_country_example'),
                    ('bill_zip_code', 'bill_zip_code_example'),
                    ('ship_addr', 'ship_addr_example'),
                    ('ship_city', 'ship_city_example'),
                    ('ship_state', 'ship_state_example'),
                    ('ship_country', 'ship_country_example'),
                    ('ship_zip_code', 'ship_zip_code_example'),
                    ('email_domain', 'email_domain_example'),
                    ('user_phone', 'user_phone_example'),
                    ('email', 'email_example'),
                    ('email_hash', 'email_hash_example'),
                    ('username_hash', 'username_hash_example'),
                    ('password_hash', 'password_hash_example'),
                    ('bin_no', 'bin_no_example'),
                    ('card_hash', 'card_hash_example'),
                    ('avs_result', 'avs_result_example'),
                    ('cvv_result', 'cvv_result_example'),
                    ('user_order_id', 'user_order_id_example'),
                    ('user_order_memo', 'user_order_memo_example'),
                    ('amount', 3.4),
                    ('quantity', 56),
                    ('currency', 'currency_example'),
                    ('department', 'department_example'),
                    ('payment_mode', 'payment_mode_example'),
                    ('flp_checksum', 'flp_checksum_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='POST',
        path='/v1/order/screen',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

