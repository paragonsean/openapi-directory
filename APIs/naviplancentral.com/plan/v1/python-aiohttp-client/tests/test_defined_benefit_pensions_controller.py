# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.defined_benefit_pension_model import DefinedBenefitPensionModel
from openapi_server.models.defined_benefit_pensions_model import DefinedBenefitPensionsModel


pytestmark = pytest.mark.asyncio

async def test_defined_benefit_pensions_get_by_id_planid(client):
    """Test case for defined_benefit_pensions_get_by_id_planid

    Retrieve a definedBenefitPension
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/DefinedBenefitPensions/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_defined_benefit_pensions_get_by_planid(client):
    """Test case for defined_benefit_pensions_get_by_planid

    Retrieve defined benefit pensions
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/DefinedBenefitPensions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

