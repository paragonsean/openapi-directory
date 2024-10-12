# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_personalized_ranking_request import GetPersonalizedRankingRequest
from openapi_server.models.get_personalized_ranking_response import GetPersonalizedRankingResponse
from openapi_server.models.get_recommendations_request import GetRecommendationsRequest
from openapi_server.models.get_recommendations_response import GetRecommendationsResponse


pytestmark = pytest.mark.asyncio

async def test_get_personalized_ranking(client):
    """Test case for get_personalized_ranking

    
    """
    body = {"filterValues":"","inputList":"","filterArn":"","context":"","userId":"","campaignArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/personalize-ranking',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recommendations(client):
    """Test case for get_recommendations

    
    """
    body = {"filterValues":"","itemId":"","promotions":"","filterArn":"","recommenderArn":"","context":"","numResults":"","userId":"","campaignArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/recommendations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

