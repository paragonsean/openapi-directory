# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_api_docs(client):
    """Test case for get_api_docs

    Browse API documentation
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/docs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_swagger_ui(client):
    """Test case for get_api_swagger_ui

    Browse interactive API documentation
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/docs/swagger-ui',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_autocomplete(client):
    """Test case for get_autocomplete

    Get `autocomplete` objects.
    """
    params = [('q', 'q_example'),
                    ('size', 'size_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_disease_by_id(client):
    """Test case for get_disease_by_id

    Find information about a disease
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/disease/{disease}'.format(disease='disease_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_drug_by_id(client):
    """Test case for get_drug_by_id

    Get drug by ID
    """
    params = [('drug_id', 'drug_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/drug/{drug_id}'.format(drug_id2='drug_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ec_oby_id(client):
    """Test case for get_ec_oby_id

    Get evidence code by ID
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/eco/{eco_id}'.format(eco_id='eco_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quick_search(client):
    """Test case for get_quick_search

    Search most relevant results
    """
    params = [('q', 'q_example'),
                    ('size', 'size_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/quicksearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_relation_by_efoid(client):
    """Test case for get_relation_by_efoid

    Find related entities by disease
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/relation/disease/{disease}'.format(disease='disease_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_relation_by_ensgid(client):
    """Test case for get_relation_by_ensgid

    Find related entities by target
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/relation/target/{target}'.format(target='target_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_swagger(client):
    """Test case for get_swagger

    Get OpenAPI schema
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/swagger',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_target_by_ensgid(client):
    """Test case for get_target_by_ensgid

    Find information about a target
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/target/{target}'.format(target='target_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_target_expression_by_ensgid(client):
    """Test case for get_target_expression_by_ensgid

    Query expression levels
    """
    params = [('gene', 'gene_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/private/target/expression',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_best_hit_search(client):
    """Test case for post_best_hit_search

    Find the best hit
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/private/besthitsearch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_disease_by_id(client):
    """Test case for post_disease_by_id

    Find information about a list of diseases
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/private/disease',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_enrichment_target(client):
    """Test case for post_enrichment_target

    Enrichment analysis
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/private/enrichment/targets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_relation(client):
    """Test case for post_relation

    Find related entities
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/private/relation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_target_by_ensgid(client):
    """Test case for post_target_by_ensgid

    Find information about a list of targets
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/private/target',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_target_expression_by_ensgid(client):
    """Test case for post_target_expression_by_ensgid

    Batch query expression levels
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/private/target/expression',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

