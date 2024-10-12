# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inbox_upload_entity import InboxUploadEntity


pytestmark = pytest.mark.asyncio

async def test_get_inbox_uploads(client):
    """Test case for get_inbox_uploads

    List Inbox Uploads
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_lt', None),
                    ('filter_lteq', None),
                    ('inbox_registration_id', 56),
                    ('inbox_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/inbox_uploads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

