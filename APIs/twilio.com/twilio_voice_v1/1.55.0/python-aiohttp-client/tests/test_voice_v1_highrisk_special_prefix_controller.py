# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_dialing_permissions_hrs_prefixes_response import ListDialingPermissionsHrsPrefixesResponse


pytestmark = pytest.mark.asyncio

async def test_list_dialing_permissions_hrs_prefixes(client):
    """Test case for list_dialing_permissions_hrs_prefixes

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/DialingPermissions/Countries/{iso_code}/HighRiskSpecialPrefixes'.format(iso_code='iso_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

