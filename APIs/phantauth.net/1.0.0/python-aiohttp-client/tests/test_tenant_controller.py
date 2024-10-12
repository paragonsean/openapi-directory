# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tenant_tenantname_get200_response import TenantTenantnameGet200Response


pytestmark = pytest.mark.asyncio

async def test_tenant_tenantname_get(client):
    """Test case for tenant_tenantname_get

    Get a Tenant
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/tenant/{tenantname}'.format(tenantname='tenantname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

