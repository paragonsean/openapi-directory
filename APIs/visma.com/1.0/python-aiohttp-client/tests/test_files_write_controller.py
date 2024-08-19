# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.file_keyword_model import FileKeywordModel


pytestmark = pytest.mark.asyncio

async def test_keywords_link_keyword_to_file(client):
    """Test case for keywords_link_keyword_to_file

    Link existing keyword to file
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/files/{file_guid}/keywords/{guid}'.format(file_guid='file_guid_example', guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

