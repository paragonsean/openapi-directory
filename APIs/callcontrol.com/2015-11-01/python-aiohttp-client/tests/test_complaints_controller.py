# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.complaints import Complaints


pytestmark = pytest.mark.asyncio

async def test_complaints_complaints(client):
    """Test case for complaints_complaints

    Complaints: Free service (with registration), providing community and government complaint lookup by phone number for up to 2,000 queries per month.  Details include number complaint rates from (FTC, FCC, IRS, Indiana Attorney  General) and key entity tag extractions from complaints.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/2015-11-01/Complaints/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

