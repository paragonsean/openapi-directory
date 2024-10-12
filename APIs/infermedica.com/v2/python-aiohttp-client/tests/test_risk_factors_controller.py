# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.risk_factor_details import RiskFactorDetails
from openapi_server.models.risk_factor_public import RiskFactorPublic


pytestmark = pytest.mark.asyncio

async def test_get_all_risk_factors(client):
    """Test case for get_all_risk_factors

    List all risk factors
    """
    params = [('age.value', 18),
                    ('age.unit', year),
                    ('enable_triage_5', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/risk_factors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_risk_factor(client):
    """Test case for get_risk_factor

    Get risk factor by id
    """
    params = [('age.value', 18),
                    ('age.unit', year),
                    ('enable_triage_5', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/risk_factors/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

