# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.budget import Budget


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_budget_get(client):
    """Test case for adexchangebuyer_budget_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.4/billinginfo/{account_id}/{billing_id}'.format(account_id='account_id_example', billing_id='billing_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_budget_patch(client):
    """Test case for adexchangebuyer_budget_patch

    
    """
    body = {"accountId":"accountId","billingId":"billingId","budgetAmount":"budgetAmount","kind":"adexchangebuyer#budget","id":"id","currencyCode":"currencyCode"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/adexchangebuyer/v1.4/billinginfo/{account_id}/{billing_id}'.format(account_id='account_id_example', billing_id='billing_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_budget_update(client):
    """Test case for adexchangebuyer_budget_update

    
    """
    body = {"accountId":"accountId","billingId":"billingId","budgetAmount":"budgetAmount","kind":"adexchangebuyer#budget","id":"id","currencyCode":"currencyCode"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/adexchangebuyer/v1.4/billinginfo/{account_id}/{billing_id}'.format(account_id='account_id_example', billing_id='billing_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

