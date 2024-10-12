# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_ontology_subset(client):
    """Test case for get_ontology_subset

    Returns meta data of an ontology subset (slim)
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/ontology/subset/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ontology_term(client):
    """Test case for get_ontology_term

    Returns meta data of an ontology term
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/ontology/term/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ontology_term_graph(client):
    """Test case for get_ontology_term_graph

    Returns graph of an ontology term
    """
    params = [('graph_type', topology_graph)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/ontology/term/{id}/graph'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ontology_term_subgraph(client):
    """Test case for get_ontology_term_subgraph

    Extract a subgraph from an ontology term
    """
    params = [('cnode', ['cnode_example']),
                    ('include_ancestors', True),
                    ('include_descendants', True),
                    ('relation', ["subClassOf","BFO:0000050"]),
                    ('include_meta', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/ontology/term/{id}/subgraph'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ontology_term_subsets(client):
    """Test case for get_ontology_term_subsets

    Returns subsets (slims) associated to an ontology term
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/ontology/term/{id}/subsets'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ontology_terms_shared_ancestor(client):
    """Test case for get_ontology_terms_shared_ancestor

    Returns the ancestor ontology terms shared by two ontology terms
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/ontology/shared/{subject}/{object}'.format(subject='subject_example', object='object_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

