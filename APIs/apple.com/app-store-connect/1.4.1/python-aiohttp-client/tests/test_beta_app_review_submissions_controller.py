# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beta_app_review_submission_create_request import BetaAppReviewSubmissionCreateRequest
from openapi_server.models.beta_app_review_submission_response import BetaAppReviewSubmissionResponse
from openapi_server.models.beta_app_review_submissions_response import BetaAppReviewSubmissionsResponse
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_beta_app_review_submissions_build_get_to_one_related(client):
    """Test case for beta_app_review_submissions_build_get_to_one_related

    
    """
    params = [('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppReviewSubmissions/{id}/build'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_review_submissions_create_instance(client):
    """Test case for beta_app_review_submissions_create_instance

    
    """
    body = {"data":{"relationships":{"build":{"data":{"id":"id","type":"builds"}}},"type":"betaAppReviewSubmissions"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaAppReviewSubmissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_review_submissions_get_collection(client):
    """Test case for beta_app_review_submissions_get_collection

    
    """
    params = [('filter[betaReviewState]', ['filter_beta_review_state_example']),
                    ('filter[build]', ['filter_build_example']),
                    ('fields[betaAppReviewSubmissions]', ['fields_beta_app_review_submissions_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppReviewSubmissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_app_review_submissions_get_instance(client):
    """Test case for beta_app_review_submissions_get_instance

    
    """
    params = [('fields[betaAppReviewSubmissions]', ['fields_beta_app_review_submissions_example']),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaAppReviewSubmissions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

