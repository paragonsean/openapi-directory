# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.upload_private_data_request import UploadPrivateDataRequest
from openapi_server.models.upload_private_data_response import UploadPrivateDataResponse


pytestmark = pytest.mark.asyncio

async def test_walletobjects_walletobjects_v1_private_content_upload_private_data(client):
    """Test case for walletobjects_walletobjects_v1_private_content_upload_private_data

    
    """
    body = {"issuerId":"issuerId","text":{"header":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"body":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]}},"uri":{"description":{"defaultValue":{"kind":"kind","language":"language","value":"value"},"kind":"kind","translatedValues":[{"kind":"kind","language":"language","value":"value"},{"kind":"kind","language":"language","value":"value"}]},"uri":"uri"}}
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
        path='/walletobjects/v1/privateContent/uploadPrivateData',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

