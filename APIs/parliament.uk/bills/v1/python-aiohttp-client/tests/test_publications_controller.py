# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill_publication_list import BillPublicationList
from openapi_server.models.bill_stage_publication_list import BillStagePublicationList
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_api_v1_bills_bill_id_stages_stage_id_publications_get(client):
    """Test case for api_v1_bills_bill_id_stages_stage_id_publications_get

    Return a list of Bill stage publications.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills/{bill_id}/Stages/{stage_id}/Publications'.format(bill_id=56, stage_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bill_publication(client):
    """Test case for get_bill_publication

    Return a list of Bill publications.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills/{bill_id}/Publications'.format(bill_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

