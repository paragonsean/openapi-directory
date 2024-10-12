# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit_candidate_search_list import AuditCandidateSearchList
from openapi_server.models.audit_case_page import AuditCasePage
from openapi_server.models.audit_category_page import AuditCategoryPage
from openapi_server.models.audit_committee_search_list import AuditCommitteeSearchList
from openapi_server.models.audit_primary_category_page import AuditPrimaryCategoryPage


pytestmark = pytest.mark.asyncio

async def test_audit_case_get(client):
    """Test case for audit_case_get

    
    """
    params = [('max_election_cycle', 56),
                    ('q', ['q_example']),
                    ('sub_category_id', 'all'),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('audit_case_id', ['audit_case_id_example']),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('qq', ['qq_example']),
                    ('per_page', 20),
                    ('sort', ["-cycle","committee_name"]),
                    ('min_election_cycle', 56),
                    ('audit_id', [56]),
                    ('committee_designation', 'committee_designation_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('committee_type', ['committee_type_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('primary_category_id', 'all')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audit-case/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_audit_category_get(client):
    """Test case for audit_category_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('primary_category_id', ['primary_category_id_example']),
                    ('sort', 'primary_category_name'),
                    ('primary_category_name', ['primary_category_name_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audit-category/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_audit_primary_category_get(client):
    """Test case for audit_primary_category_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('primary_category_id', ['primary_category_id_example']),
                    ('sort', 'primary_category_name'),
                    ('primary_category_name', ['primary_category_name_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audit-primary-category/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_audit_candidates_get(client):
    """Test case for names_audit_candidates_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('q', ['q_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/names/audit_candidates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_audit_committees_get(client):
    """Test case for names_audit_committees_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('q', ['q_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/names/audit_committees/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

