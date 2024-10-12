# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ldap_service_info import LdapServiceInfo
from openapi_server.models.ldap_service_info_update import LdapServiceInfoUpdate
from openapi_server.models.ldap_service_summary import LdapServiceSummary
from openapi_server.models.ldap_service_summary_list_response import LdapServiceSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_create_ldap_service(client):
    """Test case for create_ldap_service

    Add a new authentication domain
    """
    body = {"bindUserPassword":"bindUserPassword","advancedOptions":{"userNameSearchAttribute":"userNameSearchAttribute","groupMembershipAttribute":"groupMembershipAttribute","userSearchFilter":"userSearchFilter","groupSearchFilter":"groupSearchFilter","groupMaxLevel":0,"groupMemberAttribute":"groupMemberAttribute"},"certificateId":"certificateId","name":"name","authServers":["authServers","authServers"],"mfaServerId":"mfaServerId","dynamicDnsName":"dynamicDnsName","baseDn":"baseDn","bindUserName":"bindUserName","isTotpEnforced":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/ldap_service',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ldap_service(client):
    """Test case for delete_ldap_service

    Delete an authentication domain for the given ID
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/ldap_service/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ldap_service(client):
    """Test case for get_ldap_service

    Get a LDAP service for the given ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ldap_service/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_ldap_service(client):
    """Test case for patch_ldap_service

    Update an existing authentication domain
    """
    body = {"bindUserPassword":"bindUserPassword","advancedOptions":{"userNameSearchAttribute":"userNameSearchAttribute","groupMembershipAttribute":"groupMembershipAttribute","userSearchFilter":"userSearchFilter","groupSearchFilter":"groupSearchFilter","groupMaxLevel":0,"groupMemberAttribute":"groupMemberAttribute"},"certificateId":"certificateId","name":"name","authServers":["authServers","authServers"],"mfaServerId":"mfaServerId","dynamicDnsName":"dynamicDnsName","baseDn":"baseDn","bindUserName":"bindUserName","isTotpEnforced":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/ldap_service/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_ldap_service(client):
    """Test case for put_ldap_service

    Replace the values of an authentication domain
    """
    body = {"bindUserPassword":"bindUserPassword","advancedOptions":{"userNameSearchAttribute":"userNameSearchAttribute","groupMembershipAttribute":"groupMembershipAttribute","userSearchFilter":"userSearchFilter","groupSearchFilter":"groupSearchFilter","groupMaxLevel":0,"groupMemberAttribute":"groupMemberAttribute"},"certificateId":"certificateId","name":"name","authServers":["authServers","authServers"],"mfaServerId":"mfaServerId","dynamicDnsName":"dynamicDnsName","baseDn":"baseDn","bindUserName":"bindUserName","isTotpEnforced":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/ldap_service/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_ldap_service(client):
    """Test case for query_ldap_service

    Get a list of LDAP services
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ldap_service',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

