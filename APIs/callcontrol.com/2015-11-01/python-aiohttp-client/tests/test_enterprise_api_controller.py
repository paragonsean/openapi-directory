# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call_control_user import CallControlUser


pytestmark = pytest.mark.asyncio

async def test_enterprise_api_get_user(client):
    """Test case for enterprise_api_get_user

    Enterprise  GET: GetUser  Returns the current information from the user;  try 12066194123 as demo
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/2015-11-01/Enterprise/GetUser/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_api_should_block(client):
    """Test case for enterprise_api_should_block

    Enterprise  GET: ShouldBlock  Simple Enteprise which returns a call block proceed decision.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/2015-11-01/Enterprise/ShouldBlock/{phone_number}/{user_phone_number}'.format(phone_number='phone_number_example', user_phone_number='user_phone_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_enterprise_api_upsert_user(client):
    """Test case for enterprise_api_upsert_user

    UpsertUser: insert or update all properties from a user  PhoneNumber  WhiteList (list of phone numbers to whitelist)  BlackList (list of phone numbers to blacklist)  QuietHourList (list of quiet hour objects)  UseCommunityBlacklist (enable / disable community blacklist) default true  BreakThroughQhWithMultipleCalls (break through quiet hours with two calls in 3 minutes)  WhiteListBreaksQh (break through quiet hours for whitelist)
    """
    user = {"Email":"Email","FirstName":"FirstName","WhiteList":["WhiteList","WhiteList"],"BlackList":["BlackList","BlackList"],"Gender":"Gender","MiddleName":"MiddleName","UseCommunityBlacklist":True,"Salutation":"Salutation","PhoneNumbeRegion":"PhoneNumbeRegion","BlockBehavior":"allow","Suffix":"Suffix","BreakThroughQhWithMultipleCalls":True,"PhoneNumber":"PhoneNumber","LastName":"LastName","Age":0,"QuietHourList":[{"StartMinLocal":5,"DayOfWeekList":["Sunday","Sunday"],"DurationMin":6,"TimeZoneName":"TimeZoneName","StartHourLocal":1},{"StartMinLocal":5,"DayOfWeekList":["Sunday","Sunday"],"DurationMin":6,"TimeZoneName":"TimeZoneName","StartHourLocal":1}],"WhiteListBreaksQh":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/2015-11-01/Enterprise/UpsertUser',
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

