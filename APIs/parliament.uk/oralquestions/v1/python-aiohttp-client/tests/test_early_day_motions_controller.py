# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response_list_published_written_question import ApiResponseListPublishedWrittenQuestion
from openapi_server.models.api_response_object import ApiResponseObject


pytestmark = pytest.mark.asyncio

async def test_early_day_motions_list_get(client):
    """Test case for early_day_motions_list_get

    Returns a list of Early Day Motions
    """
    params = [('parameters.edmIds', [56]),
                    ('parameters.uINWithAmendmentSuffix', 'parameters_u_in_with_amendment_suffix_example'),
                    ('parameters.searchTerm', 'parameters_search_term_example'),
                    ('parameters.currentStatusDateStart', '2013-10-20T19:20:30+01:00'),
                    ('parameters.currentStatusDateEnd', '2013-10-20T19:20:30+01:00'),
                    ('parameters.isPrayer', True),
                    ('parameters.memberId', 56),
                    ('parameters.includeSponsoredByMember', True),
                    ('parameters.tabledStartDate', '2013-10-20T19:20:30+01:00'),
                    ('parameters.tabledEndDate', '2013-10-20T19:20:30+01:00'),
                    ('parameters.statuses', ['parameters_statuses_example']),
                    ('parameters.orderBy', 'parameters_order_by_example'),
                    ('parameters.skip', 56),
                    ('parameters.take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EarlyDayMotions/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_published_early_day_motion_get(client):
    """Test case for published_early_day_motion_get

    Returns a single Early Day Motion by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/EarlyDayMotion/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

