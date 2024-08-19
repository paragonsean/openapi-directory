# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.member_joining_rule import MemberJoiningRule
from openapi_server.models.member_joining_rule_request import MemberJoiningRuleRequest
from openapi_server.models.member_joining_rule_update import MemberJoiningRuleUpdate
from openapi_server.models.member_joining_rule_update_partial import MemberJoiningRuleUpdatePartial


pytestmark = pytest.mark.asyncio

async def test_member_joining_rules_create(client):
    """Test case for member_joining_rules_create

    
    """
    body = {"consuming_account":"2381982","managing_account":"238189294","network_service":"network_service","external_ref":"IX:Service:23042","capacity_min":1,"capacity_max":1,"type":"allow"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/member-joining-rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_member_joining_rules_destroy(client):
    """Test case for member_joining_rules_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/member-joining-rules/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_member_joining_rules_list(client):
    """Test case for member_joining_rules_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('network_service', 'network_service_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/member-joining-rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_member_joining_rules_partial_update(client):
    """Test case for member_joining_rules_partial_update

    
    """
    body = openapi_server.MemberJoiningRuleUpdatePartial()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/member-joining-rules/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_member_joining_rules_read(client):
    """Test case for member_joining_rules_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/member-joining-rules/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_member_joining_rules_update(client):
    """Test case for member_joining_rules_update

    
    """
    body = {"consuming_account":"2381982","managing_account":"238189294","external_ref":"IX:Service:23042","capacity_min":1,"capacity_max":1,"type":"allow"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/member-joining-rules/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

