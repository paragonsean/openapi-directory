# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_sm_apns_cert200_response import GetOrganizationSmApnsCert200Response


pytestmark = pytest.mark.asyncio

async def test_get_organization_sm_apns_cert_1(client):
    """Test case for get_organization_sm_apns_cert_1

    Get the organization's APNS certificate
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/sm/apnsCert'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

