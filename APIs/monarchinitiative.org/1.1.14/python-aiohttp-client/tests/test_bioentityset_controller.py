# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association_results import AssociationResults


pytestmark = pytest.mark.asyncio

async def test_get_entity_set_associations(client):
    """Test case for get_entity_set_associations

    Returns compact associations for a given input set
    """
    params = [('subject', ['subject_example']),
                    ('background', ['background_example']),
                    ('object_category', 'object_category_example'),
                    ('object_slim', 'object_slim_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/bioentityset/associations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_entity_set_graph_resource(client):
    """Test case for get_entity_set_graph_resource

    TODO Graph object spanning all entities
    """
    params = [('subject', ['subject_example']),
                    ('background', ['background_example']),
                    ('object_category', 'object_category_example'),
                    ('object_slim', 'object_slim_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentityset/graph',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_entity_set_summary(client):
    """Test case for get_entity_set_summary

    Summary statistics for objects associated
    """
    params = [('subject', ['subject_example']),
                    ('background', ['background_example']),
                    ('object_category', 'object_category_example'),
                    ('object_slim', 'object_slim_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentityset/descriptor/counts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_over_representation(client):
    """Test case for get_over_representation

    Summary statistics for objects associated
    """
    params = [('object_category', 'object_category_example'),
                    ('subject', ['subject_example']),
                    ('background', ['background_example']),
                    ('subject_category', 'gene'),
                    ('max_p_value', '0.05'),
                    ('ontology', 'ontology_example'),
                    ('taxon', 'taxon_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentityset/overrepresentation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

