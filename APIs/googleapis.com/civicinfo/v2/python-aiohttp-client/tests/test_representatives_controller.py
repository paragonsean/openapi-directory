# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.representative_info_data import RepresentativeInfoData
from openapi_server.models.representative_info_response import RepresentativeInfoResponse


pytestmark = pytest.mark.asyncio

async def test_civicinfo_representatives_representative_info_by_address(client):
    """Test case for civicinfo_representatives_representative_info_by_address

    
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
                    ('address', 'address_example'),
                    ('includeOffices', True),
                    ('levels', ['levels_example']),
                    ('roles', ['roles_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/civicinfo/v2/representatives',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_civicinfo_representatives_representative_info_by_division(client):
    """Test case for civicinfo_representatives_representative_info_by_division

    
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
                    ('levels', ['levels_example']),
                    ('recursive', True),
                    ('roles', ['roles_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/civicinfo/v2/representatives/{ocd_id}'.format(ocd_id='ocd_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

