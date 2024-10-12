# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association_results import AssociationResults


pytestmark = pytest.mark.asyncio

async def test_get_association_by_subject_and_assoc_type(client):
    """Test case for get_association_by_subject_and_assoc_type

    Returns list of matching associations of a given type
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('evidence', 'evidence_example'),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('use_compact_associations', False),
                    ('subject', 'subject_example'),
                    ('object', 'object_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/association/type/{association_type}'.format(association_type='association_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_association_by_subject_and_object_category_search(client):
    """Test case for get_association_by_subject_and_object_category_search

    Returns list of matching associations between a given subject and object category
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('evidence', 'evidence_example'),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('use_compact_associations', False),
                    ('subject', 'subject_example'),
                    ('object', 'object_example'),
                    ('subject_taxon', 'subject_taxon_example'),
                    ('object_taxon', 'object_taxon_example'),
                    ('relation', 'relation_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/association/find/{subject_category}/{object_category}'.format(object_category='object_category_example', subject_category='subject_category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_association_by_subject_category_search(client):
    """Test case for get_association_by_subject_category_search

    Returns list of matching associations for a given subject category
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('evidence', 'evidence_example'),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('use_compact_associations', False),
                    ('subject_taxon', 'subject_taxon_example'),
                    ('object_taxon', 'object_taxon_example'),
                    ('relation', 'relation_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/association/find/{subject_category}'.format(subject_category='subject_category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_association_object(client):
    """Test case for get_association_object

    Returns the association with a given identifier
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/association/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_associations_between(client):
    """Test case for get_associations_between

    Returns associations connecting two entities
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('evidence', 'evidence_example'),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('use_compact_associations', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/association/between/{subject}/{object}'.format(object='object_example', subject='subject_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_associations_from(client):
    """Test case for get_associations_from

    Returns list of matching associations starting from a given subject (source)
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('evidence', 'evidence_example'),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('use_compact_associations', False),
                    ('object_taxon', 'object_taxon_example'),
                    ('relation', 'relation_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/association/from/{subject}'.format(subject='subject_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_associations_to(client):
    """Test case for get_associations_to

    Returns list of matching associations pointing to a given object (target)
    """
    params = [('rows', 100),
                    ('start', 56),
                    ('evidence', 'evidence_example'),
                    ('unselect_evidence', False),
                    ('exclude_automatic_assertions', False),
                    ('use_compact_associations', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/association/to/{object}'.format(object='object_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

