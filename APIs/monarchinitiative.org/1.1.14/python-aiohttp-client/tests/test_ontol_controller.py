# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_extract_ontology_subgraph_resource(client):
    """Test case for get_extract_ontology_subgraph_resource

    Extract a subgraph from an ontology
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
        path='/api/ontol/subgraph/{ontology}/{node}'.format(node='node_example', ontology='ontology_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_information_content_resource(client):
    """Test case for get_information_content_resource

    Returns information content (IC) for a set of relevant ontology classes
    """
    params = [('evidence', 'evidence_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/ontol/information_content/{subject_category}/{object_category}/{subject_taxon}'.format(subject_category='subject_category_example', object_category='object_category_example', subject_taxon='subject_taxon_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_extract_ontology_subgraph_resource(client):
    """Test case for post_extract_ontology_subgraph_resource

    Extract a subgraph from an ontology
    """
    params = [('cnode', ['cnode_example']),
                    ('include_ancestors', True),
                    ('include_descendants', True),
                    ('relation', ["subClassOf","BFO:0000050"]),
                    ('include_meta', False)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/ontol/subgraph/{ontology}/{node}'.format(node='node_example', ontology='ontology_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

