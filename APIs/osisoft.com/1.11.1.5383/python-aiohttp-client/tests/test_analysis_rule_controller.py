# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis_rule import AnalysisRule
from openapi_server.models.items_analysis_rule import ItemsAnalysisRule


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_rule_create_analysis_rule(client):
    """Test case for analysis_rule_create_analysis_rule

    Create a new Analysis Rule as a child of an existing Analysis Rule.
    """
    analysis_rule = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement\\Analyses[MyAnalysis]\\AnalysisRule","ConfigString":"a := TagVal('sinusoid'); b := Pow(a, 2); c := a + b;","Description":"Runs a performance equation.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"VariableMapping":"b||Attribute1;c||Attribute2","EditorType":"OSIsoft.AF.Analysis.AnalysisRule.PEAnalysisRuleEditor","Name":"PerformanceEquation","HasChildren":False,"DisplayString":"a := TagVal('sinusoid'); b := Pow(a, 2); c := a + b;","SupportedBehaviors":["SupportsRunningCase","SupportStatePassing","OutputCorrectAfterSkipping"],"WebId":"I1XRXDqD5loBNH0erqeqJodtALAfyWdysKU5xGEQwAVXYTCAAfyWdysKU5xGEQwAVXYTCAA","Links":{"AnalysisTemplate":"AnalysisTemplate","Parent":"Parent","Analysis":"Analysis","AnalysisRules":"AnalysisRules","Self":"Self","PlugIn":"PlugIn"},"IsInitializing":False,"Id":"ca9d257f-94c2-11e7-8443-00155d84c200","PlugInName":"PerformanceEquation","IsConfigured":False}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/analysisrules/{web_id}/analysisrules'.format(web_id='web_id_example'),
        headers=headers,
        json=analysis_rule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_rule_delete(client):
    """Test case for analysis_rule_delete

    Delete an Analysis Rule.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/analysisrules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_rule_get(client):
    """Test case for analysis_rule_get

    Retrieve an Analysis Rule.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysisrules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_rule_get_analysis_rules(client):
    """Test case for analysis_rule_get_analysis_rules

    Get the child Analysis Rules of the Analysis Rule.
    """
    params = [('maxCount', 56),
                    ('nameFilter', 'name_filter_example'),
                    ('searchFullHierarchy', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortField', 'sort_field_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('startIndex', 56),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysisrules/{web_id}/analysisrules'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_rule_get_by_path(client):
    """Test case for analysis_rule_get_by_path

    Retrieve an Analysis Rule by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysisrules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_rule_update(client):
    """Test case for analysis_rule_update

    Update an Analysis Rule by replacing items in its definition.
    """
    analysis_rule = {"Path":"\\\\MyAssetServer\\MyDatabase\\MyElement\\Analyses[MyAnalysis]\\AnalysisRule","ConfigString":"a := TagVal('sinusoid'); b := Pow(a, 2); c := a + b;","Description":"Runs a performance equation.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"VariableMapping":"b||Attribute1;c||Attribute2","EditorType":"OSIsoft.AF.Analysis.AnalysisRule.PEAnalysisRuleEditor","Name":"PerformanceEquation","HasChildren":False,"DisplayString":"a := TagVal('sinusoid'); b := Pow(a, 2); c := a + b;","SupportedBehaviors":["SupportsRunningCase","SupportStatePassing","OutputCorrectAfterSkipping"],"WebId":"I1XRXDqD5loBNH0erqeqJodtALAfyWdysKU5xGEQwAVXYTCAAfyWdysKU5xGEQwAVXYTCAA","Links":{"AnalysisTemplate":"AnalysisTemplate","Parent":"Parent","Analysis":"Analysis","AnalysisRules":"AnalysisRules","Self":"Self","PlugIn":"PlugIn"},"IsInitializing":False,"Id":"ca9d257f-94c2-11e7-8443-00155d84c200","PlugInName":"PerformanceEquation","IsConfigured":False}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/analysisrules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=analysis_rule,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

