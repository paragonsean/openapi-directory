# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.acme_challenge_set import AcmeChallengeSet
from openapi_server.models.rotate_challenges_request import RotateChallengesRequest


pytestmark = pytest.mark.asyncio

async def test_acmedns_acme_challenge_sets_get(client):
    """Test case for acmedns_acme_challenge_sets_get

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/acmeChallengeSets/{root_domain}'.format(root_domain='root_domain_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_acmedns_acme_challenge_sets_rotate_challenges(client):
    """Test case for acmedns_acme_challenge_sets_rotate_challenges

    
    """
    body = {"recordsToRemove":[{"fqdn":"fqdn","digest":"digest","updateTime":"updateTime"},{"fqdn":"fqdn","digest":"digest","updateTime":"updateTime"}],"keepExpiredRecords":True,"recordsToAdd":[{"fqdn":"fqdn","digest":"digest","updateTime":"updateTime"},{"fqdn":"fqdn","digest":"digest","updateTime":"updateTime"}],"accessToken":"accessToken"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/acmeChallengeSets/{root_domainrotate_challenge}'.format(root_domain='root_domain_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

