# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_request import AccountRequest
from openapi_server.models.account_update import AccountUpdate
from openapi_server.models.account_update_partial import AccountUpdatePartial
from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response


pytestmark = pytest.mark.asyncio

async def test_accounts_create(client):
    """Test case for accounts_create

    
    """
    body = {"billing_information":{"address":{"country":"US","street_address":"1600 Amphitheatre Pkwy.","post_office_box_number":"2335232","locality":"Mountain View","postal_code":"9409","region":"CA"},"vat_number":"UK2300000042","name":"Moonoc Network Services LLS."},"managing_account":"IX:Account:231","metro_area_network_presence":["14021","12939"],"address":{"country":"US","street_address":"1600 Amphitheatre Pkwy.","post_office_box_number":"2335232","locality":"Mountain View","postal_code":"9409","region":"CA"},"discoverable":False,"external_ref":"IX:Service:23042","name":"Moonpeer Inc.","legal_name":"Moon Network Services LLS."}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_destroy(client):
    """Test case for accounts_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/accounts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_list(client):
    """Test case for accounts_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('state', 'state_example'),
                    ('state__is_not', 'state__is_not_example'),
                    ('managing_account', 'managing_account_example'),
                    ('billable', 56),
                    ('external_ref', 'external_ref_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_partial_update(client):
    """Test case for accounts_partial_update

    
    """
    body = openapi_server.AccountUpdatePartial()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/accounts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_read(client):
    """Test case for accounts_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/accounts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_update(client):
    """Test case for accounts_update

    
    """
    body = {"billing_information":{"address":{"country":"US","street_address":"1600 Amphitheatre Pkwy.","post_office_box_number":"2335232","locality":"Mountain View","postal_code":"9409","region":"CA"},"vat_number":"UK2300000042","name":"Moonoc Network Services LLS."},"managing_account":"IX:Account:231","metro_area_network_presence":["14021","12939"],"address":{"country":"US","street_address":"1600 Amphitheatre Pkwy.","post_office_box_number":"2335232","locality":"Mountain View","postal_code":"9409","region":"CA"},"discoverable":False,"external_ref":"IX:Service:23042","name":"Moonpeer Inc.","legal_name":"Moon Network Services LLS."}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/accounts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

