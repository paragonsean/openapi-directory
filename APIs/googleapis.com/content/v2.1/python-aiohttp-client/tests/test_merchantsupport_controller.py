# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.render_account_issues_request_payload import RenderAccountIssuesRequestPayload
from openapi_server.models.render_account_issues_response import RenderAccountIssuesResponse
from openapi_server.models.render_product_issues_request_payload import RenderProductIssuesRequestPayload
from openapi_server.models.render_product_issues_response import RenderProductIssuesResponse


pytestmark = pytest.mark.asyncio

async def test_content_merchantsupport_renderaccountissues(client):
    """Test case for content_merchantsupport_renderaccountissues

    
    """
    body = {"contentOption":"CONTENT_OPTION_UNSPECIFIED"}
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
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/merchantsupport/renderaccountissues'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_merchantsupport_renderproductissues(client):
    """Test case for content_merchantsupport_renderproductissues

    
    """
    body = {"contentOption":"CONTENT_OPTION_UNSPECIFIED"}
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
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/merchantsupport/renderproductissues/{product_id}'.format(merchant_id='merchant_id_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

