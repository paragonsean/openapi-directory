# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_list_of_self_uploaded_documents500_response import GetListOfSelfUploadedDocuments500Response
from openapi_server.models.sample5 import Sample5
from openapi_server.models.upload_file_to_locker_id401_response import UploadFileToLockerId401Response


pytestmark = pytest.mark.asyncio

async def test_account_detail_api_id(client):
    """Test case for account_detail_api_id

    Get User Details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/public/oauth2/1/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

