# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.time_rule import TimeRule


pytestmark = pytest.mark.asyncio

async def test_time_rule_delete(client):
    """Test case for time_rule_delete

    Delete a Time Rule.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/timerules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_rule_get(client):
    """Test case for time_rule_get

    Retrieve a Time Rule.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/timerules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_rule_get_by_path(client):
    """Test case for time_rule_get_by_path

    Retrieve a Time Rule by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/timerules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_time_rule_update(client):
    """Test case for time_rule_update

    Update a Time Rule by replacing items in its definition.
    """
    time_rule = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement\\Analyses[MyAnalysis]\\TimeRule","ConfigString":"Frequency=300","Description":"Creates regular periodic time periods.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"MergeDuplicatedItems":False,"EditorType":"OSIsoft.AF.Time.TimeRule.PeriodicConfig","ConfigStringStored":"","Name":"Periodic","DisplayString":"Frequency=300","WebId":"I1TRXDqD5loBNH0erqeqJodtALAROsUFcWU5xGEQwAVXYTCAAROsUFcWU5xGEQwAVXYTCAA","Links":{"AnalysisTemplate":"AnalysisTemplate","Analysis":"Analysis","Self":"Self","PlugIn":"PlugIn"},"IsInitializing":False,"Id":"1514eb44-94c5-11e7-8443-00155d84c200","PlugInName":"Periodic","IsConfigured":True}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/timerules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=time_rule,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

