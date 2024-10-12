# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill import Bill
from openapi_server.models.bill_sort_order import BillSortOrder
from openapi_server.models.bill_stage_details import BillStageDetails
from openapi_server.models.bill_summary_search_result import BillSummarySearchResult
from openapi_server.models.house import House
from openapi_server.models.originating_house import OriginatingHouse
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.stage_summary_search_result import StageSummarySearchResult


pytestmark = pytest.mark.asyncio

async def test_api_v1_bills_bill_id_stages_get(client):
    """Test case for api_v1_bills_bill_id_stages_get

    Returns all Bill stages.
    """
    params = [('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills/{bill_id}/Stages'.format(bill_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bill(client):
    """Test case for get_bill

    Return a Bill.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills/{bill_id}'.format(bill_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bill_stage_details(client):
    """Test case for get_bill_stage_details

    Returns a Bill stage.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills/{bill_id}/Stages/{bill_stage_id}'.format(bill_id=56, bill_stage_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bills(client):
    """Test case for get_bills

    Returns a list of Bills.
    """
    params = [('SearchTerm', 'search_term_example'),
                    ('Session', 56),
                    ('CurrentHouse', openapi_server.House()),
                    ('OriginatingHouse', openapi_server.OriginatingHouse()),
                    ('MemberId', 56),
                    ('DepartmentId', 56),
                    ('BillStage', [56]),
                    ('BillStagesExcluded', [56]),
                    ('IsDefeated', True),
                    ('IsWithdrawn', True),
                    ('BillType', [56]),
                    ('SortOrder', openapi_server.BillSortOrder()),
                    ('BillIds', [56]),
                    ('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

