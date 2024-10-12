# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_in_request import CheckInRequest
from openapi_server.models.check_in_response import CheckInResponse


pytestmark = pytest.mark.asyncio

async def test_genomics_workers_check_in(client):
    """Test case for genomics_workers_check_in

    
    """
    body = {"result":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"deadlineExpired":"{}","sosReport":"sosReport","workerStatus":{"totalRamBytes":"totalRamBytes","attachedDisks":{"key":{"freeSpaceBytes":"freeSpaceBytes","totalSpaceBytes":"totalSpaceBytes"}},"freeRamBytes":"freeRamBytes","bootDisk":{"freeSpaceBytes":"freeSpaceBytes","totalSpaceBytes":"totalSpaceBytes"},"uptimeSeconds":"uptimeSeconds"},"event":{"key":""},"events":[{"data":{"key":""},"timestamp":"timestamp"},{"data":{"key":""},"timestamp":"timestamp"}]}
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
        path='/v2alpha1/workers/{idcheck_i}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

