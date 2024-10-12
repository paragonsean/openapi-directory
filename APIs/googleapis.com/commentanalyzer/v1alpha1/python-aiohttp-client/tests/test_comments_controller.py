# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analyze_comment_request import AnalyzeCommentRequest
from openapi_server.models.analyze_comment_response import AnalyzeCommentResponse
from openapi_server.models.suggest_comment_score_request import SuggestCommentScoreRequest
from openapi_server.models.suggest_comment_score_response import SuggestCommentScoreResponse


pytestmark = pytest.mark.asyncio

async def test_commentanalyzer_comments_analyze(client):
    """Test case for commentanalyzer_comments_analyze

    
    """
    body = {"spanAnnotations":True,"languages":["languages","languages"],"requestedAttributes":{"key":{"scoreThreshold":0.8008282,"scoreType":"SCORE_TYPE_UNSPECIFIED"}},"clientToken":"clientToken","context":{"entries":[{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"},{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"}],"articleAndParentComment":{"parentComment":{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"},"article":{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"}}},"comment":{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"},"sessionId":"sessionId","communityId":"communityId","doNotStore":True,"dropUnsupportedAttributes":True}
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
        path='/v1alpha1/comments:analyze',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commentanalyzer_comments_suggestscore(client):
    """Test case for commentanalyzer_comments_suggestscore

    
    """
    body = {"languages":["languages","languages"],"clientToken":"clientToken","attributeScores":{"key":{"summaryScore":{"type":"SCORE_TYPE_UNSPECIFIED","value":1.4658129},"spanScores":[{"score":{"type":"SCORE_TYPE_UNSPECIFIED","value":1.4658129},"end":6,"begin":0},{"score":{"type":"SCORE_TYPE_UNSPECIFIED","value":1.4658129},"end":6,"begin":0}]}},"context":{"entries":[{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"},{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"}],"articleAndParentComment":{"parentComment":{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"},"article":{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"}}},"comment":{"text":"text","type":"TEXT_TYPE_UNSPECIFIED"},"sessionId":"sessionId","communityId":"communityId"}
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
        path='/v1alpha1/comments:suggestscore',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

