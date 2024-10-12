# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_sdf_download_task_request import CreateSdfDownloadTaskRequest
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_displayvideo_sdfdownloadtasks_create(client):
    """Test case for displayvideo_sdfdownloadtasks_create

    
    """
    body = {"inventorySourceFilter":{"inventorySourceIds":["inventorySourceIds","inventorySourceIds"]},"idFilter":{"insertionOrderIds":["insertionOrderIds","insertionOrderIds"],"adGroupAdIds":["adGroupAdIds","adGroupAdIds"],"mediaProductIds":["mediaProductIds","mediaProductIds"],"lineItemIds":["lineItemIds","lineItemIds"],"adGroupIds":["adGroupIds","adGroupIds"],"campaignIds":["campaignIds","campaignIds"]},"partnerId":"partnerId","parentEntityFilter":{"filterIds":["filterIds","filterIds"],"filterType":"FILTER_TYPE_UNSPECIFIED","fileType":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"]},"version":"SDF_VERSION_UNSPECIFIED","advertiserId":"advertiserId"}
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
        path='/v3/sdfdownloadtasks',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_displayvideo_sdfdownloadtasks_operations_get(client):
    """Test case for displayvideo_sdfdownloadtasks_operations_get

    
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
        path='/v3/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

