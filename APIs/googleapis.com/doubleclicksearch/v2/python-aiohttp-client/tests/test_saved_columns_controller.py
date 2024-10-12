# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.saved_column_list import SavedColumnList


pytestmark = pytest.mark.asyncio

async def test_doubleclicksearch_saved_columns_list(client):
    """Test case for doubleclicksearch_saved_columns_list

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/doubleclicksearch/v2/agency/{agency_id}/advertiser/{advertiser_id}/savedcolumns'.format(agency_id='agency_id_example', advertiser_id='advertiser_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

