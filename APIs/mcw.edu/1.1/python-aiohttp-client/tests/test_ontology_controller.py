# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.term import Term


pytestmark = pytest.mark.asyncio

async def test_get_ont_dags_using_get(client):
    """Test case for get_ont_dags_using_get

    Returns child and parent terms for Accession ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/ontology/ont/{acc_id}'.format(acc_id='acc_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_term_using_get(client):
    """Test case for get_term_using_get

    Returns term for Accession ID
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/ontology/term/{acc_id}'.format(acc_id='acc_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_is_descendant_of_using_get(client):
    """Test case for is_descendant_of_using_get

    Returns true or false for terms
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/ontology/term/{acc_id1}/{acc_id2}'.format(acc_id1='acc_id1_example', acc_id2='acc_id2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

