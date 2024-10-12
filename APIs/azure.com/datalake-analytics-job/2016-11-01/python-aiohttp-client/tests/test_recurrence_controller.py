# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_recurrence_information import JobRecurrenceInformation
from openapi_server.models.job_recurrence_information_list_result import JobRecurrenceInformationListResult


pytestmark = pytest.mark.asyncio

async def test_recurrence_get(client):
    """Test case for recurrence_get

    
    """
    params = [('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recurrences/{recurrence_identity}'.format(recurrence_identity='recurrence_identity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recurrence_list(client):
    """Test case for recurrence_list

    
    """
    params = [('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/recurrences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

