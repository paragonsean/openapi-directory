# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_factchecking_factchecktools_v1alpha1_fact_checked_claim_search_response import GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse


pytestmark = pytest.mark.asyncio

async def test_factchecktools_claims_search(client):
    """Test case for factchecktools_claims_search

    
    """
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
                    ('uploadType', 'upload_type_example'),
                    ('languageCode', 'language_code_example'),
                    ('maxAgeDays', 56),
                    ('offset', 56),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example'),
                    ('reviewPublisherSiteFilter', 'review_publisher_site_filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/claims:search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

