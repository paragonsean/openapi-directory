# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filing_status_type_model import FilingStatusTypeModel
from openapi_server.models.filing_status_types_model import FilingStatusTypesModel


pytestmark = pytest.mark.asyncio

async def test_filing_status_types_get_by_country(client):
    """Test case for filing_status_types_get_by_country

    
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FilingStatusTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filing_status_types_get_by_id(client):
    """Test case for filing_status_types_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/FilingStatusTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

