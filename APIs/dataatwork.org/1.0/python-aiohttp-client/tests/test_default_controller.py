# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.job import Job
from openapi_server.models.job_related_jobs import JobRelatedJobs
from openapi_server.models.job_skills import JobSkills
from openapi_server.models.normalized_job import NormalizedJob
from openapi_server.models.normalized_skill import NormalizedSkill
from openapi_server.models.skill import Skill
from openapi_server.models.skill_jobs import SkillJobs
from openapi_server.models.skill_related_skills import SkillRelatedSkills


pytestmark = pytest.mark.asyncio

async def test_jobs_autocomplete_get(client):
    """Test case for jobs_autocomplete_get

    Job Title Autocomplete
    """
    params = [('begins_with', 'begins_with_example'),
                    ('contains', 'contains_example'),
                    ('ends_with', 'ends_with_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs/autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get(client):
    """Test case for jobs_get

    Job Titles and Descriptions
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_id_get(client):
    """Test case for jobs_id_get

    Job Title and Description
    """
    params = [('fips', 'fips_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_id_related_jobs_get(client):
    """Test case for jobs_id_related_jobs_get

    Jobs Associated with a Job
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs/{id}/related_jobs'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_id_related_skills_get(client):
    """Test case for jobs_id_related_skills_get

    Skills Associated with a Job
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs/{id}/related_skills'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_normalize_get(client):
    """Test case for jobs_normalize_get

    Job Title Normalization
    """
    params = [('job_title', 'job_title_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs/normalize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_unusual_titles_get(client):
    """Test case for jobs_unusual_titles_get

    Unusual Job Titles
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs/unusual_titles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skills_autocomplete_get(client):
    """Test case for skills_autocomplete_get

    Skill Name Autocomplete
    """
    params = [('begins_with', 'begins_with_example'),
                    ('contains', 'contains_example'),
                    ('ends_with', 'ends_with_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/skills/autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skills_get(client):
    """Test case for skills_get

    Skill Names and Descriptions
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/skills',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skills_id_get(client):
    """Test case for skills_id_get

    Skill Name and Description
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/skills/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skills_id_related_jobs_get(client):
    """Test case for skills_id_related_jobs_get

    Jobs Associated with a Skill
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/skills/{id}/related_jobs'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skills_id_related_skills_get(client):
    """Test case for skills_id_related_skills_get

    Skills Associated with a Skill
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/skills/{id}/related_skills'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skills_normalize_get(client):
    """Test case for skills_normalize_get

    Skill Name Normalization
    """
    params = [('skill_name', 'skill_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/skills/normalize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

