# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_status_request import ClientStatusRequest
from openapi_server.models.client_status_response import ClientStatusResponse


pytestmark = pytest.mark.asyncio

async def test_trafficdirector_discovery_client_status(client):
    """Test case for trafficdirector_discovery_client_status

    
    """
    body = {"nodeMatchers":[{"nodeMetadatas":[{"path":[{"key":"key"},{"key":"key"}],"value":{"presentMatch":True,"listMatch":{},"boolMatch":True,"nullMatch":"{}","stringMatch":{"regex":"regex","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}},"doubleMatch":{"exact":6.027456183070403,"range":{"start":5.962133916683182,"end":1.4658129805029452}}}},{"path":[{"key":"key"},{"key":"key"}],"value":{"presentMatch":True,"listMatch":{},"boolMatch":True,"nullMatch":"{}","stringMatch":{"regex":"regex","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}},"doubleMatch":{"exact":6.027456183070403,"range":{"start":5.962133916683182,"end":1.4658129805029452}}}}],"nodeId":{"regex":"regex","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}}},{"nodeMetadatas":[{"path":[{"key":"key"},{"key":"key"}],"value":{"presentMatch":True,"listMatch":{},"boolMatch":True,"nullMatch":"{}","stringMatch":{"regex":"regex","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}},"doubleMatch":{"exact":6.027456183070403,"range":{"start":5.962133916683182,"end":1.4658129805029452}}}},{"path":[{"key":"key"},{"key":"key"}],"value":{"presentMatch":True,"listMatch":{},"boolMatch":True,"nullMatch":"{}","stringMatch":{"regex":"regex","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}},"doubleMatch":{"exact":6.027456183070403,"range":{"start":5.962133916683182,"end":1.4658129805029452}}}}],"nodeId":{"regex":"regex","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}}}]}
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
        path='/v2/discovery:client_status',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

