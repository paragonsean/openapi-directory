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
    body = {"node":{"cluster":"cluster","extensions":[{"name":"name","disabled":True,"category":"category","version":{"metadata":{"key":""},"version":{"patch":1,"majorNumber":0,"minorNumber":6}},"typeUrls":["typeUrls","typeUrls"],"typeDescriptor":"typeDescriptor"},{"name":"name","disabled":True,"category":"category","version":{"metadata":{"key":""},"version":{"patch":1,"majorNumber":0,"minorNumber":6}},"typeUrls":["typeUrls","typeUrls"],"typeDescriptor":"typeDescriptor"}],"metadata":{"key":""},"clientFeatures":["clientFeatures","clientFeatures"],"userAgentVersion":"userAgentVersion","dynamicParameters":{"key":{"params":{"key":"params"}}},"locality":{"zone":"zone","region":"region","subZone":"subZone"},"userAgentBuildVersion":{"metadata":{"key":""},"version":{"patch":1,"majorNumber":0,"minorNumber":6}},"id":"id","userAgentName":"userAgentName","listeningAddresses":[{"pipe":{"mode":5,"path":"path"},"envoyInternalAddress":{"serverListenerName":"serverListenerName","endpointId":"endpointId"},"socketAddress":{"protocol":"TCP","resolverName":"resolverName","address":"address","ipv4Compat":True,"portValue":5,"namedPort":"namedPort"}},{"pipe":{"mode":5,"path":"path"},"envoyInternalAddress":{"serverListenerName":"serverListenerName","endpointId":"endpointId"},"socketAddress":{"protocol":"TCP","resolverName":"resolverName","address":"address","ipv4Compat":True,"portValue":5,"namedPort":"namedPort"}}]},"excludeResourceContents":True,"nodeMatchers":[{"nodeMetadatas":[{"path":[{"key":"key"},{"key":"key"}],"value":{"presentMatch":True,"listMatch":{},"boolMatch":True,"orMatch":{"valueMatchers":[null,null]},"nullMatch":"{}","stringMatch":{"contains":"contains","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}},"doubleMatch":{"exact":6.027456183070403,"range":{"start":5.962133916683182,"end":1.4658129805029452}}}},{"path":[{"key":"key"},{"key":"key"}],"value":{"presentMatch":True,"listMatch":{},"boolMatch":True,"orMatch":{"valueMatchers":[null,null]},"nullMatch":"{}","stringMatch":{"contains":"contains","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}},"doubleMatch":{"exact":6.027456183070403,"range":{"start":5.962133916683182,"end":1.4658129805029452}}}}],"nodeId":{"contains":"contains","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}}},{"nodeMetadatas":[{"path":[{"key":"key"},{"key":"key"}],"value":{"presentMatch":True,"listMatch":{},"boolMatch":True,"orMatch":{"valueMatchers":[null,null]},"nullMatch":"{}","stringMatch":{"contains":"contains","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}},"doubleMatch":{"exact":6.027456183070403,"range":{"start":5.962133916683182,"end":1.4658129805029452}}}},{"path":[{"key":"key"},{"key":"key"}],"value":{"presentMatch":True,"listMatch":{},"boolMatch":True,"orMatch":{"valueMatchers":[null,null]},"nullMatch":"{}","stringMatch":{"contains":"contains","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}},"doubleMatch":{"exact":6.027456183070403,"range":{"start":5.962133916683182,"end":1.4658129805029452}}}}],"nodeId":{"contains":"contains","ignoreCase":True,"prefix":"prefix","exact":"exact","suffix":"suffix","safeRegex":{"regex":"regex","googleRe2":{"maxProgramSize":0}}}}]}
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
        path='/v3/discovery:client_status',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

