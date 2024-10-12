# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hybrid_use_benefit_list_result import HybridUseBenefitListResult


pytestmark = pytest.mark.asyncio

async def test_hybrid_use_benefit_revision_list(client):
    """Test case for hybrid_use_benefit_revision_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{plan_id}/revisions'.format(scope='scope_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

