# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deployed_branch import DeployedBranch
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_list_site_deployed_branches(client):
    """Test case for list_site_deployed_branches

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/deployed-branches'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

