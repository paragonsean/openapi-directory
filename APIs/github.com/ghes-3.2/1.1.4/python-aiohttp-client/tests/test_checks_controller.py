# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_annotation import CheckAnnotation
from openapi_server.models.check_run import CheckRun
from openapi_server.models.check_suite import CheckSuite
from openapi_server.models.check_suite_preference import CheckSuitePreference
from openapi_server.models.checks_create_request import ChecksCreateRequest
from openapi_server.models.checks_create_suite_request import ChecksCreateSuiteRequest
from openapi_server.models.checks_list_for_suite200_response import ChecksListForSuite200Response
from openapi_server.models.checks_list_suites_for_ref200_response import ChecksListSuitesForRef200Response
from openapi_server.models.checks_set_suites_preferences_request import ChecksSetSuitesPreferencesRequest
from openapi_server.models.checks_update_request import ChecksUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_checks_create(client):
    """Test case for checks_create

    Create a check run
    """
    body = {"actions":[{"description":"Allow us to fix these errors for you","identifier":"fix_errors","label":"Fix"}],"completed_at":"2017-11-30T19:49:10Z","conclusion":"success","head_sha":"ce587453ced02b1526dfb4cb910479d431683101","name":"mighty_readme","output":{"annotations":[{"annotation_level":"warning","end_line":2,"message":"Check your spelling for 'banaas'.","path":"README.md","raw_details":"Do you mean 'bananas' or 'banana'?","start_line":2,"title":"Spell Checker"},{"annotation_level":"warning","end_line":4,"message":"Check your spelling for 'aples'","path":"README.md","raw_details":"Do you mean 'apples' or 'Naples'","start_line":4,"title":"Spell Checker"}],"images":[{"alt":"Super bananas","image_url":"http://example.com/images/42"}],"summary":"There are 0 failures, 2 warnings, and 1 notices.","text":"You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.","title":"Mighty Readme report"},"started_at":"2017-11-30T19:39:10Z","status":"completed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/repos/{owner}/{repo}/check-runs'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_create_suite(client):
    """Test case for checks_create_suite

    Create a check suite
    """
    body = {"head_sha":"d6fde92930d4715a2b49857d24b940956b26d2d3"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/repos/{owner}/{repo}/check-suites'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_get(client):
    """Test case for checks_get

    Get a check run
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/check-runs/{check_run_id}'.format(owner='owner_example', repo='repo_example', check_run_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_get_suite(client):
    """Test case for checks_get_suite

    Get a check suite
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/check-suites/{check_suite_id}'.format(owner='owner_example', repo='repo_example', check_suite_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_list_annotations(client):
    """Test case for checks_list_annotations

    List check run annotations
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations'.format(owner='owner_example', repo='repo_example', check_run_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_list_for_ref(client):
    """Test case for checks_list_for_ref

    List check runs for a Git reference
    """
    params = [('check_name', 'check_name_example'),
                    ('status', 'status_example'),
                    ('filter', latest),
                    ('per_page', 30),
                    ('page', 1),
                    ('app_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/commits/{ref}/check-runs'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_list_for_suite(client):
    """Test case for checks_list_for_suite

    List check runs in a check suite
    """
    params = [('check_name', 'check_name_example'),
                    ('status', 'status_example'),
                    ('filter', latest),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs'.format(owner='owner_example', repo='repo_example', check_suite_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_list_suites_for_ref(client):
    """Test case for checks_list_suites_for_ref

    List check suites for a Git reference
    """
    params = [('app_id', 1),
                    ('check_name', 'check_name_example'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/repos/{owner}/{repo}/commits/{ref}/check-suites'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_rerequest_suite(client):
    """Test case for checks_rerequest_suite

    Rerequest a check suite
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest'.format(owner='owner_example', repo='repo_example', check_suite_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_set_suites_preferences(client):
    """Test case for checks_set_suites_preferences

    Update repository preferences for check suites
    """
    body = {"auto_trigger_checks":[{"app_id":4,"setting":false}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/repos/{owner}/{repo}/check-suites/preferences'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checks_update(client):
    """Test case for checks_update

    Update a check run
    """
    body = {"completed_at":"2018-05-04T01:14:52Z","conclusion":"success","name":"mighty_readme","output":{"annotations":[{"annotation_level":"warning","end_line":2,"message":"Check your spelling for 'banaas'.","path":"README.md","raw_details":"Do you mean 'bananas' or 'banana'?","start_line":2,"title":"Spell Checker"},{"annotation_level":"warning","end_line":4,"message":"Check your spelling for 'aples'","path":"README.md","raw_details":"Do you mean 'apples' or 'Naples'","start_line":4,"title":"Spell Checker"}],"images":[{"alt":"Super bananas","image_url":"http://example.com/images/42"}],"summary":"There are 0 failures, 2 warnings, and 1 notices.","text":"You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.","title":"Mighty Readme report"},"started_at":"2018-05-04T01:14:52Z","status":"completed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/repos/{owner}/{repo}/check-runs/{check_run_id}'.format(owner='owner_example', repo='repo_example', check_run_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

