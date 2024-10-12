# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_videointelligence_v1p2beta1_annotate_video_request import GoogleCloudVideointelligenceV1p2beta1AnnotateVideoRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_videointelligence_videos_annotate(client):
    """Test case for videointelligence_videos_annotate

    
    """
    body = openapi_server.GoogleCloudVideointelligenceV1p2beta1AnnotateVideoRequest()
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1p2beta1/videos:annotate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

