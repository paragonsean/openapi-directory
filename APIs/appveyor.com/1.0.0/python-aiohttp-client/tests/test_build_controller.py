# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_model import ArtifactModel
from openapi_server.models.build import Build
from openapi_server.models.build_start_request import BuildStartRequest
from openapi_server.models.error import Error
from openapi_server.models.re_run_build_request import ReRunBuildRequest


pytestmark = pytest.mark.asyncio

async def test_cancel_build(client):
    """Test case for cancel_build

    Cancel build
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/builds/{account_name}/{project_slug}/{build_version}'.format(account_name='account_name_example', project_slug='project_slug_example', build_version='build_version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_build_artifact(client):
    """Test case for get_build_artifact

    Download build artifact
    """
    headers = { 
        'Accept': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/buildjobs/{job_id}/artifacts/{artifact_file_name}'.format(job_id='job_id_example', artifact_file_name='artifact_file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_build_artifacts(client):
    """Test case for get_build_artifacts

    Get build artifacts
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/buildjobs/{job_id}/artifacts'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_build_log(client):
    """Test case for get_build_log

    Download build log
    """
    headers = { 
        'Accept': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/buildjobs/{job_id}/log'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_re_run_build(client):
    """Test case for re_run_build

    Re-run build
    """
    body = {"buildId":23864,"reRunIncomplete":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/builds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_build(client):
    """Test case for start_build

    Start build of branch most recent commit
    """
    body = {"accountName":"your-account-name","branch":"master","environmentVariables":{"another_var":"another value","my_var":"value"},"projectSlug":"project-slug-from-url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/builds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

