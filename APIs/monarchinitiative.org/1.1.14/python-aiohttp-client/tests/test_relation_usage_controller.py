# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association_results import AssociationResults


pytestmark = pytest.mark.asyncio

async def test_get_relation_usage_between_resource(client):
    """Test case for get_relation_usage_between_resource

    All relations used plus count of associations
    """
    params = [('subject_taxon', 'subject_taxon_example'),
                    ('evidence', 'evidence_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/relation/usage/between/{subject_category}/{object_category}'.format(subject_category='subject_category_example', object_category='object_category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_relation_usage_pivot_label_resource(client):
    """Test case for get_relation_usage_pivot_label_resource

    Relation usage count for all subj x obj category combinations, showing label
    """
    params = [('subject_taxon', 'subject_taxon_example'),
                    ('evidence', 'evidence_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/relation/usage/pivot/label',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_relation_usage_pivot_resource(client):
    """Test case for get_relation_usage_pivot_resource

    Relation usage count for all subj x obj category combinations
    """
    params = [('subject_taxon', 'subject_taxon_example'),
                    ('evidence', 'evidence_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/relation/usage/pivot',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_relation_usage_resource(client):
    """Test case for get_relation_usage_resource

    All relations used plus count of associations
    """
    params = [('subject_taxon', 'subject_taxon_example'),
                    ('evidence', 'evidence_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/relation/usage/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

