# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compare_input import CompareInput
from openapi_server.models.sim_result import SimResult
from openapi_server.models.sufficiency_output import SufficiencyOutput
from openapi_server.models.sufficiency_post_input import SufficiencyPostInput


pytestmark = pytest.mark.asyncio

async def test_get_annotation_score(client):
    """Test case for get_annotation_score

    Get annotation score
    """
    params = [('id', ['id_example']),
                    ('absent_id', [])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/sim/score',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sim_compare(client):
    """Test case for get_sim_compare

    Compare a reference profile vs one profiles
    """
    params = [('is_feature_set', True),
                    ('metric', phenodigm),
                    ('ref_id', []),
                    ('query_id', [])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/sim/compare',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sim_search(client):
    """Test case for get_sim_search

    Search for phenotypically similar diseases or model genes
    """
    params = [('is_feature_set', True),
                    ('metric', phenodigm),
                    ('id', []),
                    ('limit', 20),
                    ('taxon', 'taxon_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/sim/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_annotation_score(client):
    """Test case for post_annotation_score

    Get annotation score
    """
    body = {"features":[{"isPresent":True,"id":"id","label":"label","type":"type"},{"isPresent":True,"id":"id","label":"label","type":"type"}],"id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/sim/score',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_sim_compare(client):
    """Test case for post_sim_compare

    Compare a reference profile vs one or more profiles
    """
    body = {"query_ids":[["query_ids","query_ids"],["query_ids","query_ids"]],"reference_ids":["reference_ids","reference_ids"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/sim/compare',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

