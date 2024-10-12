# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branch_model import BranchModel
from openapi_server.models.branch_model_results import BranchModelResults


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_branch_branches_branch_idget(client):
    """Test case for v2_tier1_short_name_branch_branches_branch_idget

    Get a specific branch given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/branch/branches/{branch_id}'.format(short_name='short_name_example', branch_id='branch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_branch_branches_get(client):
    """Test case for v2_tier1_short_name_branch_branches_get

    All branches defined for a company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/branch/branches'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

