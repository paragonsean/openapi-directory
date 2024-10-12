# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.paginated_response_of_change_log_entry import PaginatedResponseOfChangeLogEntry


pytestmark = pytest.mark.asyncio

async def test_list_organization_change_log(client):
    """Test case for list_organization_change_log

    List change log entries of an organization
    """
    params = [('messageMimeType', 'text/mustache'),
                    ('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/changelog/organization/{organization_id}'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

