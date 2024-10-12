# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.amendment_detail import AmendmentDetail
from openapi_server.models.amendment_search_item_search_result import AmendmentSearchItemSearchResult
from openapi_server.models.decision import Decision
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_amendment(client):
    """Test case for get_amendment

    Returns an amendment.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills/{bill_id}/Stages/{bill_stage_id}/Amendments/{amendment_id}'.format(bill_id=56, bill_stage_id=56, amendment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_amendments(client):
    """Test case for get_amendments

    Returns a list of amendments.
    """
    params = [('SearchTerm', 'search_term_example'),
                    ('Decision', openapi_server.Decision()),
                    ('MemberId', 56),
                    ('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills/{bill_id}/Stages/{bill_stage_id}/Amendments'.format(bill_id=56, bill_stage_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

