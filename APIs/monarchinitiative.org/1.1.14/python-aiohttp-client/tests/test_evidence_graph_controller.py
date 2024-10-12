# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association_results import AssociationResults
from openapi_server.models.graph import Graph


pytestmark = pytest.mark.asyncio

async def test_get_evidence_graph_object(client):
    """Test case for get_evidence_graph_object

    Returns evidence graph object for a given association
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/evidence/graph/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_evidence_graph_table(client):
    """Test case for get_evidence_graph_table

    Returns evidence as a association_results object given an association
    """
    params = [('is_publication', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/evidence/graph/{id}/table'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

