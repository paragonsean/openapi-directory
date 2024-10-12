# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advertising_branch_model import AdvertisingBranchModel
from openapi_server.models.advertising_branch_model_results import AdvertisingBranchModelResults


pytestmark = pytest.mark.asyncio

async def test_company_controller_get_branches(client):
    """Test case for company_controller_get_branches

    All branches defined for a company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/diary/{short_name}/company/branches'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_diary_short_name_company_branches_branch_idget(client):
    """Test case for v3_diary_short_name_company_branches_branch_idget

    Get a specific branch given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/diary/{short_name}/company/branches/{branch_id}'.format(short_name='short_name_example', branch_id='branch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

