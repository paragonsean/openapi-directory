# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis_archive_add_result import AnalysisArchiveAddResult
from openapi_server.models.analysis_archive_transition_rule import AnalysisArchiveTransitionRule
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.archive_summary import ArchiveSummary
from openapi_server.models.archived_analysis import ArchivedAnalysis


pytestmark = pytest.mark.asyncio

async def test_archive_image_analysis(client):
    """Test case for archive_image_analysis

    
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/archives/images',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_analysis_archive_rule(client):
    """Test case for create_analysis_archive_rule

    
    """
    body = {"max_images_per_account":1,"rule_id":"rule_id","last_updated":"2000-01-23T04:56:07.000+00:00","tag_versions_newer":5,"created_at":"2000-01-23T04:56:07.000+00:00","exclude":{"expiration_days":6,"selector":{"registry":"registry","tag":"tag","repository":"repository"}},"selector":{"registry":"registry","tag":"tag","repository":"repository"},"analysis_age_days":0,"system_global":True,"transition":"archive"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/archives/rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_analysis_archive_rule(client):
    """Test case for delete_analysis_archive_rule

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/archives/rules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_archived_analysis(client):
    """Test case for delete_archived_analysis

    
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/archives/images/{image_digest}'.format(image_digest='image_digest_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analysis_archive_rule(client):
    """Test case for get_analysis_archive_rule

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/archives/rules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_archived_analysis(client):
    """Test case for get_archived_analysis

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/archives/images/{image_digest}'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_analysis_archive(client):
    """Test case for list_analysis_archive

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/archives/images',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_analysis_archive_rules(client):
    """Test case for list_analysis_archive_rules

    
    """
    params = [('system_global', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/archives/rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_archives(client):
    """Test case for list_archives

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/archives',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

