# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call_report import CallReport
from openapi_server.models.reputation import Reputation


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_reputation_report(client):
    """Test case for reputation_report

    Report: report spam calls received to better tune our algorithms based upon spam calls you receive
    """
    call_report = {"Comment":"Comment","ReportedCallerId":"ReportedCallerId","ReportedCallerName":"ReportedCallerName","Reporter":"Reporter","UnwantedCall":True,"PhoneNumber":"PhoneNumber","IpAddress":"IpAddress","Latitude":0.8008281904610115,"CallTime":"2000-01-23T04:56:07.000+00:00","CallerType":"Unknown","Longitude":6.027456183070403}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/2015-11-01/Report',
        headers=headers,
        json=call_report,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reputation_reputation(client):
    """Test case for reputation_reputation

    Reputation:  Premium service which returns a reputation informaiton of a phone number via API.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/2015-11-01/Reputation/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

