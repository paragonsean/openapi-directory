# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_regulation_response import ListRegulationResponse
from openapi_server.models.numbers_v2_regulatory_compliance_regulation import NumbersV2RegulatoryComplianceRegulation
from openapi_server.models.regulation_enum_end_user_type import RegulationEnumEndUserType


pytestmark = pytest.mark.asyncio

async def test_fetch_regulation(client):
    """Test case for fetch_regulation

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/Regulations/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_regulation(client):
    """Test case for list_regulation

    
    """
    params = [('EndUserType', openapi_server.RegulationEnumEndUserType()),
                    ('IsoCountry', 'iso_country_example'),
                    ('NumberType', 'number_type_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/Regulations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

