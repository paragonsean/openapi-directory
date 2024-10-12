# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_info_for_observed_beacons_request import GetInfoForObservedBeaconsRequest
from openapi_server.models.get_info_for_observed_beacons_response import GetInfoForObservedBeaconsResponse


pytestmark = pytest.mark.asyncio

async def test_proximitybeacon_beaconinfo_getforobserved(client):
    """Test case for proximitybeacon_beaconinfo_getforobserved

    
    """
    body = {"namespacedTypes":["namespacedTypes","namespacedTypes"],"observations":[{"advertisedId":{"id":"id","type":"TYPE_UNSPECIFIED"},"telemetry":"telemetry","timestampMs":"timestampMs"},{"advertisedId":{"id":"id","type":"TYPE_UNSPECIFIED"},"telemetry":"telemetry","timestampMs":"timestampMs"}]}
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
        path='/v1beta1/beaconinfo:getforobserved',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

