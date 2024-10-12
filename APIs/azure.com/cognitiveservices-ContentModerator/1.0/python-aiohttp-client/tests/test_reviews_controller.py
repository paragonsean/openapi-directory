# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.frames import Frames
from openapi_server.models.job import Job
from openapi_server.models.job_id import JobId
from openapi_server.models.review import Review
from openapi_server.models.reviews_add_video_transcript_moderation_result_request_inner import ReviewsAddVideoTranscriptModerationResultRequestInner
from openapi_server.models.reviews_create_job_request import ReviewsCreateJobRequest
from openapi_server.models.reviews_create_reviews_request_inner import ReviewsCreateReviewsRequestInner


pytestmark = pytest.mark.asyncio

async def test_reviews_add_video_frame(client):
    """Test case for reviews_add_video_frame

    
    """
    params = [('timescale', 56)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/review/v1.0/teams/{team_name}/reviews/{review_id}/frames'.format(team_name='team_name_example', review_id='review_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_reviews_add_video_transcript(client):
    """Test case for reviews_add_video_transcript

    
    """
    vtt_file = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'content_type': 'content_type_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/contentmoderator/review/v1.0/teams/{team_name}/reviews/{review_id}/transcript'.format(team_name='team_name_example', review_id='review_id_example'),
        headers=headers,
        json=vtt_file,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_add_video_transcript_moderation_result(client):
    """Test case for reviews_add_video_transcript_moderation_result

    
    """
    transcript_moderation_body = [openapi_server.ReviewsAddVideoTranscriptModerationResultRequestInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/contentmoderator/review/v1.0/teams/{team_name}/reviews/{review_id}/transcriptmoderationresult'.format(team_name='team_name_example', review_id='review_id_example'),
        headers=headers,
        json=transcript_moderation_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_reviews_create_job(client):
    """Test case for reviews_create_job

    
    """
    content = openapi_server.ReviewsCreateJobRequest()
    params = [('ContentType', 'content_type_example'),
                    ('ContentId', 'content_id_example'),
                    ('WorkflowName', 'workflow_name_example'),
                    ('CallBackEndpoint', 'call_back_endpoint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type2': 'content_type_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/review/v1.0/teams/{team_name}/jobs'.format(team_name='team_name_example'),
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_create_reviews(client):
    """Test case for reviews_create_reviews

    
    """
    create_review_body = [openapi_server.ReviewsCreateReviewsRequestInner()]
    params = [('subTeam', 'sub_team_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'url_content_type': 'url_content_type_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/review/v1.0/teams/{team_name}/reviews'.format(team_name='team_name_example'),
        headers=headers,
        json=create_review_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_get_job_details(client):
    """Test case for reviews_get_job_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/contentmoderator/review/v1.0/teams/{team_name}/jobs/{job_id}'.format(team_name='team_name_example', job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_get_review(client):
    """Test case for reviews_get_review

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/contentmoderator/review/v1.0/teams/{team_name}/reviews/{review_id}'.format(team_name='team_name_example', review_id='review_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_get_video_frames(client):
    """Test case for reviews_get_video_frames

    
    """
    params = [('startSeed', 56),
                    ('noOfRecords', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/contentmoderator/review/v1.0/teams/{team_name}/reviews/{review_id}/frames'.format(team_name='team_name_example', review_id='review_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reviews_publish_video_review(client):
    """Test case for reviews_publish_video_review

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/review/v1.0/teams/{team_name}/reviews/{review_id}/publish'.format(team_name='team_name_example', review_id='review_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

