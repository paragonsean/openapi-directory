# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.symptom_details import SymptomDetails
from openapi_server.models.symptom_public import SymptomPublic


pytestmark = pytest.mark.asyncio

async def test_get_all_symptoms(client):
    """Test case for get_all_symptoms

    List all symptoms
    """
    params = [('age.value', 18),
                    ('age.unit', year),
                    ('enable_triage_5', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/symptoms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_symptom(client):
    """Test case for get_symptom

    Get symptoms by id
    """
    params = [('age.value', 18),
                    ('age.unit', year),
                    ('enable_triage_5', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/symptoms/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

