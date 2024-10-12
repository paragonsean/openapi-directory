# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_sm_vpp_accounts200_response_inner import GetOrganizationSmVppAccounts200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_sm_vpp_account_1(client):
    """Test case for get_organization_sm_vpp_account_1

    Get a hash containing the unparsed token of the VPP account with the given ID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/sm/vppAccounts/{vpp_account_id}'.format(organization_id='organization_id_example', vpp_account_id='vpp_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_sm_vpp_accounts_1(client):
    """Test case for get_organization_sm_vpp_accounts_1

    List the VPP accounts in the organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/sm/vppAccounts'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

