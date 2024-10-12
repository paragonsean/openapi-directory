# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association_results import AssociationResults


pytestmark = pytest.mark.asyncio

async def test_get_entity_set_homologs(client):
    """Test case for get_entity_set_homologs

    Returns homology associations for a given input set of genes
    """
    params = [('subject', ['subject_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentityset/homologs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

